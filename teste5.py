palavra = input("Digite uma palavra:")

i = len(palavra) - 1

inverso = ""

while i >= 0:
    inverso += palavra[i]
    i = i - 1

print(inverso)