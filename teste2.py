a = 0
b = 1
soma = 0

num = int(input("Digite um número:"))

while soma <= num:
    soma = a + b
    a = b
    b = soma
    
if a == num:
    print(f"O número {num} pertence a sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence a sequência de Fibonacci.")