# app.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from tasks_config import TASKS

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def run_tests(task_id: int, user_code: str):
    task = TASKS[task_id]
    func_name = task["function_name"]
    tests = task["tests"]

    ns = {}
    try:
        exec(user_code, ns)
    except Exception as e:
        return {
            "ok": False,
            "error": f"Ошибка при выполнении кода: {e}",
            "details": [],
        }

    if func_name not in ns or not callable(ns[func_name]):
        return {
            "ok": False,
            "error": f"Не найдена функция {func_name}",
            "details": [],
        }

    func = ns[func_name]
    details = []
    all_passed = True

    for i, test in enumerate(tests, start=1):
        args = test["args"]
        expected = test["expected"]
        try:
            result = func(*args)
        except Exception as e:
            all_passed = False
            details.append({
                "test": i,
                "status": "error",
                "args": args,
                "expected": expected,
                "result": str(e),
            })
            continue

        if result == expected:
            details.append({
                "test": i,
                "status": "ok",
                "args": args,
                "expected": expected,
                "result": result,
            })
        else:
            all_passed = False
            details.append({
                "test": i,
                "status": "fail",
                "args": args,
                "expected": expected,
                "result": result,
            })

    return {
        "ok": all_passed,
        "error": None,
        "details": details,
    }


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": TASKS},
    )


@app.get("/tasks/{task_id}", response_class=HTMLResponse)
async def task_detail(request: Request, task_id: int):
    task = TASKS.get(task_id)
    if not task:
        return HTMLResponse("Задача не найдена", status_code=404)
    return templates.TemplateResponse(
        "task_detail.html",
        {"request": request, "task_id": task_id, "task": task},
    )


@app.post("/tasks/{task_id}/submit", response_class=HTMLResponse)
async def submit_solution(request: Request, task_id: int, code: str = Form(...)):
    task = TASKS.get(task_id)
    if not task:
        return HTMLResponse("Задача не найдена", status_code=404)

    result = run_tests(task_id, code)
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "task": task,
            "code": code,
            "result": result,
        },
    )
