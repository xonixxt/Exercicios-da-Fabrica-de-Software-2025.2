def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

notas = []

print("Digite as notas de uma em uma. Digite 'sair' para finalizar:")

while True:
    entrada = input()
    if entrada.lower() == "sair":
        break
    if entrada.isdigit():
        notas.append(int(entrada))
    else:
        print("Digite apenas números inteiros.")

media = calcular_media(notas)
print(f"Média: {media:.2f}")
