#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def zd3():
    sum = 1
    while True:
        message = int(input("Введите число: "))
        sum *= message
        if sum == 0:
            print('Произведение равно 0')
            break
        else:
            print(f'Полчившееся прозведение: {sum}')


if __name__ == '__main__':
    zd3()
