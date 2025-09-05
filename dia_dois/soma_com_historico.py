print("Vamos realizar uma operação de soma entre dois números e armazenar o histórico! Para iniciar digite 'i'.")

def soma(num1, num2):
    return num1 + num2

historico = []

while True:
    print("Digite 'i' para iniciar ou 'e' para encerrar: ")
    opcao = input().lower()

    if opcao == 'i':
        while True:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            resultado = soma(num1, num2)
            historico.append(resultado)
            print(f"Resultado da soma = {resultado}")

            while True:
                print("Deseja executar outra operação? (s/n) ")
                opcao2 = input().lower()
                if opcao2 == 's':
                    break
                elif opcao2 == 'n':
                    print("Histórico de somas:", historico)
                    break
                else:
                    print("Ou 's' para Sim ou 'n' para Não.")

            if opcao2 == 'n':
                break

    elif opcao == 'e':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite 'i' para iniciar ou 'e' para encerrar.")
