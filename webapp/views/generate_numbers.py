from random import shuffle


def generate_numbers(n):
    data = list(range(1, 10))
    shuffle(data)
    return data[:4]