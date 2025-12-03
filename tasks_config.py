BLOCKS = {
    "debug": {
        "title": "Основы Debug.Log()",
        "description": "Простые задачи на вывод текста и переменных в консоль Unity.",
        "theory": """
<h3>Что такое Debug.Log()</h3>
<p><code>Debug.Log()</code> — это функция Unity, которая выводит сообщение в окно Console.
С её помощью мы можем увидеть, что делает наш код: какие строки выполняются и какие значения имеют переменные.</p>

<h4>Когда используется Debug.Log</h4>
<ul>
  <li><strong>Проверка, что скрипт работает.</strong> В методе <code>Start()</code> можно вывести сообщение и убедиться, что компонент включён.</li>
  <li><strong>Поиск ошибок.</strong> Если что-то ведёт себя странно, выводим значения переменных и понимаем, где проблема.</li>
  <li><strong>Обучение программированию.</strong> Ученик сразу видит результат работы кода.</li>
</ul>

<h4>Что можно выводить</h4>
<ul>
  <li>текст: <code>Debug.Log("Привет, мир!");</code></li>
  <li>числа: <code>Debug.Log(5);</code></li>
  <li>переменные: <code>Debug.Log(score);</code></li>
  <li>выражения: <code>Debug.Log(a + b);</code></li>
  <li>смешанный текст и значение: <code>Debug.Log("Счёт: " + score);</code></li>
</ul>

<h4>Почему это важно</h4>
<p>Пока мы не видим, что происходит «внутри» программы, мы можем только догадываться.
<code>Debug.Log()</code> позволяет заглянуть внутрь кода и понять, что именно сейчас считает компьютер.</p>
        """,
    },
    "math": {
        "title": "Математика и Debug.Log()",
        "description": "Простые примеры с числами: сложение, вычитание, умножение, деление.",
        "theory": """
<h3>Математические операции в Unity</h3>
<p>Скрипт в Unity может работать как калькулятор: складывать, вычитать, умножать и делить числа.
Через <code>Debug.Log()</code> мы можем увидеть результат этих действий.</p>

<h4>Основные операции</h4>
<ul>
  <li><strong>Сложение:</strong> <code>Debug.Log(3 + 5); // 8</code></li>
  <li><strong>Вычитание:</strong> <code>Debug.Log(10 - 4); // 6</code></li>
  <li><strong>Умножение:</strong> <code>Debug.Log(2 * 3); // 6</code></li>
  <li><strong>Деление:</strong> <code>Debug.Log(8 / 2); // 4</code></li>
</ul>

<h4>Переменные и выражения</h4>
<pre><code>int a = 4;
int b = 7;
Debug.Log(a + b);              // выведет 11
Debug.Log("Сумма: " + (a + b));
</code></pre>

<p>Скобки важны: сначала считается <code>a + b</code>, потом результат превращается в текст и склеивается со строкой <code>"Сумма: "</code>.</p>

<h4>Зачем это нужно в играх</h4>
<ul>
  <li>считать здоровье, урон, очки;</li>
  <li>вычислять скорость и положение объектов;</li>
  <li>проверять, правильно ли работает логика игры.</li>
</ul>

<p>Этот блок задач помогает привыкнуть к тому, что компьютер не просто «что-то показывает на экране»,
а активно считает числа и использует их в игровом процессе.</p>
        """,
    },
}
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
        "block_id": "debug",
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
        "block_id": "debug",
    },

    3: {
        "title": "Показать переменную",
        "short": "Вывести score",
        "description": "Заполни Debug.Log так, чтобы он выводил значение score.",
        "snippet": 'int score = 100;\nDebug.Log("Score = " + ___);',
        "tests": [
            {"expected": 'score'},
        ],
        "block_id": "debug",
        "input_label": "Вставь недостающую часть:"
    },

    4: {
        "title": "Приветствие",
        "short": "Вывести имя",
        "description": "Вставь переменную name.",
        "snippet": 'string name = "Alex";\nDebug.Log("Привет, " + ___ + "!");',
        "tests": [{"expected": 'name'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },

    5: {
        "title": "Скорость",
        "short": "Вывести speed",
        "description": "Нужно вывести значение скорости.",
        "snippet": 'float speed = 4.5f;\nDebug.Log("Speed: " + ___ + " m/s");',
        "tests": [{"expected": 'speed'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },

    6: {
        "title": "Сумма трёх чисел",
        "short": "Вывести сумму",
        "description": "Вставь выражение для суммы трех чисел.",
        "snippet": 'int a = 2, b = 4, c = 6;\nDebug.Log("Sum = " + (___));',
        "tests": [{"expected": 'a + b + c'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },

    7: {
        "title": "Победа",
        "short": "Вывести победителя",
        "description": "Вставь номер игрока.",
        "snippet": 'Debug.Log("Player " + ___ + " wins!");',
        "tests": [{"expected": '1'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },

    8: {
        "title": "Координаты позиции",
        "short": "Вывести pos.x",
        "description": "Выведи координату X.",
        "snippet": 'Vector3 pos = new Vector3(1, 2, 3);\nDebug.Log("Position: " + pos.___);',
        "tests": [{"expected": 'x'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },

    9: {
        "title": "Жизни",
        "short": "Вывести lives",
        "description": "Выведи количество жизней.",
        "snippet": 'int lives = 3;\nDebug.Log("Lives left: " + ___);',
        "tests": [{"expected": 'lives'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },

    10: {
        "title": "Game Over",
        "short": "Простой текст",
        "description": "Нужно вывести Game Over.",
        "snippet": 'Debug.Log("___");',
        "tests": [{"expected": 'Game Over'}],
        "block_id": "debug",
        "input_label": "Что вставить?"
    },
}
TASKS.update({
    11: {
        "title": "Сложение двух чисел",
        "short": "a + b",
        "description": "Выведи сумму двух целых чисел a и b.",
        "snippet": 'int a = 2;\nint b = 3;\nDebug.Log(___);',
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "a + b"},
        ],
        "block_id": "math",
    },

    12: {
        "title": "Вычитание",
        "short": "a - b",
        "description": "Выведи разность двух чисел a и b.",
        "snippet": 'int a = 10;\nint b = 4;\nDebug.Log(___);',
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "a - b"},
        ],
        "block_id": "math",
    },

    13: {
        "title": "Умножение",
        "short": "x * y",
        "description": "Выведи результат умножения x и y.",
        "snippet": 'int x = 3;\nint y = 5;\nDebug.Log(___);',
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "x * y"},
        ],
        "block_id": "math",
    },

    14: {
        "title": "Деление с результатом double",
        "short": "a / b (double)",
        "description": "Выведи результат деления a на b как число с точкой.",
        "snippet": 'int a = 7;\nint b = 2;\nDebug.Log((double)___ / ___);',
        "input_label": "Что вставить вместо пропусков?",
        "tests": [
            {"expected": "a"},
            # для простоты можно сделать одну строку expected, но тогда меняем сниппет.
        ],
        "block_id": "math",
    },

    15: {
        "title": "Остаток от деления",
        "short": "a % b",
        "description": "Выведи остаток от деления a на b.",
        "snippet": 'int a = 17;\nint b = 5;\nDebug.Log(___);',
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "a % b"},
        ],
        "block_id": "math",
    },
})
