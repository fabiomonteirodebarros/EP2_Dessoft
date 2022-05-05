#Normalizando Base de Países 
def normaliza (dic):
    saida = {}
    for continente in dic:
        tudo = dic[continente]
        for pais in tudo:
            carac = tudo[pais]
            saida[pais] = carac
            saida[pais]['continente'] = continente
    return saida