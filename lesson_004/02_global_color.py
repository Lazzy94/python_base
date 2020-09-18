# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
def triangle(start_point, angle, length, color):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 120):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw(color=color)
        current_point = v.end_point


def square(start_point, angle, length, color):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 90):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw(color=color)
        current_point = v.end_point


point_1 = sd.get_point(500, 10)


def pentagon(start_point, angle, length, color):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 72):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw(color=color)
        current_point = v.end_point


point_2 = sd.get_point(100, 300)


def hexagon(start_point, angle, length, color):
    width = 3
    current_point = start_point
    for tilt_angle in range(angle, angle + 360, 60):
        v = sd.get_vector(start_point=current_point, angle=tilt_angle, length=length, width=width)
        v.draw(color=color)
        current_point = v.end_point


point_3 = sd.get_point(350, 300)

colors = {
    0: {'name': 'red', 'sd_object': sd.COLOR_RED},
    1: {'name': 'orange', 'sd_object': sd.COLOR_ORANGE},
    2: {'name': 'yellow', 'sd_object': sd.COLOR_YELLOW},
    3: {'name': 'green', 'sd_object': sd.COLOR_GREEN},
    4: {'name': 'cyan', 'sd_object': sd.COLOR_CYAN},
    5: {'name': 'blue', 'sd_object': sd.COLOR_BLUE},
    6: {'name': 'purple', 'sd_object': sd.COLOR_PURPLE},
}

point_0 = sd.get_point(10, 10)
while True:
    print('Возможные цвета')
    for color_index, color_definition in colors.items():
        print(color_index, ':', color_definition['name'])
    user_input = input('Введите желаемый цвет > ')
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input in colors:
            hexagon(start_point=point_3, angle=10, length=100, color=colors[user_input]['sd_object'])
            pentagon(start_point=point_2, angle=10, length=100, color=colors[user_input]['sd_object'])
            square(start_point=point_1, angle=80, length=200, color=colors[user_input]['sd_object'])
            triangle(start_point=point_0, angle=10, length=200, color=colors[user_input]['sd_object'])
            break
        else:
            print('Вы ввели некорректный номер')
    else:
        print('Номер цвета должен быть числом')
sd.pause()
