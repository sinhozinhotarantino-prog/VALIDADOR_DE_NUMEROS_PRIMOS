def escreva(texto):
   s = len(texto)+4
   print("~"*s)
   print(f" {texto}  ")
   print("~"*s)

texto = input("Escreva a frase: ")
escreva(texto)
