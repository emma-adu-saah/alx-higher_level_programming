#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        tuple_a = (0, 0)
    elif len(tuple_a) < 2 and tuple_a != ():
        tuple_a = (tuple_a[0], 0)

    if tuple_b == ():
        tuple_b = (0, 0)
    elif len(tuple_b) < 2 and tuple_b != ():
        tuple_b = (tuple_b[0], 0)

    new_list = []
    for i, j in zip(tuple_a, tuple_b):
        new_list.append(i + j)

    return tuple(new_list)
