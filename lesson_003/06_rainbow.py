# -*- coding: utf-8 -*-

# (цикл for)
import pygame
import simple_draw as sd
from pygame import draw

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
# start_point = sd.get_point(50, 50)
# end_point = sd.get_point(350, 450)
width = 4
start_point_x = 50
start_point_y = 50
end_point_x = 350
end_point_y = 450

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

for rainbow_color in rainbow_colors:
    start_point = sd.get_point(start_point_x, start_point_y)
    end_point = sd.get_point(end_point_x, end_point_y)
    sd.line(start_point=start_point, end_point=end_point, color=rainbow_color, width=width)
    start_point_x += 5
    end_point_x += 5


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

radius = 500
point_x = 300
width = 10
point_y = -50
for rainbow_color in rainbow_colors:
    point = sd.get_point(point_x, point_y)
    sd.circle(center_position=point, radius=radius, width=width, color=rainbow_color)
    point_y -= 5
    radius -= 5


sd.pause()
