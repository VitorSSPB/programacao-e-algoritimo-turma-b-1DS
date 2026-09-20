n = int(input("Quantos elementos da sequência de Fibonacci? "))
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
