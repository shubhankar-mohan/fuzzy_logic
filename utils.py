import functools
import re

translation_table = {x: None for x in range(128, 256)}


def check_for_none(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        assert args[0], "First String can't be None."
        assert args[1], "First String can't be None."
        return func(*args, **kwargs)
    return decorator


def check_for_empty(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if len(args[0]) == 0 or len(args[1]) == 0:
            return 0
        return func(*args, **kwargs)
    return decorator


def filter_ascii(string):
    return string.translate(translation_table)


def convert_ascii(string):
    return filter_ascii(string.encode('ascii', 'ignore'))


def clean_string(string, force_ascii=False):
    if force_ascii:
        string = filter_ascii(string)

    string = replace_non_aplhanumeric_with_whitespace(string)
    string = string.lower().strip()

    return string


def replace_non_aplhanumeric_with_whitespace(string):
    return re.sub(r"(?ui)\W", " ", string)


def rearrange_string(string):
    words = string.split()
    return " ".join(sorted(words)).strip()
