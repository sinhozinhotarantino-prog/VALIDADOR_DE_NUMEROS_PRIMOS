def contagem(contador=10000000):
    y=0
    for x in range(1,contador):
        y=y+1
titulo_1 = "CONTAGEM DE 1 ATÉ 10 DE 1 EM 1"
titulo_2 = "CONTAGEM DE 10 ATÉ 0 DE 2 EM 2"
tamanho_1 = (len(titulo_1)//2)+2
tamanho_2 = (len(titulo_2)//2)+2
print(("~-"*tamanho_1))
print(f"  {titulo_1}")
for contador in range (1,11):
    contagem()
    print (f"{contador}", end = " ")
print ("FIM")
print ()
print(("~-"*tamanho_2))
print(f"  {titulo_2}")
for contador_2 in range (10,-1,-2):
    contagem()
    print (f"{contador_2}", end = " ")
print ("FIM")
print ()
