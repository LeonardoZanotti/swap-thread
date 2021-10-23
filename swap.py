#!/usr/bin/env python3

from multiprocessing import Process
from time import sleep

p1MustWait = True
p2MustWait = True
ocupado = False

def main():
	for i in range(2):
		func = Process(target=startThread, args=(i,))
		func.start()

def startThread(j):
	global p1MustWait
	global p2MustWait
	global ocupado
	print(j)	

	for i in range(5):
		if (j == 0):
			while (p1MustWait):
				swap(p1MustWait, ocupado)
				print('swap 1 {}'.format(p1MustWait))
			p1MustWait = true
		else:
			while (p2MustWait):
				swap(p2MustWait, ocupado)
				print('swap 2 {}'.format(p2MustWait))
			p2MustWait = true
		print(j)
		ocupado = false
		sleep(1)

def swap(a, b):
	car = a
	a = b
	b = car

main()