while True:
    try:
        a = int(input("DIGITE UM NÚMERO: "))
        break 

    except ValueError:
        print("Erro: Você precisa digitar um número inteiro válido!")  

print(f"Você digitou o número {a}.")


