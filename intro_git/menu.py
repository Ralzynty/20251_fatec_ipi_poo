import calculadora
def entradaValores():
    a = int(input("Digite o primeiro número da operação: "))
    b = int(input("Digite o segundo número da operação: "))
    return a, b

def menu():
    while  True:
        print("\nEscolha uma opção:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")