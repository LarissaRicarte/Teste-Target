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

print(min(valores))
print(max(valores))

media = sum(valores) / len(valores)

for i in valores:
    if i > media:
        cont = cont + 1

print(cont)