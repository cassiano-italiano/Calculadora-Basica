def somar(x, y):
    return x + y
def subtrair(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y
while True:
    print("\n=== Calculadora ===")
    print("Escolha a operação:")
    print("+ - Soma")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")

    operacao = input("Digite a operação: ")

    if operacao not in ['+', '-', '*', '/']:
        print("Opção inválida! Tente novamente.")
        continue  # Volta ao início do loop

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        print("Resultado:", somar(num1, num2))
    elif operacao == '-':
        print("Resultado:", subtrair(num1, num2))
    elif operacao == '*':
        print("Resultado:", multiplicar(num1, num2))
    elif operacao == '/':
        print("Resultado:", dividir(num1, num2))

    while True: 
        continuar = input("\nDeseja fazer outra operação? (s/n): ")
        if continuar.lower() not in ['s', 'sim', 'n', 'nao', 'não']:
            print("\nDesculpe, não entendi.")
            continue
        else:
            break
    if continuar.lower() in ['s', 'sim']:
        continue
    else:
        print("\n Encerrando calculadora, até mais!")
        break