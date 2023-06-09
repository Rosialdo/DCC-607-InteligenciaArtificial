"""
    Nome: Rosialdo Vicente
    N° de matrícula: 2020018122
    Atividade: Atividade 03 - Mochila 0-1
    Disciplina: DCC 607 Inteligência Artificial
"""

from random import getrandbits, randint, random

def individual(n_de_itens):
    # Cria um membro da população representando um indivíduo
    return [getrandbits(1) for x in range(n_de_itens)]

def population(n_de_individuos, n_de_itens):
    # Cria a população inicial
    return [individual(n_de_itens) for x in range(n_de_individuos)]

def fitness(individuo, peso_maximo, pesos_e_valores):
    # Avalia o fitness do indivíduo
    peso_total, valor_total = 0, 0
    for indice, valor in enumerate(individuo):
        peso_total += (individuo[indice] * pesos_e_valores[indice][0])
        valor_total += (individuo[indice] * pesos_e_valores[indice][1])

    if (peso_maximo - peso_total) < 0:
        return -1  # Retorna -1 caso o peso seja excedido
    return valor_total  # Retorna o valor do indivíduo se estiver dentro do peso máximo, sendo maior melhor

def media_fitness(populacao, peso_maximo, pesos_e_valores):
    # Calcula a média do fitness da população, levando em consideração apenas os indivíduos válidos
    summed = sum(fitness(x, peso_maximo, pesos_e_valores) for x in populacao if fitness(x, peso_maximo, pesos_e_valores) >= 0)
    return summed / (len(populacao) * 1.0)

def selecao_roleta(pais):
    # Seleciona um pai e uma mãe baseado nas regras da roleta

    def sortear(fitness_total, indice_a_ignorar=-1):
        # Sorteia um índice baseado nas probabilidades da roleta

        roleta, acumulado, valor_sorteado = [], 0, random()

        if indice_a_ignorar != -1:
            fitness_total -= valores[0][indice_a_ignorar]

        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar == indice:
                continue
            acumulado += i
            roleta.append(acumulado / fitness_total)
            if roleta[-1] >= valor_sorteado:
                return indice

    valores = list(zip(*pais))
    fitness_total = sum(valores[0])

    indice_pai = sortear(fitness_total)
    indice_mae = sortear(fitness_total, indice_pai)

    pai = valores[1][indice_pai]
    mae = valores[1][indice_mae]

    return pai, mae

def evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos, mutate=0.05):
    # Realiza a evolução da população

    # Seleciona e classifica os indivíduos da população
    pais = [[fitness(x, peso_maximo, pesos_e_valores), x] for x in populacao if fitness(x, peso_maximo, pesos_e_valores) >= 0]
    pais.sort(reverse=True)

    # REPRODUÇÃO
    filhos = []
    while len(filhos) < n_de_cromossomos:
        homem, mulher = selecao_roleta(pais)
        meio = len(homem) // 2
        filho = homem[:meio] + mulher[meio:]
        filhos.append(filho)

    # MUTAÇÃO
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo) - 1)
            if individuo[pos_to_mutate] == 1:
                individuo[pos_to_mutate] = 0
            else:
                individuo[pos_to_mutate] = 1

    return filhos


"""
    Referência principal: https://github.com/FredericoBender/Algoritmo-Genetico-Problema-da-Mochila/tree/main
"""