# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)


def draw_smiles(x, y, color):
    sd.circle(center_position=sd.get_point(x, y), radius=50, width=2, color=color)
    sd.circle(center_position=sd.get_point(x - 20, y + 20), radius=10, width=2, color=color)
    sd.circle(center_position=sd.get_point(x + 20, y + 20), radius=7, width=2, color=color)
    mouth = [sd.get_point(x - 20, y - 10), sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20),
             sd.get_point(x + 20, y - 10)]
    sd.lines(point_list=mouth, width=2, color=color)


for _ in range(10):
    x = random.randint(200, 1000)
    y = random.randint(50, 500)
    draw_smiles(x, y, sd.random_color())

sd.pause()

# зачет!
