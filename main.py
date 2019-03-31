# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

def compose(f, g):
    return lambda *a, **k: g(f(*a, **k))

import csv
import operator
with open('data.csv', encoding="utf8") as documento:
    dados = csv.reader(documento, delimiter=",")
    nacionalidades = []
    clubes = []
    nome20PrimeirosJogadores = []
    idades = {}
    i = 0
    for primeiraLinha in dados:
        break
    for linha in dados:
        if linha[primeiraLinha.index("nationality")] not in nacionalidades:
            nacionalidades.append(linha[primeiraLinha.index("nationality")])
        if linha[primeiraLinha.index("club")] not in clubes:
            clubes.append(linha[primeiraLinha.index("club")])
        if i < 20:
            nome20PrimeirosJogadores.append(linha[primeiraLinha.index("full_name")])
            i += 1
        idade = int(linha[primeiraLinha.index("age")])
        if idade not in idades:
            idades[idade]=1
        else:
            idades[idade]+=1


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    return (len(nacionalidades))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    return (len(clubes))

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    return (nome20PrimeirosJogadores)

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', encoding="utf8") as documento:
        dados = csv.reader(documento, delimiter=",")
        jogadoresGanhamMais = []
        i = 0
        for primeiraLinha in dados:
            break
        sortedlist = sorted(dados, key=compose(operator.itemgetter(primeiraLinha.index("eur_wage")), float), reverse=True)
        for linha in sortedlist:
            if i < 10:
                jogadoresGanhamMais.append(linha[primeiraLinha.index("full_name")])
                i += 1
            else:
                break
    return (jogadoresGanhamMais)

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    import csv
    import operator
    with open('data.csv', encoding="utf8") as documento:
        dados = csv.reader(documento, delimiter=",")
        jogadoresMaisVelhos = []
        i = 0
        for primeiraLinha in dados:
            break
        sortedlist = sorted(dados, key=operator.itemgetter(primeiraLinha.index("age")), reverse=True)
        for linha in sortedlist:
            if i < 10:
                jogadoresMaisVelhos.append(linha[primeiraLinha.index("full_name")])
                i += 1
            else:
                break
    return (jogadoresMaisVelhos)

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    return (idades)
