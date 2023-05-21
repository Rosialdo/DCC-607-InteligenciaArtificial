from genetic import *

                  #[peso,valor]
pesos_e_valores = [[3, 266], 
                   [13, 442], 
                   [10, 671], 
                   [9, 526], 
                   [7, 388], 
                   [1, 245], 
                   [8, 210 ], 
                   [8, 145],
                   [2, 126 ],
                   [9, 322]]
peso_maximo = 35
n_de_cromossomos = 80
geracoes = 150
n_de_itens = len(pesos_e_valores) #Analogo aos pesos e valores


#EXECUCAO DOS PROCEDIMENTOS
populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]
for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

#PRINTS DO TERMINAL
for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de valor na mochila: ", dados)

print("\nPeso máximo:",peso_maximo,"Kg\n\nItens disponíveis:")
for indice,i in enumerate(pesos_e_valores):
    print("Item ",indice+1,": ",i[0]," Kg   | R$",i[1])
    
# Exemplos de boas soluções
print("\nExemplos de boas soluções: ")
for i in range(5):
    individuo = populacao[i]
    peso_total, valor_total = 0, 0
    for indice, valor in enumerate(individuo):
        peso_total += (individuo[indice] * pesos_e_valores[indice][0])
        valor_total += (individuo[indice] * pesos_e_valores[indice][1])
    print("Solução", i + 1, ":")
    print("   - Peso: ", peso_total, "Kg")
    print("   - Valor: R$", valor_total)



#GERADOR DE GRAFICO
from matplotlib import pyplot as plt
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()