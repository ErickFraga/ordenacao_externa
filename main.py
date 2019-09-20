from math import log, ceil


def escreverFita(fita, x):
"""
    Descrição:
        Essa função registra um valor em uma das fitas

    Retorno:
        Essa função não retorna nada

    Parametros:
        Fita - O path do arquivo aberto
        X - O conteudo a ser escrito
"""
    fita.write(x)       #Essa linha faz o registro do valor contido em X


def abrirFitasLst(lstFitas, modo):

    """
    Descrição:
        Essa função abre os arquivos no path designado

    Retorno:
        Essa função retorna uma lista com os arquivos abertos

    Parametro:
        lstFitas - Variável onde a lista com os paths abertos pra fita será armazenado
        modo - O modo que será utilizado naquela fita write, read, append...
    """

    lst = list()                            # Inicialização da lista na qual sera armazenado os paths das fitas e a variavel que será retornada
    for fita in lstFitas:
        fita = open(fita.name, modo)        # Variável recebe o arquivo aberto
        lst.append(fita)                    # Acrescenta a variável fita (onde o path aberto foi amazenado) dentro da lista

    return lst                              # Retorna a lista com os paths abertos


def trocarfita(bufer):

    """
    Descrição:
        Função booleana para definir a necessidade de trocar a fita utilizada no momento

    Retorno:
        Retorna True caso o Buffer esteja vazio e False caso o Buffer ainda tenha conteudo

    Parametro:
        Buffer - Um array que carrega 3 elementos de uma fita para outra

    """

    for a in bufer:
        if a != ' ' and a != '':        #   Caso o Buffer não esteja vazio...
            return False                #   ...retornar False

    return True                         #   Caso esteja, retonar True


def pagarMenor(lstA):

    """
    Descrição:
        Busca menor elemento da Buffer

    Retorno:
        Retorna o menor elemento da Buffer

    Parametro:
        lstA - O Buffer contendo 3 elementos
    """

    lst = lstA[:]               #   Passa uma copia de lstA para lst
    while ' ' in lst:           #   Enquanto houverem espaços vazios na lista...
        if ' ' in lst:          #   (caso o elemento em que o iterador está seja vazio)
            lst.remove(' ')     #   ...remover ' '

    while '' in lst:            #   Enquanto houverem espaços vazios na lista...
        if '' in lst:           #   (caso o elemento em que o iterador está seja vazio)
            lst.remove('')      #   ...remover ''

    return min(lst)             #   Retorna o menor elemento da lista


def fecharFitasLst(lstFitas):

    """
    Descrição:
        Fecha as fitas que foram abertas em abrirFitasLst()

    Retorno:
        Esta função não retorna nada

    Parametro:
        lstFitas - As fitas que foram o retorno da função abrirFitasLst()

    """

    for fita in lstFitas:
        fita.close()            #   Função que fecha as fitas


def proximaLetra(fita):

        """
        Descrição:
            Le o proximo elemento

        Retorno:
            A função retorna o elemento lido

        Parametros:
            Fita - a fita que será lida
        """

    return fita.read(1)         #   retorno de uma posição da linha do arquivo


def calcularLog(base=1000, tamBuffer=3, num_fitas=3):
    """
    Descrição:
        Calcula o logaritmo da quantidade de passadas a ser realizada pelo algoritmo

    Retorno:
        Retorna o resultado do logaritmo

    Parametro:
        Base - a quantidade de elementos a ser ordenado
        tamBuffer - o tamanho do array que carrega os elementos das fitas
        num_fitas - quantidade de fitas utilizadas nas operações
    """
    return ceil(log(ceil(base / tamBuffer), num_fitas))         #   retorno do log


def baseToFita(base, fitas_primarias):

    """
    Descrição:
        Carrega o Conteudo do arquivo Entrada.txt para as fitas 1, 2 e 3
    Retorno:
        Esta função não retorna nada
    Parametro:
        Base -  O numero de elementos em Entrada.txt
        fitas_primarias - Uma lista com as fitas 1, 2 e 3 abertas
    """

    i = 0                                       #   Contador
    while True:
        bufferA = []                            #   Inicalizando um array
        bufferA.append(proximaLetra(base))      #   Acrescentando a proxima letra a ser lida ao buffer
        proximaLetra(base)
        bufferA.append(proximaLetra(base))
        proximaLetra(base)
        bufferA.append(proximaLetra(base))
        proximaLetra(base)

        if bufferA[0] == '':                    #   Se nenhum elemento for adicionado significa que todos o elementos do arquivo de entrada foram lidos
            print('fim base')
            break                               #   Encerra o loop

        bufferA.sort()                          #   Ordena o Array
        fitas_primarias[i].write(''.join(bufferA) + ' ')

        i = (i + 1) % 3                         #   Definindo o indice como um vetor circular

    print('base carregada')


def fitaToFita(fitasLeitura, fitasEscrita):

    """
    Descrição:
        Transfere os valores de uma fita para outra por meio do buffer
    Retorno:
        Essa função não retorna nada
    Parametro:
        fitasLeitura - Os arquivos a serem lidos
        fitasEscrita - Os arquivos a serem escritos
    """
    bufer = [                                               #   Seta o Buffer com um array e pega um elemento de cada arquivo
        proximaLetra(fitasLeitura[0]),
        proximaLetra(fitasLeitura[1]),
        proximaLetra(fitasLeitura[2])
    ]

    i = 0                                                   #   indice que determina a fita secundaria
    while True:
        print(bufer)

        if bufer[0] == '' and bufer[1] == '' and bufer[2] == '':        #   Caso o buffer esteja vazio, os valores nescessários foram lidos, portanto...
            print(bufer)
            print("todos os valores lidos (fitaToFita)")
            break                                                       #   ...interrompe-se o loop

                                                                        #   pega o menor menor elemento do buffer
        men = pagarMenor(bufer)
        menor = [men, bufer.index(men)]                                 #   Passa o valor do menor elemento e o index de onde o elemento estava armazenado
        print('menor : ', menor)


        print('i1 : ', i)
        escreverFita(fitasEscrita[i], menor[0])                         #   Escreve o menor elemento na fita
        bufer.pop(menor[1])                                             #   Elimina do array o elemento utilizado

        # pegar o proximo numero
        bufer.insert(menor[1], proximaLetra(fitasLeitura[menor[1]]))    #   E repõe com o menor elemento seguinte da mesma fita
        print(bufer)

        if trocarfita(bufer):                                           #   Caso trocar fita seja verdadeiro...
            print('mudar fita!!')
            print(menor[1])
            print('i2 : ', i)
            escreverFita(fitasEscrita[i], ' ')                          #   Escreve um espaço vazio na fita para separar da proxima vez que ela for escrita
            bufer.clear()                                               #   Limpa o Buffer
            bufer = [                                                   #   Buffer é setado novamente
                proximaLetra(fitasLeitura[0]),
                proximaLetra(fitasLeitura[1]),
                proximaLetra(fitasLeitura[2])
            ]
            print(bufer, '-')
            i += 1
            if i == 3:                                                  #   Volta com o indice pra 0 para o manter como um vetor circular
                i = 0



#   Abertuda das fitas

fita_1 = open('fitas/fita_1.txt', 'w')
fita_2 = open('fitas/fita_2.txt', 'w')
fita_3 = open('fitas/fita_3.txt', 'w')

fita_4 = open('fitas/fita_4.txt', 'w')
fita_5 = open('fitas/fita_5.txt', 'w')
fita_6 = open('fitas/fita_6.txt', 'w')

#   Abertura do arquivo de entrada

entrada = open('entrada.txt', 'r')

#   Setando as fitas que serão lidas e as que serão escritas

fitasA = [fita_1, fita_2, fita_3]
fitasB = [fita_4, fita_5, fita_6]

#   Carregando o arquivo de entrada para as fitas

baseToFita(entrada, fitasA)

#   Fechando os arquivos
entrada.close()
fecharFitasLst(fitasB)
fecharFitasLst(fitasA)

# fita para fita


passada = 0                 #   Contador do numero de passadas realizado pelo  algoritmo
base = 1000000              #   Numero de elementos na base de dados
registros = 3               #   Numero de Fitas a serem escritas
numFitas = 3                #   Numero de Fitas a serem lidas
logaritimo = calcularLog(base, registros, numFitas)         #   Variavel que armazena o resultado do logaritmo

while passada <= logaritimo:            #   Verifica se a passada é menor que o resultado do logaritmo
    print('passada : ', passada)

    if passada % 2 == 0:                #   Se o numero da passada for par transfere os valores das fitas 1, 2 e 3 para 4, 5, 6
        fitasA = abrirFitasLst(fitasA, 'r')
        fitasB = abrirFitasLst(fitasB, 'w')
        fitaToFita(fitasA, fitasB)


    else:                               #   Se o numero for impar transdere os valores das fitas 4, 5 e 6 para as fitas 1, 2 e 3
        fitasA = abrirFitasLst(fitasA, 'w')
        fitasB = abrirFitasLst(fitasB, 'r')
        fitaToFita(fitasB, fitasA)

    passada += 1            
    fecharFitasLst(fitasB)
    fecharFitasLst(fitasA)

print('passadas totais : ', passada)