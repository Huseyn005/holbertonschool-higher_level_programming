#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples or slice them to ensure we are working with at least 2 elements
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    return (a[0] + b[0], a[1] + b[1])
