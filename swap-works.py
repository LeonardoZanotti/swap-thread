#!/usr/bin/env python3

from multiprocessing import Process, Value
from time import sleep


class Thread():
    def __init__(self):
        self.p1MustWait = Value('b', True)
        self.p2MustWait = Value('b', False)
        self.ocupado = Value('b', False)

    def main(self):
        for i in range(2):
            func = Process(target=self.startThread, args=(i,))
            func.start()

    def startThread(self, j):
        for i in range(5):
            if (j == 0):
                while (self.p1MustWait.value):
                    pass
            else:
                while (self.p2MustWait.value):
                    pass

            while (self.ocupado.value):
                pass

            if (j == 0):
                [self.p2MustWait.value, self.ocupado.value] = self.swap(
                    self.p2MustWait.value, self.ocupado.value)
                self.p1MustWait.value = True
            else:
                [self.p1MustWait.value, self.ocupado.value] = self.swap(
                    self.p1MustWait.value, self.ocupado.value)
                self.p2MustWait.value = True

            # critical section
            print('{}° done for thread {}'.format(i + 1, j))

            self.ocupado.value = False

    def swap(self, a, b):
        car = a
        a = b
        b = car
        return [a, b]


if __name__ == '__main__':
    Thread().main()
