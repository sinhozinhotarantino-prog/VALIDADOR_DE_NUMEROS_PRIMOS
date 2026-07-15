import random
lista_numeros_aleatorios = []

def sorteia(lista_numeros_aleatorios):
    while len(lista_numeros_aleatorios)<5:
        numero_aleatorio = random.randint(1,100)
        if numero_aleatorio not in lista_numeros_aleatorios:
            lista_numeros_aleatorios.append(numero_aleatorio)

sorteia(lista_numeros_aleatorios)
escolhido = random.choice(lista_numeros_aleatorios)

print(f"Números aleatórios gerados: {lista_numeros_aleatorios}")
print(f"Número escolhido aleatoriamente da lista: {escolhido}")

# O programa acima gera uma lista de 5 números aleatórios entre 1 e 100.
# No entanto, ele não garante que os números gerados seja únicos.
lista_numeros_aleatorios.clear()
sorteia(lista_numeros_aleatorios)
print(f"Números aleatórios gerados após a segunda chamada: {lista_numeros_aleatorios}")