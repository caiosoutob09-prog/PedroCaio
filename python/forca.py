import funcoes as f

escolha = 10
palavra = input("\nDigite uma palavra: ")
palavra_arrumada = f .aumenta(palavra)
tracejada_texto = f .faz_traco_bonito(palavra_arrumada)
tracejada_lista = f.faz_traco(palavra_arrumada)
lista = f.vira_lista(palavra_arrumada)

while(escolha != 0):
    letra = input("\nDigite uma letra: ")
    letra = f .aumenta(letra)
    posicao = f .localiza_letra(lista,letra)
    print(posicao)
    if(posicao>0):
        print("\nAcertou")
        tracejada_lista = f .troca_traco(tracejada_lista,lista,letra)
        print(f .arrumado_bonito (tracejada_lista))
    else:
        print("\nErrou")







