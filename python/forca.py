import funcoes as f

final = 10 
palavra = input("\nDigine uma palavra : ")
palavra_arrumada = f .aumenta(palavra)
tracejada_texto = f .faz_traco_bonito(palavra_arrumada)
tracejada_lista = f.faz_traco(palavra_arrumada)
lista = f.vira_lista(palavra_arrumada)
letras_usadas = []

while(final != 0):
    letra = input("\nDigite uma letra: ")
    letra = f.aumenta(letra)
    posicao = (lista, letra)
    print(posicao)
   
    if letra in letras_usadas:
        print("Letra ja foi usada!")
    letras_usadas.append(letra)
    
    
    if posicoes:
        print("ACERTOU!")
    tracejada_lista = f.troca_traco(tracejada_lista, lista, letra)
    print(f.arrumado_bonito(tracejada_lista))
else:
    print("ERRO!")
    final -= 1
        
            