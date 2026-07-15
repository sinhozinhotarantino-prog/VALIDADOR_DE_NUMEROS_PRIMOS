def contagem_progressiva(i, f, p):
    p = abs(p)
    if p == 0:
        p = 1 
    for c in range(i, f + 1, p):
        print(c, end=" ")
    print("FIM !")

def contagem_regressiva(i, f, p):
    p = -abs(p)
    if p == 0:
        p = -1
    for c in range(i, f - 1, p):
         print(c, end=" ")
    print("FIM !")

def verificador(texto_da_pergunta):
    while True:
        try:
            a = int(input(texto_da_pergunta))
            return a 
        except ValueError:
            print("Erro: Você precisa digitar um número inteiro válido!")  

# --- PROGRAMA PRINCIPAL ---

inicio = verificador("INICIO: ")
fim = verificador("FIM: ")

if inicio == fim:
    print("O início e o fim são iguais então não é possível fazer contagem progressiva ou regressiva")
    exit()
else:
    passo = verificador("Passo: ")

    if inicio > fim:
        contagem_regressiva(inicio, fim, passo)

    elif inicio < fim:
        contagem_progressiva(inicio, fim, passo)