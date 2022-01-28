import random


def get_a_random_int(lowest=0, highest=100):
    return random.randint(lowest, highest)


def get_multiple_ints(amount=3, as_str=False, keep_around=None):
    if not keep_around:
        choices = [get_a_random_int() for i in range(amount)]
    else:
        choices = [get_a_random_int(lowest=keep_around - 10, highest=keep_around + 10) for i in range(amount)]
    if as_str:
        return [str(i) for i in choices]
    return choices
