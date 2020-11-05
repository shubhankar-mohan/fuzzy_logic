import numpy as np
from math import floor, ceil
from warnings import warn


def fuzzy_round(x: float, break_point=0.5) -> int:
    """
    Performs a Rounding off an an float to an integer, based on decimal part.
    Args:
        x: float value which needs to be rounded
        break_point: (Default: 0.5) threshold for deciding if ceil or floor needs to be returned

    Returns: ceil(x) if x-int(x) >= break_point else floor(x)
    """
    decimal_part = x - int(x)

    if decimal_part >= break_point:
        return ceil(x)
    else:
        return floor(x)


def fuzzy_integer_distribution(x: int, multiplier: list, round_type='fuzzy', break_point=0.8, guider_type='multiplier', guider=None):
    """
    The function divides a given integer into different percentages which are integer.
    Args:
        x: Integer which needs to be divided
        multiplier: Percentages in which integer needs to be divided
        round_type: (Default: fuzzy) ['floor', 'ceil', 'fuzzy'], Primary Round Type to be used while getting
                    base distribution.
        break_point: (Default: 0.8) It is needed if round_type is fuzzy. See fuzzy_round for details.
        guider_type: (Default: multiplier) ['multiplier', 'deficit_decimal', 'guider'] It defines how the left out
                      value after Primary Round off needs to be distributed. Multiplier used multiplier argument to
                      distribute, giving preference to highest. deficit_decimal uses decimal_part left after floor,
                      giving preference to highest. guider uses a given distribution for the same.
        guider: Needs is guider_type is guider. It is used to give preference to allocate left out
                      value after Primary Round off.

    Returns: A list of integer values, which are closest representation of percentage distribution of x according
            to multiplier.
    """
    assert isinstance(x, int), "Number must be integers."
    assert isinstance(multiplier, list), "Multiplier must be a list"
    assert sum(multiplier) <= 1.0, "Distribution multiplier sum can't be more than 1"
    assert round_type in ['floor', 'ceil', 'fuzzy'], "Mode can only take values ceil, floor and fuzzy"
    assert guider_type in ['multiplier', 'deficit_decimal', 'guider'], "Guider Type can only take values multiplier, " \
                                                                       "deficit_decimal and guider "
    assert break_point < 1, "Fuzzy Break Point needs to be less than 1"
    assert break_point > 0, "Fuzzy Break Point needs to be greater than 0"

    if guider:
        assert isinstance(guider, list), "Guider must be a list"
        assert len(guider) == len(multiplier), "Guider length not equal to Multiplier"

    if guider_type == 'guider':
        assert guider is not None, "Guider Required."
    else:
        if guider:
            warn("Setting guider_type to 'guider'")
            guider_type = 'guider'

    if guider_type == 'deficit_decimal':
        if round_type != 'floor':
            warn("Setting round_type to floor.")
            round_type = 'floor'

    if round_type == 'fuzzy':
        temp = [fuzzy_round(x * i, break_point) for i in multiplier]
    elif round_type == 'ceil':
        temp = [ceil(x * i) for i in multiplier]
    else:
        temp = [floor(x * i) for i in multiplier]

    if sum(temp) == x:
        return temp

    if guider_type == 'guider':
        sorted_idx = np.argsort(guider)[::-1]
    elif guider_type == 'deficit_decimal':
        sorted_idx = np.argsort([x * i - floor(x * i) for i in multiplier])[::-1]
    else:
        sorted_idx = np.argsort(multiplier)[::-1]

    if sum(temp) < x:
        for i in sorted_idx:
            temp[i] += 1
            if sum(temp) == x:
                return temp
    else:
        sorted_idx = np.argsort(multiplier)[::-1]
        for i in sorted_idx:
            temp[i] -= 1
            if sum(temp) == x:
                return temp
