
campo1 = []
campo2 = []

for linha in range(5):
    lista1 = []
    lista2 = []
    for coluna in range(5):
        lista1.append(0)
        lista2.append(0)
    campo1.append(lista1)
    campo2.append(lista2)


print("Jogador 1: posicione seus navios no jogo")
for n in range(2): 
    tamanho = int(input("Tamanho do navio (1 ou 2 blocos): "))
    linha = int(input("Linha inicial (0 a 4): "))
    coluna = int(input("Coluna inicial (0 a 4): "))
    direcao = input("Direção h/v (horizontal/vertical): ")
    for i in range(tamanho):
        if direcao == "h":
            campo1[linha][coluna + i] = 1
        else:
            campo1[linha + i][coluna] = 1

print("\n" * 50)

print("Jogador 2: posicione seus navios no jogo")

for n in range(2):
    tamanho = int(input("Tamanho do navio (1 ou 2 blocos): "))
    linha = int(input("Linha inicial (0 a 4): "))
    coluna = int(input("Coluna inicial (0 a 4): "))
    direcao = input("Direção h/v (horizontal/vertical): ")
    for i in range(tamanho):
        if direcao == "h":
            campo2[linha][coluna + i] = 1
        else:
            campo2[linha + i][coluna] = 1

print("\n" * 50)


ganhou = False
vez = 1

while ganhou == False:
    print(f"\nTurno jogador {vez}")
    
    
    
    if vez == 1:
        alvo = campo2
    else:
        alvo = campo1

        

    print("Mapa do adversario (3 = erros 2 = acertos 0 = areas não atingidas):")
    for linha_lista in alvo:
        mapa = []
        for item in linha_lista:
            if item == 2 or item == 3:
                mapa.append(item)
            else:
                mapa.append(0) 
        print(mapa)
    linha_ataque = int(input("Linha do ataque (0 a 4): "))
    coluna_ataque = int(input("Coluna do ataque (0 a 4): "))

    if alvo[linha_ataque][coluna_ataque] == 1:
        print("\nNa mosca! Acertou!")
        alvo[linha_ataque][coluna_ataque] = 2 
    else:
        print("\nIxi péssima! Na água.")
        alvo[linha_ataque][coluna_ataque] = 3

    ainda_tem_navio = False
    for l in range(5):
        if 1 in alvo[l]:
            ainda_tem_navio = True
    
    if ainda_tem_navio == False:
        print(f"\nJogador {vez} foi o vitorioso!")
        ganhou = True 
    else:
       
        if vez == 1:
            vez = 2
        else:
            vez = 1