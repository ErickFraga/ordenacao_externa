from math import log, ceil

def escreverFita(fita, x):
    fita.write(x)


def abrirFitasLst(lstFitas, modo):
    lst = list()
    for fita in lstFitas:
        fita = open(fita.name, modo)
        lst.append(fita)

    return lst


def trocarfita(bufer):
    for a in bufer:
        if a != ' ' and a != '':
            return False

    return True


def pagarMenor(lstA):
    lst = lstA[:]
    while ' ' in lst:
        if ' ' in lst:
            lst.remove(' ')

    while '' in lst:
        if '' in lst:
            lst.remove('')

    return min(lst)


def fecharFitasLst(lstFitas):
    for fita in lstFitas:
        fita.close()


def proximoNumero(arquivo):
    b = ''
    a = arquivo.read(1)
    if a == '\n' or a == ',' or a == ' ' or a == '':
        a = arquivo.read(1)
    while a.isdigit():
        b += a
        a = arquivo.read(1)
    return b


def proximaLetra(fita):
    return fita.read(1)


def calcularLog(base=1000, tamBuffer=3, num_fitas=3):
    return ceil(log(ceil(base / tamBuffer), num_fitas))


def baseToFita(base, fitas_primarias):
    i = 0
    while True:
        bufferA = []
        bufferA.append(proximaLetra(base))
        proximaLetra(base)
        bufferA.append(proximaLetra(base))
        proximaLetra(base)
        bufferA.append(proximaLetra(base))
        proximaLetra(base)

        if bufferA[0] == '':
            print('fim base')
            break

        bufferA.sort()
        fitas_primarias[i].write(''.join(bufferA) + ' ')

        i = (i + 1) % 3

    print('base carregada')


def fitaToFita(fitasLeitura, fitasEscrita):
    bufer = [
        proximaLetra(fitasLeitura[0]),
        proximaLetra(fitasLeitura[1]),
        proximaLetra(fitasLeitura[2])
    ]

    i = 0  # indece determina a fita secundaria
    while True:
        print(bufer)

        if bufer[0] == '' and bufer[1] == '' and bufer[2] == '':
            print(bufer)
            print("todos os valores lidos (fitaToFita)")
            break

        # pegar o menor
        men = pagarMenor(bufer)
        menor = [men, bufer.index(men)]
        print('menor : ', menor)

        # escrever o menor na fita

        print('i1 : ', i)
        escreverFita(fitasEscrita[i], menor[0])
        bufer.pop(menor[1])

        # pegar o proximo numero
        bufer.insert(menor[1], proximaLetra(fitasLeitura[menor[1]]))
        print(bufer)

        if trocarfita(bufer):
            print('mudar fita!!')
            print(menor[1])
            print('i2 : ', i)
            escreverFita(fitasEscrita[i], ' ')
            bufer.clear()
            bufer = [
                proximaLetra(fitasLeitura[0]),
                proximaLetra(fitasLeitura[1]),
                proximaLetra(fitasLeitura[2])
            ]
            print(bufer, '-')
            i += 1
            if i == 3:
                i = 0


fita_1 = open('fitas/fita_1.txt', 'w')
fita_2 = open('fitas/fita_2.txt', 'w')
fita_3 = open('fitas/fita_3.txt', 'w')

fita_4 = open('fitas/fita_4.txt', 'w')
fita_5 = open('fitas/fita_5.txt', 'w')
fita_6 = open('fitas/fita_6.txt', 'w')

entrada = open('entrada.txt', 'r')

fitasA = [fita_1, fita_2, fita_3]
fitasB = [fita_4, fita_5, fita_6]

baseToFita(entrada, fitasA)

entrada.close()
fecharFitasLst(fitasB)
fecharFitasLst(fitasA)

# fita para fita
"""
fitasA = abrirFitasLst(fitasA, 'r')
fitasB = abrirFitasLst(fitasB, 'w')
fitaToFita(fitasA, fitasB)

fecharFitasLst(fitasB)
fecharFitasLst(fitasA)
"""

passada = 0
base = 1000
registros = 3
numFitas = 3
logaritimo = calcularLog(base, registros, numFitas)

while passada <= logaritimo:
  print('passada : ', passada )

  if passada % 2 == 0:
    fitasA = abrirFitasLst(fitasA, 'r')
    fitasB = abrirFitasLst(fitasB, 'w')
    fitaToFita(fitasA, fitasB)
    

  else:
    fitasA = abrirFitasLst(fitasA, 'w')
    fitasB = abrirFitasLst(fitasB, 'r')
    fitaToFita(fitasB, fitasA)

  passada += 1
  fecharFitasLst(fitasB)
  fecharFitasLst(fitasA)

print('passadas totais : ', passada)
