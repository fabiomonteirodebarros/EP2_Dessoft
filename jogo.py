from funcoes import *
from dados import dados1
from math import *
class bcolors:
    preto= "0\33[0;30m"
    vermelho = "\033[0;31m"
    verde = "\033[0;32m"
    amarelo = "\033[0;33m"
    azul = "\033[0;34m"
    roxo = "\033[0;35m"
    ciano = "\033[0;36m"
    normal= "\033[0m"
    cinza_escuro= "\033[1;30m"
    branco_forte= "\033[1;37m"
    #Cores utilizadas


print (bcolors.branco_forte+" ============================ "+bcolors.normal)
print (bcolors.branco_forte+"|                            |"+bcolors.normal)
print (bcolors.branco_forte+"| Bem-vindo ao Insper Países |"+bcolors.normal)
print (bcolors.branco_forte+"|                            |"+bcolors.normal)
print (bcolors.branco_forte+" ==== Design de Software ==== "+bcolors.normal)


print (bcolors.branco_forte+"\nComandos:"+bcolors.normal)

print (bcolors.ciano+"\ndica        - entra no mercado de dicas "+bcolors.normal)
print (bcolors.cinza_escuro+"desisto     - desiste da rodada "+bcolors.normal)
print (bcolors.roxo+"inventario  - exibe sua posição \n"+bcolors.normal)


dados=normaliza(dados1)#Primeiro nós pegamos toda a lista de países e jogamos no normaliza, para que retornasse um dicionário onde a chave interna era o continente.
raio = 6371
jogar_dnv = 's'



while jogar_dnv == 's': #começamos o while grande com o jogar novamente porque se a resposta for sim ele entra no while novamente
    print ('\nUm país foi escolhido, tente adivinhar!')
    pais_aleatorio = sorteia_pais(dados)#Com os dados já normalizados, chama-se a função sorteia país e assim definisse qual o país escolhido para rodada
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
        if tentativas >15:
            tentativas_colorido= bcolors.verde+str(tentativas)+bcolors.normal
        elif tentativas >10:
            tentativas_colorido= bcolors.ciano+str(tentativas)+bcolors.normal
        elif tentativas > 5:
            tentativas_colorido= bcolors.amarelo+str(tentativas)+bcolors.normal
        else:
            tentativas_colorido=bcolors.vermelho+str(tentativas)+bcolors.normal

        
        opcoes = '0'
        print ('\nVocê tem {0} tentativa(s)\n'.format(tentativas_colorido))
        chute = input('Qual seu palpite? ')
        chute = chute.lower()
        if chute == 'desisto':#Aplicou-se a opção desisto
            desistencia = input('Tem certeza que deseja desistir da rodada? [s|n] ')
            if desistencia == 's':
                print ('>>> Que deselegante desistir, o país era: {0}'.format(pais_aleatorio))
                break
            else:
                continue

        if chute == pais_aleatorio:#Foi colocado o print de ganhou, caso o jogador acerte o país 
            tentativas_colorido = 21-tentativas
            print('*** Parabéns! Você acertou após {0} tentativas!'.format(tentativas_colorido))
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

            d = haversine(raio, p1, l1, p2, l2)#Aqui chama-se a função, distância de haversine, onde conseguimos calcular a distância do chute para o páis escolhido
            d1 = int(d)
            
            distancias = adiciona_em_ordem(chute, d1, distancias)# Função adiciona em odrem, para que as funções fiquem fiquem todas organizadas da menor para maior nos chutes
            print ('\nDistâncias:')
            for lista in distancias:
                if lista[1] <= 1000:
                    print(bcolors.verde+'{1} km -> {0}'.format(lista[0], lista[1])+ bcolors.normal)
                if lista[1] >1000 and lista[1]<=2000:
                    print(bcolors.ciano+'{1} km -> {0}'.format(lista[0], lista[1])+ bcolors.normal)
                if lista[1]> 2000 and lista[1]<=5000:
                    print(bcolors.amarelo+'{1} km -> {0}'.format(lista[0], lista[1])+ bcolors.normal)
                if lista[1]> 5000 and lista[1]<=10000:
                    print(bcolors.vermelho+'{1} km -> {0}'.format(lista[0], lista[1])+ bcolors.normal)
                if lista[1]> 10000:
                    print(bcolors.cinza_escuro+'{1} km -> {0}'.format(lista[0], lista[1])+ bcolors.normal)
            print('\nDicas:')
            for i in dicas_oficial:
                print (i)
        elif chute in chutes:
            print ('Você já tentou esse país')

        elif chute == 'inventario':#Inventário, onde o jogador vê sua posição na rodada
            print ('\nDistâncias:')
            for lista in distancias:
                print('{1} km -> {0}'.format(lista[0], lista[1]))
            print('\nDicas:')
            for i in dicas_oficial:
                print (i)

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
            
            elif escolha_dica == 1 and tentativas > 4:#Caso o jogador escolha a dica 1, será sorteada uma cor da bandeira que seja maior que zero, nos dados e diferente de outras
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

            elif escolha_dica == 2 and tentativas > 3:#Se o jogador escolher letra da capital, será sorteada uma letra da capital atráves da função sorteia_letra
                tentativas -= 3
                capital = dados[pais_aleatorio]['capital']
                letra_capital = sorteia_letra(capital,lista)#chama-se a função 
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

            elif escolha_dica == 3 and tentativas >6:#Se o jogador escolher a dica 3, ele receberá a área do país escolhido
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

            elif escolha_dica == 4 and tentativas >5:#Se o jogador escolher a dica 4, ele receberá a população do país escolhido
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

            elif escolha_dica == 5 and tentativas >7:#Se o jogador escolher a dica 5, ele receberá o continente do país escolhido
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
        chute = ''
        print ('Até a próxima!')
        break