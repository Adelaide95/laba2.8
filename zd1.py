#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def zd1():
    sentence = int(input('Введите целое число:'))
    if sentence > 0:
        positive(sentence)
    else:
        negative(sentence)


def negative(sentence):
    print(f'Число {sentence} отрицательное')


def positive(sentence):
    print(f"Число {sentence} положительное")


if __name__ == '__main__':
    zd1()
