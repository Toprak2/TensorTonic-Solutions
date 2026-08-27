import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    sum = 0.0
    for num1, num2 in zip(x,y):
        sum += num1 * num2

    return sum