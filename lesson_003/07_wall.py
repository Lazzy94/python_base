# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

left_bottom_x = 0
left_bottom_y = 0
right_top_x = 100
right_top_y = 50

width = 3
color = sd.COLOR_DARK_ORANGE


for line_number in range(0, 15):
    if line_number % 2 == 0:
        left_bottom_x = 0
        plus_for_right_top_x = 0
    else:
        left_bottom_x = -50
        plus_for_right_top_x = 50
    for right_top_x in range(100, 900, 100):
        right_top_x += plus_for_right_top_x
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=3)
        left_bottom_x += 100
    left_bottom_y += 50
    right_top_y += 50


# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()

# зачет!
