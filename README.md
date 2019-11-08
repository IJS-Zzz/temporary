# Test solution for Ramax

### Task 1
Создать декоратор, который засекает время выполнения обернутой им функции и выводит его в консоль через print.

[Решение](time_decorator.py)  
[Тесты](tests/test_time_decorator.py)  

### Task 2
Создать итератор, который принимает в конструктор итерируемый объект и признак чет/нечет
и возвращает только элементы с четной или нечетной (в соответствии с признаком, переданным
в конструктор) позицией в итерируемом объекте. Например, для последовательности a, b, c, d
"чет" вернет b, d (2-й и 4-й элементы), а "нечет" a, c  (1-й и 3-й элементы).  

[Решение](iterator.py)  
[Тесты](tests/test_iterator.py)  

### Task 3
Создать функцию, принимающую на вход строку и возвращающую True/False в зависимости от того,
можно ли перестановкой символов получить из нее палиндром (строку, одинаково читающуюся
слева направо и справа налево).  
Примеры:
* "abba" - да, уже палиндром
* "bbaa" - да, можно переставить, например, в "abba" или "baab"
* "bcaaabc" - да, можно переставить, например, в "bcaaacb"
* "bcbcbc" – нет

[Решение](palindrome.py)  
[Тесты](tests/test_palindrome.py)  

### Task 4
Рефакторинг кода. В файле [badcode.py](badcode.py) приведена функция, написанная плохо, нечитаемо
и с ошибками. Требуется понять, что функция делает и переписать ее так, чтобы код был
понятен и работал без ошибок.

[Решение](badcode_refactored.py)  
[Тесты](tests/test_badcode_refactored.py)  

### Note
Представленный код тестировался на Python 3.

### Tests
Запуск тестов
```
cd %path_to_dir%
bash run_tests.sh
```
или
```
cd %path_to_dir%
python -m unittest discover -v -s ./tests/
```

:rocket:
