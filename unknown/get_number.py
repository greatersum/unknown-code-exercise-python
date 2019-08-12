def get_number(i):
    if situation_one(i):
        return special_number
    if situation_two(i):
        return 1
    return situation_three(i)


def situation_one(i):
    return i == special_number


def situation_three(i):
    return get_number(i - 1) + get_number(i - (special_number + 2))


def situation_two(i):
    return i == special_number + 1


special_number = 0
