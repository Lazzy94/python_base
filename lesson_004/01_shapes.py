# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO сейчас видно что крайний вектор не доходит до первого есть разрыв
def triangle(start_point, angle, length):
    width = 3
    current_point = start_point
    # TODO рандж будем крутить от 0 до 361-120 с шагом 120
    for tilt_angle in range(angle, angle + 360, 120):
        # TODO а angle которую мы принимаем в параметрах используем вот тут angle=tilt_angle+angle
        # TODO в параметрах вектора дописать
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point
    # TODO а крайнею вектор мы будем рисовать линией sd.line (от, до, ширина)


point_0 = sd.get_point(10, 10)
triangle(start_point=point_0, angle=10, length=200)


def square(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 90):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


point_1 = sd.get_point(500, 10)
square(start_point=point_1, angle=80, length=200)


def pentagon(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 72):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


point_2 = sd.get_point(100, 300)
pentagon(start_point=point_2, angle=10, length=100)


def hexagon(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 60):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


point_3 = sd.get_point(350, 300)
hexagon(start_point=point_3, angle=10, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
