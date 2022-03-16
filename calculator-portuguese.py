
# program to make a simple calculator

# essas funções irão somar, subtrair, multiplicar e dividir

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Selecione uma operação.")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    # essa função irá receber o input do usuário
    choice = input("Escolha (1/2/3/4): ")

    # essa irá determinar se foi um input válido
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # essa função irá checar se o usuário deseja fazer outro cálculo
        # caso a resposta seja não, irá quebrar o while loop
        next_calculation = input("Vamos fazer mais um cálculo? (sim/nao): ")
        if next_calculation == "nao":
            break

    else:
        print("opção inválida")
