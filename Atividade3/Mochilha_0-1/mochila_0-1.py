"""
    Nome: Rosialdo Vicente
    N° de matrícula: 2020018122
    Atividade: Atividade 03 - Mochila 0-1
    Disciplina: DCC 607 Inteligência Artificial
"""

from genetic import *

# Definição dos pesos e valores dos itens
pesos_e_valores = [[3, 266],
                   [13, 442],
                   [10, 671],
                   [9, 526],
                   [7, 388],
                   [1, 245],
                   [8, 210],
                   [8, 145],
                   [2, 126],
                   [9, 322]]

peso_maximo = 35
n_de_cromossomos = 80
geracoes = 150
n_de_itens = len(pesos_e_valores)

# Criação da população inicial
populacao = population(n_de_cromossomos, n_de_itens)

# Registro do histórico de fitness
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]

# Evolução da população por um número específico de gerações
for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

# Impressão dos resultados no terminal
for indice, dados in enumerate(historico_de_fitness):
    print("Geração:", indice, "| Média de valor na mochila:", dados)

print("\nPeso máximo:", peso_maximo, "Kg\n\nItens disponíveis:")
for indice, i in enumerate(pesos_e_valores):
    print("Item", indice + 1, ":", i[0], "Kg | R$", i[1])

# Exemplos de boas soluções
print("\nExemplos de boas soluções:")
for i in range(5):
    individuo = populacao[i]
    peso_total, valor_total = 0, 0
    for indice, valor in enumerate(individuo):
        peso_total += (individuo[indice] * pesos_e_valores[indice][0])
        valor_total += (individuo[indice] * pesos_e_valores[indice][1])
    print("Solução", i + 1, ":")
    print("   - Peso:", peso_total, "Kg")
    print("   - Valor: R$", valor_total)

# Gerador de gráfico
from matplotlib import pyplot as plt
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geração")
plt.ylabel("Valor médio da mochila")
plt.show()



"""
    Referência principal: https://github.com/FredericoBender/Algoritmo-Genetico-Problema-da-Mochila/tree/main
"""