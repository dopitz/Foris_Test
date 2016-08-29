#Programa 2. Retorna el primer numero de Fibonachi que tiene más de 1000 divisores
#Es un tanto lento, hay que mejorar la funcion divisorGenerator


import numpy as np
import math

#Función Fibonacci

def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

#Función Divisores

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

N=np.zeros(100)  #Serie Fibonacci
ND=np.zeros(100) #Numero de divisores

#Generando un arreglo con los numeros de Fibonacci

for i in range (len(N)):
    N[i]=fib(i+1)
#Print N

#Buscando el termino con numero de divisores ND > 1000

for i in range (100):
	ND[i]=len(list(divisorGenerator(N[i])))
	if ND[i] > 1000: 
		print "n= " + str(i+1) + "\n"
		print "Numero Fibonacci= " + str(fib(i+1)) + "\n"
		break

#Respuesta 498454011879264 con 1536.0 divisores





