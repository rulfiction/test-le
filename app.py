# app.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict, Any

from tasks_config import TASKS

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def normalize(s: str) -> str:
    # можно усложнить при желании
    return s.strip()


def run_tests(task_id: int, user_answer: str) -> Dict[str, Any]:
    task = TASKS[task_id]
    tests = task["tests"]

    norm_answer = normalize(user_answer)
    details = []
    all_passed = True

    for i, test in enumerate(tests, start=1):
        expected = normalize(test["expected"])
        if norm_answer == expected:
            details.append({
                "test": i,
                "status": "ok",
                "expected": test["expected"],
                "result": user_answer,
            })
        else:
            all_passed = False
            details.append({
                "test": i,
                "status": "fail",
                "expected": test["expected"],
                "result": user_answer,
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
    
@app.post("/tasks/{task_id}/submit", response_class=HTMLResponse)
async def submit_solution(request: Request, task_id: int, answer: str = Form(...)):
    task = TASKS.get(task_id)
    if not task:
        return HTMLResponse("Задача не найдена", status_code=404)

    result = run_tests(task_id, answer)
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "task": task,
            "answer": answer,
            "result": result,
        },
    )
