from funcoes import *
from dados import dados1
from math import *
pref = "\033["
reset = f"{pref}0m"
class cores:
    preto= "30m"
    vermelho= "31m"
    verde= "32m"
    amarelo= "33m"
    azul= "34m"
    magenta= "35m"
    ciano= "36m"
    branco = "37m"
    


print (" ============================ ")
print ("|                            |")
print ("| Bem-vindo ao Insper Países |")
print ("|                            |")
print (" ==== Design de Software ==== ")


print ("\nComandos:")

print ("\ndica        - entra no mercado de dicas ")
print ("desisto     - desiste da rodada ")
print ("inventario  - exibe sua posição \n")


dados=normaliza(dados1)
pais_aleatorio = sorteia_pais(dados)
raio = 6371
chutes = []
tentativas = 20
i = 0
distancias = []
cores_validas = []
lista=[]

while i == 0:
    print ('Um país foi escolhido, tente adivinhar!')
    while tentativas > 0:
        print ('\nVocê tem {0} tentativa(s)\n'.format(tentativas))
        chute = input('Qual seu palpite? ')
        chute = chute.lower()
        if chute == 'desisto':
            desistencia = input('Tem certeza que deseja desistir da rodada? [s|n] ')
            if desistencia == 's':
                print ('>>> Que deselegante desistir, o país era: {0}'.format(pais_aleatorio))
                break
            else:
                continue

        if chute == pais_aleatorio:
            print('*** Parabéns! Você acertou após {0} tentativas!'.format(len(chutes)))

        if chute not in dados:
            print("País desconhecido")
        
        elif chute != pais_aleatorio and chute not in chutes:
            tentativas -= 1
            chutes.append(chute)
            
            p1 = dados[pais_aleatorio]['geo']['latitude']
            l1 = dados[pais_aleatorio]['geo']['longitude']
            
            p2 = dados[chute]['geo']['latitude']
            l2 = dados[chute]['geo']['longitude']

            d = haversine(raio, p1, l1, p2, l2)
            d1 = int(d)
            
            ordem_distancias = adiciona_em_ordem(chute, d1, distancias)
            distancias.append([chute, d1])
            for lista in ordem_distancias:
                print('{1} km -> {0}'.format(lista[0], lista[1]))
            

        if chute == 'dica':
            print('\n1. Cor da bandeira  - custa 4 tentativas\n2. Letra da capital - custa 3 tentativas\n3. Área             - custa 6 tentativas\n4. População        - custa 5 tentativas\n5. Continente       - custa 7 tentativas\n0. Sem dica')
            escolha_dica = int(input('Escolha sua opção: [0][1][2][3][4][5] '))
            if escolha_dica == 0:
                continue
            elif escolha_dica == 1 and tentativas > 4:
                tentativas -= 4
                cores = dados[pais_aleatorio]['bandeira']
                for cor in cores:
                    if cores[cor] > 0:
                        cores_validas.append(cor)
                        if 'outras' in cores_validas:
                            cores_validas.remove('outras')
                cor_sorteada = random.choice(cores_validas)
                cores_validas.remove(cor_sorteada)
                print ('- Cores da bandeira: {0}'.format(cor_sorteada))
            elif escolha_dica == 2 and tentativas > 3:
                tentativas -= 3
                capital = dados[pais_aleatorio]['capital']
                letra_capital=sorteia_letra(capital,lista)
                lista.append(letra_capital)
                print ('- Letras da capital: {0}'.format(', '.join(lista)))

            elif escolha_dica == 3 and tentativas >6:
                tentativas -=6
                area= dados[pais_aleatorio]['area']
                print ('- Área: {0} km2'.format(area))

            elif escolha_dica == 4 and tentativas >5:
                tentativas -=5
                populacao=dados[pais_aleatorio]['populacao']
                print ('- População: {0} habitantes'.format(populacao))
            
            elif escolha_dica == 5 and tentativas >7:
                tentativas -=7
                continente=dados[pais_aleatorio]['continente']
                print ('- Continente: {0} '.format(continente))
            

    if tentativas == 0:
        print ('>>> Você perdeu, o país era: {0}'.format(pais_aleatorio))

    jogar_dnv = input('Jogar novamente? [s|n] ')
    if jogar_dnv == 'n':
        print ('Até a próxima!')
        break
    else:
        continue