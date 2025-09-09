def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")
    print(f"Idade válida: {idade}")

while True:
    try:
        print("Digite sua idade: ")
        idade = int(input())
        print(validar_idade(idade))
        break
    except ValueError as e:
        print(f"Valor inválido: {e}")
