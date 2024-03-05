n = int(input("Digite um numero: "))

a, b = 0, 1

while a < n:
    a, b = b, a + b

if a == n:
    print("O número informado pertence a sequência")
else:
    print("O número informado não pertence a sequência")