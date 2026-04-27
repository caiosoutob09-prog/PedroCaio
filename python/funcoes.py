def aumenta(texto):
    return texto.upper()

def soma(a,b):
    a = a +1
    return a + b
    
def faz_traco(texto):
    nome_traco = []
    for letra in texto:
        if(letra != " "):
            nome_traco.append("_ ")
        else:
            nome_traco.append("")
    return nome_traco
        
def faz_traco_bonito(texto):
    nome_traco = ''
    for letra in texto:
        if(letra != " "):
            nome_traco += "_"
        else:
            nome_traco += " "
    return nome_traco
        
#def localiza_letra(lista,letra):
    contador = 1
    localizei = 0 
    for i in lista:
        if(i == letra):
            localizei = localizei + 1 
        contador += 1
    return localizei

def vira_lista(texto):
    lista = []
    for letra in texto:
        lista.append (letra)
    return lista

def troca_traco(lista_tracejada,lista,letra):
    contador = 0 
    for i in lista:
        if(i == letra):
            lista_tracejada[contador] = letra
        contador +=1
    return lista_tracejada

def arrumado_bonito(lista):
    texto = ''
    for i in lista:
        texto += str (i)
    return texto

def palavra(texto):
    texto