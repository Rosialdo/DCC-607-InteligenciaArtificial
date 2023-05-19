import random
import matplotlib.pyplot as plt


n = 8                          # Número de rainhas
p = 500                        # Numero da população

current_generation = []        # Geração Atual
new_generation = []            # Proxima geração


def randomGeneration(NumberOfRows,NumberOfQueens):
    # Define a função randomGeneration com dois parâmetros: NumberOfRows e NumberOfQueens

    lista_geracoes = []

    for i in range(NumberOfRows):
        # Inicia um loop que itera NumberOfRows vezes para gerar cada indivíduo

        gene = []

        for j in range(NumberOfQueens):
            # Inicia um loop que itera NumberOfQueens vezes para adicionar as posições das rainhas ao indivíduo
            gene.append(random.randint(1,n))

        gene.append(0)
        lista_geracoes.append(gene)

    return lista_geracoes
    # Retorna a lista de indivíduos gerada (população inicial)


def fitness(population_list):
    # Define a função fitness com um parâmetro population_list

    i = 0
    conflict = 0

    while i < len(population_list):
        # Inicia um loop que itera enquanto i for menor que o comprimento da population_list

        j = 0
        conflict = 0

        while j < n:
            # Inicia um loop que itera enquanto j for menor que n (número de rainhas)
            l = j + 1

            while l < n:
                # Inicia um loop que itera enquanto l for menor que n

                if population_list[i][j] == population_list[i][l]:
                    conflict += 1
                    # Incrementa a variável conflict se duas rainhas estiverem na mesma posição (mesma coluna)

                if abs(j - l) == abs(population_list[i][j] - population_list[i][l]):
                    conflict += 1
                    # Incrementa a variável conflict se duas rainhas estiverem na mesma diagonal

                l += 1

            j += 1

        population_list[i][len(population_list[j]) - 1] = conflict
        # Armazena o valor da variável conflict na última posição do indivíduo em population_list

        i += 1

    for i in range(len(population_list)):
        # Inicia um loop que itera pelo comprimento da population_list

        min = i

        for j in range(i, len(population_list)):
            # Inicia um loop que itera a partir do valor de i até o comprimento da population_list

            if population_list[j][n] < population_list[min][n]:
                min = j

        temp = population_list[i]
        population_list[i] = population_list[min]
        population_list[min] = temp
        # Troca a posição dos indivíduos i e min em population_list

    return population_list
    # Retorna a population_list com os indivíduos ordenados pelo valor de fitness


def cross_over(lista_geracoes):
    # Define a função cross_over com um parâmetro lista_geracoes

    for i in range(0, len(lista_geracoes), 2):
        # Inicia um loop que itera de 0 até o comprimento da lista_geracoes, incrementando 2 a cada iteração
        z = 0
        new_kid1 = []
        new_kid2 = []
        # Inicializa as variáveis z, new_kid1 e new_kid2

        while z < n:
            # Inicia um loop que itera enquanto z for menor que n (número de rainhas)

            if z < n // 2:
                new_kid1.append(lista_geracoes[i][z])
                new_kid2.append(lista_geracoes[i + 1][z])
            else:
                new_kid1.append(lista_geracoes[i + 1][z])
                new_kid2.append(lista_geracoes[i][z])
            z += 1
        new_kid1.append(0)
        new_kid2.append(0)
        # Adiciona um valor 0 ao final de new_kid1 e new_kid2

        lista_geracoes.append(new_kid1)
        lista_geracoes.append(new_kid2)
        # Adiciona new_kid1 e new_kid2 à lista_geracoes

    return lista_geracoes
    # Retorna a lista_geracoes com os novos indivíduos gerados pelo crossover



def mutation(lista_geracoes):
    # Define a função mutation com um parâmetro lista_geracoes

    muted_list = []
    # Inicializa uma lista vazia para armazenar os índices já mutados

    i = 0
    while i < p // 2:
        # Inicia um loop que itera enquanto i for menor que p dividido por 2 (p é uma variável não definida)

        new_rand = random.randint(p // 2, p - 1)

        if new_rand not in muted_list:
            # Verifica se new_rand não está na lista muted_list

            muted_list.append(new_rand)
            # Adiciona new_rand à lista muted_list

            lista_geracoes[new_rand][random.randint(0, n - 1)] = random.randint(1, n - 1)
            # Realiza a mutação em um indivíduo selecionado aleatoriamente da lista_geracoes.

            i += 1
    return lista_geracoes
    # Retorna a lista_geracoes após a aplicação das mutações



def showRes(res):

    l = len(res)

    plt.figure(figsize=(6, 6))
    # Cria uma nova figura com o tamanho 6x6 usando a biblioteca matplotlib.pyplot

    plt.scatter([x + 1 for x in range(l - 1)], res[:l - 1])
    # Gera um gráfico de dispersão, onde o eixo x é uma lista de valores de 1 a l - 1

    for i in range(l):
        # Inicia um loop que itera de 0 a l - 1

        plt.plot([0.5, l - 0.5], [i + 0.5, i + 0.5], color="k")
        # Desenha uma linha horizontal no gráfico no nível i + 0.5

        plt.plot([i + 0.5, i + 0.5], [0.5, l - 0.5], color="k")
        # Desenha uma linha vertical no gráfico no nível i + 0.5
    plt.show()
    # Exibe o gráfico na tela


# Chama as funções para começar o programa
current_generation = randomGeneration(p,n)
current_generation = fitness(current_generation)
epoch = 1

# Roda o resultato até que não haja conflito
while True:
    print("-------------------------------------------------------")
    print("geração ",epoch)
    current_generation = current_generation[0:p//2]
    new_generation = cross_over(current_generation)
    new_generation = mutation(new_generation)
    current_generation = new_generation
    current_generation = fitness(current_generation)
    if current_generation[0][n] == 0:
        print("Solution Found: ", current_generation[0])
        showRes(current_generation[0])
        break
    else:
        print("Best Solution: ", current_generation[0])
    epoch+=1