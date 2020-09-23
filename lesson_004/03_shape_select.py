# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def triangle(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 240, 120):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle + angle, length=length, width=width)
        v.draw()
        current_point = v.end_point
    sd.line(start_point=point_0, end_point=v.end_point, width=width)


point_0 = sd.get_point(10, 10)


def square(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 361 - 120, 90):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle + angle, length=length, width=width)
        v.draw()
        current_point = v.end_point
    sd.line(start_point=point_1, end_point=v.end_point, width=width)


point_1 = sd.get_point(500, 200)


def pentagon(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 361 - 72, 72):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle + angle, length=length, width=width)
        v.draw()
        current_point = v.end_point
    sd.line(start_point=point_2, end_point=v.end_point, width=width)


point_2 = sd.get_point(100, 300)


def hexagon(start_point, angle, length):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 361 - 60, 60):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle + angle, length=length, width=width)
        v.draw()
        current_point = v.end_point
    sd.line(start_point=point_3, end_point=v.end_point, width=width)


point_3 = sd.get_point(350, 300)
figures = {
    0: {'name': 'треугольник', 'paint_function': triangle, 'length': 200, 'angle': 0},
    1: {'name': 'квадрат', 'paint_function': square, 'length': 200, 'angle': 0},
    2: {'name': 'пятиугольник', 'paint_function': pentagon, 'length': 100, 'angle': 0},
    3: {'name': 'шестиугольник', 'paint_function': hexagon, 'length': 100, 'angle': 0},
}
print('Возможные фигуры')
while True:
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
