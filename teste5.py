palavra = input("Digite uma palavra:")

i = len(palavra) - 1

inverso = ""

while i >= 0:
    inverso += palavra[i]
    i = i - 1

print(f"O inverso da palavra: {palavra} é: {inverso}")