campo1 = []
campo2 = []

for p in [1, 2]:
    print(f"\nJOGADOR {p}: Agora posicione seus navios!")
    
    
    for n in range(2):
        print(f"Navio {n+1}:")
        lin = int(input("Linha (0-4): "))
        col = int(input("Coluna (0-4): "))
        
        
        if p == 1:
            campo1[lin][col] = 1
        else:
            campo2[lin][col] = 1
            
    # Esse print limpa a tela pro próximo jogador não ver o que você fez
    print("\n" * 50)

