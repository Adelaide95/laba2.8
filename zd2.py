#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def circle(rad):
    p_circle = rad * rad * 3.14
    return p_circle


def cylinder():
    radius = float(input("Радиус цилиндра: "))
    height = float(input("Высота цилиндра: "))

    mes = input("Для вывода площади боковой поверхности"
                " введиите 1\nДля вывода полной площади"
                " цилиндра введите 2\n"
                " >>>> ")
    if mes.lower() == '1':
        bok = 2 * 3.14 * height * radius
        print(f'Площадь боковой поверхности = {bok}')
    elif mes.lower() == '2':
        whole = 2 * 3.14 * height * radius * (2 * circle(radius))
        print(f'Площадь всей поверхности = {whole}')
    else:
        print("Команда не опознана")


if __name__ == '__main__':
    cylinder()
