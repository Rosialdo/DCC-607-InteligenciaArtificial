import random
import matplotlib.pyplot as plt

n = 8  # Número de rainhas no problema
p = 500  # Tamanho da população
current_generation = []  # Lista para armazenar a geração atual
new_generation = []  # Lista para armazenar a nova geração

def randomGeneration(NumberOfRows, NumberOfQueens):
    # Gera uma população aleatória inicial com NumberOfRows indivíduos
    lista_geracoes = []
    for i in range(NumberOfRows):
        gene = []
        for j in range(NumberOfQueens):
            gene.append(random.randint(1, n))  # Cada rainha é atribuída a uma coluna aleatória
        gene.append(0)  # Adiciona um espaço para armazenar o número de conflitos
        lista_geracoes.append(gene)
    return lista_geracoes

def fitness(population_list):
    # Avalia a aptidão de cada indivíduo na população
    i = 0
    while i < len(population_list):
        j = 0
        conflict = 0
        while j < n:
            l = j + 1
            while l < n:
                if population_list[i][j] == population_list[i][l]:
                    conflict += 1  # Incrementa o número de conflitos se duas rainhas estiverem na mesma linha
                if abs(j - l) == abs(population_list[i][j] - population_list[i][l]):
                    conflict += 1  # Incrementa o número de conflitos se duas rainhas estiverem na mesma diagonal
                l += 1
            j += 1
        population_list[i][len(population_list[j]) - 1] = conflict  # Armazena o número de conflitos no último índice do indivíduo
        i += 1

    # Ordena a população com base no número de conflitos (menor número de conflitos primeiro)
    for i in range(len(population_list)):
        min = i
        for j in range(i, len(population_list)):
            if population_list[j][n] < population_list[min][n]:
                min = j
        temp = population_list[i]
        population_list[i] = population_list[min]
        population_list[min] = temp
    return population_list

def cross_over(lista_geracoes):
    # Realiza o cruzamento para gerar novos indivíduos
    for i in range(0, len(lista_geracoes), 2):
        z = 0
        new_kid1 = []
        new_kid2 = []
        while z < n:
            if z < n // 2:
                new_kid1.append(lista_geracoes[i][z])
                new_kid2.append(lista_geracoes[i + 1][z])
            else:
                new_kid1.append(lista_geracoes[i + 1][z])
                new_kid2.append(lista_geracoes[i][z])
            z += 1
        new_kid1.append(0)  # Adiciona espaço para armazenar o número de conflitos do novo indivíduo
        new_kid2.append(0)
        lista_geracoes.append(new_kid1)
        lista_geracoes.append(new_kid2)
    return lista_geracoes

def mutation(lista_geracoes):
    # Realiza a mutação em alguns indivíduos da população
    muted_list = []
    i = 0
    while i < p // 2:
        new_rand = random.randint(p // 2, p - 1)
        if new_rand not in muted_list:
            muted_list.append(new_rand)
            lista_geracoes[new_rand][random.randint(0, n - 1)] = random.randint(1, n - 1)  # Altera aleatoriamente a posição de uma rainha em um indivíduo
            i += 1
    return lista_geracoes

def showRes(res):
    # Mostra o resultado do melhor indivíduo encontrado
    l = len(res)
    plt.figure(figsize=(6, 6))
    plt.scatter([x + 1 for x in range(l - 1)], res[:l - 1])  # Plota um gráfico de dispersão das posições das rainhas
    for i in range(l):
        plt.plot([0.5, l - 0.5], [i + 0.5, i + 0.5], color="k")  # Linhas horizontais
        plt.plot([i + 0.5, i + 0.5], [0.5, l - 0.5], color="k")  # Linhas verticais
    plt.show()

# Geração inicial aleatória
current_generation = randomGeneration(p, n)
current_generation = fitness(current_generation)
epoch = 1

while True:
    print("-------------------------------------------------------")
    print("geração ", epoch)
    current_generation = current_generation[0:p//2]  # Mantém apenas os melhores indivíduos da geração atual
    new_generation = cross_over(current_generation)  # Realiza o cruzamento para gerar a nova geração
    new_generation = mutation(new_generation)  # Realiza a mutação na nova geração
    current_generation = new_generation
    current_generation = fitness(current_generation)
    if current_generation[0][n] == 0:  # Se o melhor indivíduo tiver zero conflitos, a solução foi encontrada
        print("Solução sem Conflito: ", current_generation[0])
        showRes(current_generation[0])
        break
    else:
        print("Melhor Solução: ", current_generation[0])
    epoch += 1
