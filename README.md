Это программа "Калькулятор".
На момент релиза 3.1 все кнопки работают.
Если вы заметили некоторые баги, сообщите о них разработчику vk.com/drmattsuu

MANUAL
C -> Полностью очищает память калькулятора.
10->2 -> Переводит одно число в двоичную систему.
10->8 -> Переводит одно число в восьмеричную систему.
10->16 -> Переводит одно число в шестнадцатеричную систему.
16->10 -> Переводит одно число из шестнадцатеричной в десятичную систему.
8->10 -> Переводит одно число из восьмеричной в десятичную систему.
2->10 -> Переводит одно число из двоичной в десятичную систему.
% -> Вычисляет процент от числа (5% = 0.05, 5×5% = 0.25).
Alt -> Переключает режим определённых кнопок.
Del -> Удаляет последнюю цифру НО! не удаляет знаки.
X! -> Считает факториал числа от 1 до 12.
√X -> Считает корень из данного числа.
Х² -> Считает квадрат данного числа.
1/X -> Делит единицу на данное число.
Ans -> Запоминает результат выражения для следующего подсчёта.
Буквы A-F на кнопках нужны для того, чтобы записать число в 16-ричной системе.

ПОЯСНЕНИЯ ПО КОДУ
1-14, 507-510 - настройки программы.
16-46 - обработка нажатия кнопок.
48-74 - настройка цветов кнопок.
76-91 - если нажата кнопка "разделить"(/), то записать число в список чисел, а знак деления в список знаков деления. Если предыдущий символ в общей строке - знак, а не цифра, то поменять его на новый нажатый. При ошибке вывести Error, иначе вывести общий введённый текст в label над LCD.
93-163 - аналогичные функции для суммы, разности, умножения и процента.
165-171 - функция alt, которая при нажатии кнопки переключает некоторые кнопки для 16-ричной системы.
173-267 - функции цифр.
269-272 - функция С, которая при нажатии соответствующей кнопки очищает память калькулятора.
274-278 - функция, которая ставит точку.
280-293 - функция, которая удаляет последнюю цифру, если та введена неверно.
295-310 - функция факториала, которая, если число находится в промежутке 1-12(допустимое значение ответа в LCD), считает и выводит его факториал, иначе ошибка.
312-321 - функция делит единицу на полученое число и выводит результат.
323-334 - функция считает корень из данного числа и выводит результат. Если число меньше 0 - ошибка.
336-345 - функция считает квадрат числа.
347-392 - функция, которая срабатывает при нажатии кнопки =. В неё поступает список чисел и знаков. Если первый знак в общем примере -, то функция умножает первое число в списке чисел на -1, а - из списка знаков удаляет. Далее, пока в списке знаков есть что-то, функция считает пример по правилам математики: сначала процент, потом умножение и деление, затем складывание и вычитание. Например, если в списке знаков есть умножить, то функция умножает число с номером знака на последующее, присваивает результат ячейке с номером знака, удаляет следующее число, которое уже преобразовалось, после всего удаляет знак и прерывает функцию, так как она делается через for. После всех вычислений список знаков остаётся пустым, а в списке чисел остаётся 1 число - результат, который выводится на LCD. После этого все данные калькулятора принудительно очищаются. При любом отходе от данного алгоритма программа выдаёт ошибку.
395-402 - кнопка, которая позволяет использовать результат для следующего вычисления.
404-511 - функции перевода чисел из одной системы счисления в другую, работающие по основным правилам перевода.
