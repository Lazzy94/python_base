# -*- coding: utf-8 -*-

import simple_draw as sd

COLOR_RED = (255, 0, 0)
sd.random_color()
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, color=sd.random_color()):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)


point = sd.get_point(900, 600)
bubble(point=point, step=10, color=sd.random_color())

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1100, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5, color=sd.random_color())

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5, color=sd.random_color())

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5, color=sd.random_color())

sd.pause()

# Начиная с третьего модуля буду обращать внимание на то что подчеркивает Пайчар. Придерживаемся PEP8
# Можно привести все к нужному формату code\Reformat code

# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме
