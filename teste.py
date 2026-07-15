while True:
    # Já limpamos espaços em branco (.strip) e deixamos maiúsculo (.upper) logo na entrada!
    p = input("Sim [S] ou Não [N]: ").strip().upper()
    
    if p == "S":
        print(f"Você digitou {p}. Vou perguntar novamente.")
        # O laço simplesmente recomeça sozinho aqui
        
    elif p == "N":
        print(f"Você digitou {p}. Vou encerrar o programa.")
        break # A porta de saída!
        
    else:
        # Se não for S e não for N (se for 1, enter vazio, batata...), ele cai aqui.
        print("Erro: Você precisa digitar exatamente S ou N!")



            