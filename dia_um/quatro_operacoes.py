print("Vamos realizar as 4 operações matemáticas! Qual o primeiro número? ")
num1 = float(input())

print("Digite o segundo número:")
num2 = float(input())

print(f"\nSoma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")

if num2 != 0:
    print(f"Divisão: {num1 / num2}")
else:
    print("Divisão: impossível dividir por zero.")
