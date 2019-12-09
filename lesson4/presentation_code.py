def min_sec(x):  # Создать функцию и связать ее с именем
    return x * 60  # Тело, выполняемое при вызове функции


value = min_sec(30)  # Вызов функции
print(value)  # Что выведет print?

x = 10


def my_func(a, b):
    print(x)
    z = 5


my_func(1, 4)
print(z)

x = 10


def my_func(a, b):
    x = x + 1
    print(x)


my_func(1, 4)

def degree(x, a = 2):
    f = x**a
    return f
print(degree(5), degree(5, 3), degree(2, a = 5))

print(degree(a = 5))

def unknown(*args):
    for argument in args:
        print ( argument )

func = lambda x, y: x + y
func(1, 2) # 3
func('a', 'b') # 'ab‘

(lambda x, y: x + y)(1, 2) # 3
(lambda x, y: x + y)('a', 'b') # 'ab‘
