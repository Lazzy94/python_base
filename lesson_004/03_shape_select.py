# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


# TODO используем обновленный код от 01 задания
def triangle(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 120):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


def square(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 90):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


def pentagon(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 72):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


def hexagon(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 60):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw()
        current_point = v.end_point


point_0 = sd.get_point(150, 150)
figures = {
    0: {'name': 'треугольник', 'paint_function': triangle, 'length': 200, 'angle': 0},
    1: {'name': 'квадрат', 'paint_function': square, 'length': 200, 'angle': 0},
    2: {'name': 'пятиугольник', 'paint_function': pentagon, 'length': 100, 'angle': 0},
    3: {'name': 'шестиугольник', 'paint_function': hexagon, 'length': 100, 'angle': 0},
}

while True:
    # TODO вынести до основного цикла while
    print('Возможные фигуры')
    for figures_index, figures_definition in figures.items():
        print(figures_index, ':', figures_definition['name'])
    user_input = input('Введите желаемую фигуру > ')
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input in figures:
            paint_function = figures[user_input]['paint_function']
            paint_function(start_point=point_0,
                           angle=figures[user_input]['angle'],
                           length=figures[user_input]['length'])
            break
        else:
            print('Вы ввели некоректный номер!')
    else:
        print('Номер фигуры должен быть числом')

sd.pause()
