#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    zd4 = input('Введите строку: ')
    test_input(zd4)

def test_input(zd4):
    try:
        str_to_int(zd4)
    except ValueError:
        print('Нельзя преобразовать в число')


def str_to_int(zd4):
    i = int(zd4)
    print_int(i)


def print_int(i):
    print(i)


if __name__ == '__main__':
    get_input()
