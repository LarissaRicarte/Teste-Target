import json

dados = []
cont = 0

with open('dados.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dados = json.loads(conteudo)

valores = []

for i in dados:
    if i['valor'] > 0:
        valores.append(i['valor'])

#o enunciado não informou se os dias sem faturamento deveriam ser tirados do cálculo mínimo

print(f"O faturamento mínimo foi: {min(valores)}")
print(f"O faturamento máximo foi: {max(valores)}")

media = sum(valores) / len(valores)

for i in valores:
    if i > media:
        cont = cont + 1

print(f"O faturamento ultrapassou a média: {round(media, 2)} em {cont} dias.")