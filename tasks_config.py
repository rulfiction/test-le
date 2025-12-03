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
     "movement": {
        "title": "Движение объекта",
        "description": "Задачи на движение и поворот объекта через transform.",
        "theory": """
<h3>Движение объекта в Unity</h3>

<p>У каждого объекта в Unity есть компонент <code>Transform</code>. 
Он хранит позицию, поворот и масштаб объекта в трёхмерном мире.</p>

<ul>
  <li><strong>position</strong> — где находится объект;</li>
  <li><strong>rotation</strong> — как он повёрнут;</li>
  <li><strong>localScale</strong> — во сколько раз растянут или уменьшен.</li>
</ul>

<p>Чаще всего движение делают в методе <code>Update()</code>. 
Этот метод вызывается каждый кадр игры, то есть много раз в секунду.</p>

<h4>Простое движение</h4>

<p>Один из самых простых способов двигать объект — использовать метод 
<code>transform.Translate(...)</code>. Он сдвигает объект на вектор, который мы передаём.</p>

<pre><code>void Update()
{
    // каждую секунду немного двигаем объект вправо
    transform.Translate(Vector3.right);
}</code></pre>

<ul>
  <li><code>Vector3.right</code> — вектор (1, 0, 0), движение по оси X вправо;</li>
  <li><code>Vector3.left</code> — (−1, 0, 0);</li>
  <li><code>Vector3.up</code> — (0, 1, 0);</li>
  <li><code>Vector3.down</code> — (0, −1, 0);</li>
  <li><code>Vector3.forward</code> — (0, 0, 1);</li>
  <li><code>Vector3.back</code> — (0, 0, −1).</li>
</ul>

<h4>Скорость движения</h4>

<p>Чтобы управлять скоростью, обычно заводят переменную <code>speed</code>:</p>

<pre><code>public float speed = 2f;

void Update()
{
    transform.Translate(Vector3.right * speed * Time.deltaTime);
}</code></pre>

<p><code>Time.deltaTime</code> — время (в секундах) между кадрами. 
Если домножать движение на <code>deltaTime</code>, то объект будет двигаться 
равномерно на разных компьютерах.</p>

<h4>Поворот объекта</h4>

<p>Повернуть объект можно методом <code>transform.Rotate(...)</code>:</p>

<pre><code>public float rotationSpeed = 90f;

void Update()
{
    // поворот вокруг оси Y
    transform.Rotate(0, rotationSpeed * Time.deltaTime, 0);
}</code></pre>

<p>Так мы задаём скорость поворота в градусах в секунду.</p>

<p>В задачах этого блока мы потренируемся:</p>
<ul>
  <li>двигать объект в разные стороны;</li>
  <li>использовать <code>Vector3</code> для направления;</li>
  <li>подставлять переменную скорости в формулу движения или поворота.</li>
</ul>
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

TASKS.update({
    16: {
        "title": "Движение вправо",
        "short": "Translate вправо",
        "description": "Сделай так, чтобы объект каждый кадр немного двигался вправо по оси X.",
        "snippet": "void Update()\n{\n    transform.Translate(___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "Vector3.right"},
        ],
        "block_id": "movement",
    },

    17: {
        "title": "Движение вперёд",
        "short": "Translate вперёд",
        "description": "Сделай так, чтобы объект двигался вперёд по оси Z.",
        "snippet": "void Update()\n{\n    transform.Translate(___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "Vector3.forward"},
        ],
        "block_id": "movement",
    },

    18: {
        "title": "Скорость движения",
        "short": "speed по Z",
        "description": "Используй переменную speed, чтобы задать скорость движения вперёд.",
        "snippet": "public float speed = 2f;\n\nvoid Update()\n{\n    transform.Translate(Vector3.forward * ___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "speed"},
        ],
        "block_id": "movement",
    },

    19: {
        "title": "Скорость + deltaTime",
        "short": "равномерное движение",
        "description": "Сделай так, чтобы движение вправо не зависело от FPS (используй Time.deltaTime).",
        "snippet": "public float speed = 3f;\n\nvoid Update()\n{\n    transform.Translate(Vector3.right * ___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "speed * Time.deltaTime"},
        ],
        "block_id": "movement",
    },

    20: {
        "title": "Диагональное движение",
        "short": "вперёд и вправо",
        "description": "Сделай так, чтобы объект двигался одновременно вперёд и вправо.",
        "snippet": "void Update()\n{\n    transform.Translate(___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "Vector3.right + Vector3.forward"},
        ],
        "block_id": "movement",
    },

    21: {
        "title": "Изменение позиции через position",
        "short": "position + вектор",
        "description": "Сделай шаг вверх, напрямую изменяя transform.position.",
        "snippet": "void Update()\n{\n    transform.position = ___;\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "transform.position + Vector3.up"},
        ],
        "block_id": "movement",
    },

    22: {
        "title": "Поворот вокруг оси Y",
        "short": "rotationSpeed",
        "description": "Используй rotationSpeed и Time.deltaTime, чтобы крутить объект вокруг оси Y.",
        "snippet": "public float rotationSpeed = 90f;\n\nvoid Update()\n{\n    transform.Rotate(0, ___, 0);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "rotationSpeed * Time.deltaTime"},
        ],
        "block_id": "movement",
    },

    23: {
        "title": "Движение с Input (вперёд-назад)",
        "short": "Vertical",
        "description": "Используй ось Vertical, чтобы двигать объект вперёд и назад по Z.",
        "snippet": "public float speed = 5f;\n\nvoid Update()\n{\n    float v = Input.GetAxis(\"Vertical\");\n    transform.Translate(Vector3.forward * v * ___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "speed * Time.deltaTime"},
        ],
        "block_id": "movement",
    },

    24: {
        "title": "Движение с Input (влево-вправо)",
        "short": "Horizontal",
        "description": "Используй ось Horizontal, чтобы двигать объект влево и вправо по X.",
        "snippet": "public float speed = 5f;\n\nvoid Update()\n{\n    float h = Input.GetAxis(\"Horizontal\");\n    transform.Translate(Vector3.right * h * ___);\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "speed * Time.deltaTime"},
        ],
        "block_id": "movement",
    },

    25: {
        "title": "Остановка при нулевом Input",
        "short": "нет движения без ввода",
        "description": "Здесь код уже не двигает объект при нулевом вводе, но закрепим формулу движения.",
        "snippet": "public float speed = 4f;\n\nvoid Update()\n{\n    float h = Input.GetAxis(\"Horizontal\");\n    if (h != 0)\n    {\n        transform.Translate(Vector3.right * h * ___);\n    }\n}",
        "input_label": "Что вставить вместо ___ ?",
        "tests": [
            {"expected": "speed * Time.deltaTime"},
        ],
        "block_id": "movement",
    },
})
