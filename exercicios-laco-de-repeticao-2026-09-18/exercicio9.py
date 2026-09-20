q = int(input("Quantos termos da sequência de Fibonacci? "))
a, b = 0, 1
for _ in range(q):
    print(a)
    a, b = b, a + b
