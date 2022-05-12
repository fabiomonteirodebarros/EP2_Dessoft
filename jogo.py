from funcoes import *
from dados import dados1
from math import *
pref = "\033["
reset = f"{pref}0m"
class colorido:
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
raio = 6371
i = 0


while i == 0:
    print ('Um país foi escolhido, tente adivinhar!')
    pais_aleatorio = sorteia_pais(dados)
    tentativas = 20
    chutes = []
    distancias = []
    lista=[]
    cores_validas = []
    d3 = True
    d4 = True
    d5 = True
    letras_capitais = []
    dicas_oficial = []
    bandeiras = []
    while tentativas > 0:
        opcoes = '0'
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
            print('*** Parabéns! Você acertou após {0} tentativas!'.format(21-tentativas))
            break

        if chute not in dados and chute != 'dica' and chute != 'inventario' :
            print("País desconhecido")
        
        elif chute != pais_aleatorio and chute not in chutes and chute != 'dica' and chute != 'inventario':
            tentativas -= 1
            chutes.append(chute)
            
            p1 = dados[pais_aleatorio]['geo']['latitude']
            l1 = dados[pais_aleatorio]['geo']['longitude']
            
            p2 = dados[chute]['geo']['latitude']
            l2 = dados[chute]['geo']['longitude']

            d = haversine(raio, p1, l1, p2, l2)
            d1 = int(d)
            
            distancias = adiciona_em_ordem(chute, d1, distancias)
            print ('\nDistâncias:')
            for lista in distancias:
                print('{1} km -> {0}'.format(lista[0], lista[1]))
            print('\nDicas:')
            for i in dicas_oficial:
                print (i)
        elif chute in chutes:
            print ('Você já tentou esse país')

        elif chute == 'inventario':
            print ('\nDistâncias:')
            for lista in distancias:
                print('{1} km -> {0}'.format(lista[0], lista[1]))

        if chute == 'dica':
            print('\nMercado de Dicas')
            print('------------------------------------------------------')
            if tentativas > 4:
                print ('1. Cor da bandeira  - custa 4 tentativas')
                opcoes += '|1'
            if tentativas > 3:
                print ('2. Letra da capital - custa 3 tentativas')
                opcoes += '|2'
            if tentativas > 6 and d3 == True:
                print ('3. Área             - custa 6 tentativas')
                opcoes += '|3'
            if tentativas > 5 and d4 == True:
                print ('4. População        - custa 5 tentativas')
                opcoes += '|4'
            if tentativas > 7 and d5 == True:
                print('5. Continente       - custa 7 tentativas')
                opcoes += '|5'
            print('0. Sem dica')
            print('------------------------------------------------------')
            
            escolha_dica = int(input('Escolha sua opção: {0}: '.format(opcoes)))
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
                bandeiras.append(cor_sorteada)
                dica_bandeira = '- Cores da bandeira: '
                for j in bandeiras:
                    dica_bandeira += j + ', '
                if len(bandeiras) < 2:
                    dicas_oficial.append(dica_bandeira)
                    index_band = dicas_oficial.index(dica_bandeira)
                else:
                    dicas_oficial[index_band] = dica_bandeira
                print ('\nDistâncias:')
                for lista in distancias:
                    print('{1} km -> {0}'.format(lista[0], lista[1]))
                print('\nDicas:')
                for i in dicas_oficial:
                    print (i)

            elif escolha_dica == 2 and tentativas > 3:
                tentativas -= 3
                capital = dados[pais_aleatorio]['capital']
                letra_capital = sorteia_letra(capital,lista)
                letras_capitais.append(letra_capital)
                dica_capital = '- Letras da capital: '
                for j in letras_capitais:
                    dica_capital += j + ', '
                if len(letras_capitais) < 2:
                    dicas_oficial.append(dica_capital)
                    index_cap = dicas_oficial.index(dica_capital)
                else:
                    dicas_oficial[index_cap] = dica_capital
                print ('\nDistâncias:')
                for lista in distancias:
                    print('{1} km -> {0}'.format(lista[0], lista[1]))
                print('\nDicas:')
                for i in dicas_oficial:
                    print (i)

            elif escolha_dica == 3 and tentativas >6:
                tentativas -=6
                area = dados[pais_aleatorio]['area']
                d3 = False
                dicas_oficial.append('\n- Área: {0} km2'.format(area))
                print ('\nDistâncias:')
                for lista in distancias:
                    print('{1} km -> {0}'.format(lista[0], lista[1]))
                print('\nDicas:')
                for i in dicas_oficial:
                    print (i)

            elif escolha_dica == 4 and tentativas >5:
                tentativas -=5
                populacao = dados[pais_aleatorio]['populacao']
                d4 = False 
                dicas_oficial.append('\n- População: {0} habitantes'.format(populacao))
                print ('\nDistâncias:')
                for lista in distancias:
                    print('{1} km -> {0}'.format(lista[0], lista[1]))
                print('\nDicas:')
                for i in dicas_oficial:
                    print (i)

            elif escolha_dica == 5 and tentativas >7:
                tentativas -=7
                continente = dados[pais_aleatorio]['continente']
                d5 = False
                dicas_oficial.append('\n- Continente: {0} '.format(continente))
                print ('\nDistâncias:')
                for lista in distancias:
                    print('{1} km -> {0}'.format(lista[0], lista[1]))
                print('\nDicas:')
                for i in dicas_oficial:
                    print (i)
            

    if tentativas == 0:
        print ('>>> Você perdeu, o país era: {0}'.format(pais_aleatorio))

    jogar_dnv = input('Jogar novamente? [s|n] ')
    if jogar_dnv == 'n':
        print ('Até a próxima!')
        break
    else:
        continue