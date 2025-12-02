# app.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from tasks_config import TASKS
from auth import init_db, verify_user, create_user, add_submission, get_rating

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="super-secret-key-change-me")

templates = Jinja2Templates(directory="templates")

# создаём таблицы в БД при старте приложения
init_db()


# ========= ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =========

def get_current_user(request: Request):
    """Вернуть текущего залогиненного пользователя из сессии или None."""
    return request.session.get("user")


def normalize(s: str) -> str:
    return s.strip()


def run_tests(task_id: int, user_code: str):
    """Проверка ответа: просто сравниваем строку с ожидаемой."""
    task = TASKS[task_id]
    tests = task["tests"]

    norm_code = normalize(user_code)
    details = []
    all_passed = True

    for i, test in enumerate(tests, start=1):
        expected = normalize(test["expected"])
        if norm_code == expected:
            details.append({
                "test": i,
                "status": "ok",
                "expected": test["expected"],
                "result": user_code,
            })
        else:
            all_passed = False
            details.append({
                "test": i,
                "status": "fail",
                "expected": test["expected"],
                "result": user_code,
            })

    return {
        "ok": all_passed,
        "error": None,
        "details": details,
    }


# ========= МАРШРУТЫ ЗАДАЧ =========

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": TASKS, "user": user},
    )


@app.get("/tasks/{task_id}", response_class=HTMLResponse)
async def task_detail(request: Request, task_id: int):
    user = get_current_user(request)
    if not user:
        # только залогиненные могут решать
        return RedirectResponse("/login", status_code=302)

    task = TASKS.get(task_id)
    if not task:
        return HTMLResponse("Задача не найдена", status_code=404)

    return templates.TemplateResponse(
        "task_detail.html",
        {"request": request, "task_id": task_id, "task": task, "user": user},
    )


@app.post("/tasks/{task_id}/submit", response_class=HTMLResponse)
async def submit_solution(
    request: Request,
    task_id: int,
    code: str = Form(...),
):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    task = TASKS.get(task_id)
    if not task:
        return HTMLResponse("Задача не найдена", status_code=404)

    result = run_tests(task_id, code)

    # записываем попытку в БД (для рейтинга)
    add_submission(
        user_id=user["id"],
        task_id=task_id,
        is_correct=result["ok"],
        answer=code,
    )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "task": task,
            "code": code,
            "result": result,
            "user": user,
        },
    )


# ========= РЕГИСТРАЦИЯ / ЛОГИН / ЛОГАУТ =========

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse(
        "register.html",
        {"request": request, "user": user, "error": None},
    )


@app.post("/register", response_class=HTMLResponse)
async def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    ok = create_user(username, password)
    if not ok:
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "user": None,
                "error": "Такое имя уже занято",
            },
            status_code=400,
        )

    # сразу логиним после успешной регистрации
    user = verify_user(username, password)
    request.session["user"] = user
    return RedirectResponse("/", status_code=302)


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "user": user, "error": None},
    )


@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    user = verify_user(username, password)
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "user": None,
                "error": "Неверный логин или пароль",
            },
            status_code=400,
        )
    request.session["user"] = user
    return RedirectResponse("/", status_code=302)


@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse("/", status_code=302)


# ========= РЕЙТИНГ =========

@app.get("/rating", response_class=HTMLResponse)
async def rating_page(request: Request):
    user = get_current_user(request)
    rating = get_rating()
    return templates.TemplateResponse(
        "rating.html",
        {"request": request, "user": user, "rating": rating},
    )
