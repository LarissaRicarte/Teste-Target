faturamentos = [
    {'UF': 'SP', 'fat': 67836.43},
    {'UF': 'RJ', 'fat': 36678.66},
    {'UF': 'MG', 'fat': 29229.88},
    {'UF': 'ES', 'fat': 27165.48},
    {'UF': 'Outros', 'fat': 19849.53},
]

total = 0

for i in faturamentos:
    total += i['fat']

percents = []

for i in faturamentos:
    percents.append({"UF": i["UF"], 'percent': f"{round((i['fat']/total)*100, 2)}%"})

print(percents)