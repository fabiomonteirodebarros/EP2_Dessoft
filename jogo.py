from funcoes import *
from dados import dados1
from math import *



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

while i == 0:
    print ('Um país foi escolhido, tente adivinhar!')
    while tentativas > 0:
        print ('Você tem {0} tentativa(s)\n'.format(tentativas))
        chute = input('Qual seu palpite? ')
        chute = chute.lower()
        if chute == 'desisto':
            desistencia = input('Tem certeza que deseja desistir da rodada? [s|n] ')
            if desistencia == 's':
                print ('>>> Que deselegante desistir, o país era: {0}'.format(pais_aleatorio))
                break
            else:
                continue
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
            print('{1} km -> {0}'.format(chute ,d1))

        elif chute == 'dica':
            print('1. Cor da bandeira  - custa 4 tentativas//2. Letra da capital - custa 3 tentativas//3. Área             - custa 6 tentativas//4. População        - custa 5 tentativas//5. Continente       - custa 7 tentativas//0. Sem dica')
            escolha_dica = int(input('Escolha sua opção: [0][1][2][3][4][5] '))

    jogar_dnv = input('Jogar novamente? [s|n] ')
    if jogar_dnv == 'n':
        print ('Até a próxima!')
        break
    else:
        continue