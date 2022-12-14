#!/usr/bin/env python3
from numba import njit
from person import Person
import time as t
import matplotlib.pyplot as plt
import numpy as np

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	toTest = np.arange(20, 46)
	print(toTest)
	resCpp = np.array([])
	#Time for fib in c++
	for i in toTest:
		f.set(i)
		start = t.perf_counter()
		f.fib()
		end = t.perf_counter()
		resCpp = np.append(resCpp, end - start)
	print(resCpp)
	#Time for fib with Numba
	resNumba = np.array([])
	for i in toTest:
		start = t.perf_counter()
		fib_numba(i)
		end = t.perf_counter()
		resNumba = np.append(resNumba, end - start)
	print(resNumba)
	#Time for fib with python
	resPy = np.array([])
	pyToTest = np.arange(20, 41)
	for i in (pyToTest):
		start = t.perf_counter()
		fib_py(i)
		end = t.perf_counter()
		resPy = np.append(resPy, end - start)
	print(resPy)


	plt.figure(figsize=(5, 2.7), layout='constrained')
	plt.plot(toTest, resNumba, 'ro', toTest, resCpp, 'bo', pyToTest, resPy, 'go')
	plt.legend(['Numba', 'Cpp', 'Py'])
	plt.title('Time to compute Fib')
	plt.xlabel('Fib number')
	plt.ylabel('Time[s]')
	plt.xlim(30, 47)
	plt.savefig('Time to compute Fib')

	plt.figure(figsize=(5, 2.7), layout='constrained')
	plt.plot(toTest - 15, resNumba - 15, 'ro', pyToTest- 10, resPy - 10, 'go')
	plt.legend(['Numba', 'Py'])
	plt.title('Time to compute Fib')
	plt.xlabel('Fib number')
	plt.ylabel('Time[s]')
	plt.xlim(20, 30)
	plt.savefig('Time to compute Fib20')

	print(fib_numba(47))
	f.set(47)
	print(f.fib())
	#Fib47 with cpp gives -1323752223 and with numba 2971215073. Due to memory issues, when it reaches it's limit it's starts from the lowest value and starts adding numbers
	#to that, therefor we get a negative answer. This is called Int overflow.
	#
if __name__ == '__main__':
	main()
