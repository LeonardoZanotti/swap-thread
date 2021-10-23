#!/usr/bin/env python3

from multiprocessing import Process
from time import sleep


class Thread():
    def __init__(self):
        self.p1MustWait = True
        self.p2MustWait = False
        self.ocupado = False

    def main(self):
        for i in range(2):
            func = Process(target=self.startThread, args=(i,))
            func.start()

    def startThread(self, j):
        for i in range(5):
            if (j == 0):
                while (self.p1MustWait):
                    sleep(1)
                    self.p1MustWait = self.ocupado
                    pass
            else:
                while (self.p2MustWait):
                    sleep(1)
                    self.p2MustWait = self.ocupado
                    pass

            if (j == 0):
                [self.p2MustWait, self.ocupado] = self.swap(
                    self.p2MustWait, self.ocupado)
                self.p1MustWait = True
            else:
                [self.p1MustWait, self.ocupado] = self.swap(
                    self.p1MustWait, self.ocupado)
                self.p2MustWait = True

            # critical section
            print('{}° done for thread {}'.format(i + 1, j))

            sleep(1)
            self.ocupado = False

    def swap(self, a, b):
        car = a
        a = b
        b = car
        return [a, b]


if __name__ == '__main__':
    Thread().main()
