import random
import numpy as np
from math import floor, ceil


def fuzzy_round(x: float, break_point=0.5) -> int:
    decimal_part = x - int(x)

    if decimal_part >= break_point:
        return ceil(x)
    else:
        return floor(x)


def fuzzy_integer_distribution(x: int, multiplier: list, round_type='fuzzy', break_point=0.8, guider=None):
    assert isinstance(x, int), "Number must be integers."
    assert isinstance(multiplier, list), "Multiplier must be a list"
    assert sum(multiplier) <= 1.0, "Distribuation multipler sum cann't be more than 1"
    assert round_type in ['floor', 'hard', 'fuzzy'], "Mode can only take values hard and soft"
    assert break_point < 1, "Fuzzy Break Point needs to be less than 1"
    assert break_point > 0, "Fuzzy Break Point needs to be greater than 0"
    if guider:
        assert isinstance(guider, list), "Guider must be a list"
        assert len(guider) == len(multiplier), "Guider length not equal to Multiplier"

    if round_type == 'fuzzy':
        temp = [fuzzy_round(x * i, break_point) for i in multiplier]
    elif round_type == 'ceil':
        temp = [ceil(x * i) for i in multiplier]
    else:
        temp = [floor(x * i) for i in multiplier]
    print(temp)
    if sum(temp) == x:
        return temp

    if guider:
        sorted_idx = np.argsort(guider)[::-1]
    else:
        sorted_idx = np.argsort(multiplier)[::-1]
    print(sorted_idx)
    if sum(temp) < x:
        for i in sorted_idx:
            temp[i] += 1
            if sum(temp) == x:
                return temp
    else:
        sorted_idx = np.argsort(multiplier)[::-1]
        print(sorted_idx)
        for i in sorted_idx:
            temp[i] -= 1
            if sum(temp) == x:
                return temp


if __name__ == '__main__':
    print(fuzzy_round(1.5))
    print(fuzzy_integer_distribution(5, [.2, .3, .5], 'fuzzy', 0.9, [8, 5, 2]))
