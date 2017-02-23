def parent(i):
    return (i - 1) / 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


class Heap:
    def __init__(self):
        self.A = []
