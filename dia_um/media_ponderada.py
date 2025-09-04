print("Iremos fazer um cálculo de média ponderada! " + "Qual sua nota 1?")
nota1 = float(input())

print("Agora a segunda: ")
nota2 = float(input())

print("Por fim a terceira e última: ")
nota3 = float(input())

mediaPonderada = (nota1*2 + nota2*5 + nota3*6) / (2+5+6)

print(f"\nA sua média ficou sendo: {round(mediaPonderada, 2)} pontos!")