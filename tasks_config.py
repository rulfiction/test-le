# tasks_config.py

TASKS = {
    1: {
        "title": "Сумма двух чисел",
        "description": "Напиши функцию sum_two(a, b), которая возвращает сумму a + b.",
        "function_name": "sum_two",
        "tests": [
            {"args": (1, 2), "expected": 3},
            {"args": (10, -5), "expected": 5},
            {"args": (0, 0), "expected": 0},
        ],
    },
    2: {
        "title": "Факториал",
        "description": "Напиши функцию factorial(n), которая возвращает n! для n >= 0.",
        "function_name": "factorial",
        "tests": [
            {"args": (0,), "expected": 1},
            {"args": (1,), "expected": 1},
            {"args": (5,), "expected": 120},
        ],
    },
}
