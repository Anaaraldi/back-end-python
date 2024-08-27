import math

# Faça um programa que calcula a Raiz Quadrada de um numero
# Da sequencia de Fibbonacci 
# Use função 

def fib(n):
    fib_1 = 0
    fib_2 = 1

    for i in range(n-1):
        fibonacci = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fibonacci

    print(f"Fibonacci: {fibonacci} - Raiz {math.sqrt(fibonacci)}")

for i in range(3, 10):
    fib(i)

