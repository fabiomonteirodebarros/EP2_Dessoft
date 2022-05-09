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

#Adicionando em uma Lista Ordenada

def adiciona_em_ordem (nome, distancia, listas):
    entrada = [nome, distancia]
    resposta = []
    if listas == []:
        resposta.append(entrada)
    for lista in listas:
        if distancia > lista[1]:
            resposta.append(lista)
        elif distancia < lista[1] and entrada not in resposta:
            resposta.append(entrada)
            resposta.append(lista)
        elif distancia < lista[1] and entrada in resposta:
            resposta.append(lista)
    if entrada not in resposta:
        resposta.append(entrada)
    return resposta

#Sorteia Letra com Restrições

import random
def sorteia_letra(palavra, lista):
    especiais= ['.', ',', '-', ';', ' ']
    letras= []
    palavra1= palavra.casefold()
    for letra in palavra1:
        if letra not in lista and letra not in especiais and letra not in letras :
            letras.append (letra)
    if letras != []:
        escolha= random.choice(letras)
    else:
        escolha = ''
    return escolha

#Esta na lista?
def esta_na_lista (pais, lista_paises):
    for lista in lista_paises:
        if lista[0] == pais:
            return True
    return False

#Sorteando Países

import random
def sorteia_pais (dicionario):
    lista_pais = []
    for pais in dicionario.keys():
        lista_pais.append(pais)
    pais_aleatorio = random.choice(lista_pais)
    return pais_aleatorio

#Distância de Haversine

from math import *
def haversine (raio, p1, l1, p2 , l2):
    raiz = (sin(radians((p2-p1)/2))*2) + cos(radians(p1)) * cos(radians(p2)) * (sin(radians((l2-l1)/2))*2)
    raiz2 = raiz**(1/2)
    d = 2 * raio * asin(raiz2)
    return d

print ('oi')
