TASKS = {
    1: {
        "title": "Привет, мир",
        "short": "Напечатать простое сообщение",
        "description": "Заполни Debug.Log так, чтобы он выводил 'Привет, мир!'.",
        "snippet": 'Debug.Log("___");',
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": 'Привет, мир!'},
        ],
    },

    2: {
        "title": "Сложение чисел",
        "short": "Вывести сумму",
        "description": "Вставь выражение для вывода суммы a и b.",
        "snippet": 'int a = 5;\nint b = 3;\nDebug.Log("Результат: " + ___);',
        "input_label": "Что вставить?",
        "tests": [
            {"expected": 'a + b'},
        ],
    },

    3: {
        "title": "Показать переменную",
        "short": "Вывести score",
        "description": "Заполни Debug.Log так, чтобы он выводил значение score.",
        "snippet": 'int score = 100;\nDebug.Log("Score = " + ___);',
        "tests": [
            {"expected": 'score'},
        ],
        "input_label": "Вставь недостающую часть:"
    },

    4: {
        "title": "Приветствие",
        "short": "Вывести имя",
        "description": "Вставь переменную name.",
        "snippet": 'string name = "Alex";\nDebug.Log("Привет, " + ___ + "!");',
        "tests": [{"expected": 'name'}],
        "input_label": "Что вставить?"
    },

    5: {
        "title": "Скорость",
        "short": "Вывести speed",
        "description": "Нужно вывести значение скорости.",
        "snippet": 'float speed = 4.5f;\nDebug.Log("Speed: " + ___ + " m/s");',
        "tests": [{"expected": 'speed'}],
        "input_label": "Что вставить?"
    },

    6: {
        "title": "Сумма трёх чисел",
        "short": "Вывести сумму",
        "description": "Вставь выражение для суммы трех чисел.",
        "snippet": 'int a = 2, b = 4, c = 6;\nDebug.Log("Sum = " + (___));',
        "tests": [{"expected": 'a + b + c'}],
        "input_label": "Что вставить?"
    },

    7: {
        "title": "Победа",
        "short": "Вывести победителя",
        "description": "Вставь номер игрока.",
        "snippet": 'Debug.Log("Player " + ___ + " wins!");',
        "tests": [{"expected": '1'}],
        "input_label": "Что вставить?"
    },

    8: {
        "title": "Координаты позиции",
        "short": "Вывести pos.x",
        "description": "Выведи координату X.",
        "snippet": 'Vector3 pos = new Vector3(1, 2, 3);\nDebug.Log("Position: " + pos.___);',
        "tests": [{"expected": 'x'}],
        "input_label": "Что вставить?"
    },

    9: {
        "title": "Жизни",
        "short": "Вывести lives",
        "description": "Выведи количество жизней.",
        "snippet": 'int lives = 3;\nDebug.Log("Lives left: " + ___);',
        "tests": [{"expected": 'lives'}],
        "input_label": "Что вставить?"
    },

    10: {
        "title": "Game Over",
        "short": "Простой текст",
        "description": "Нужно вывести Game Over.",
        "snippet": 'Debug.Log("___");',
        "tests": [{"expected": 'Game Over'}],
        "input_label": "Что вставить?"
    },
}
