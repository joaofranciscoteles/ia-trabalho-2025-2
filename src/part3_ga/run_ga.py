from ga import GA
from problems.tsp import *
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    ga = GA(
        pop_size=60,
        cx_rate=0.9,
        mut_rate=0.2,
        fitness_fn=fitness,
        create_ind=create_ind,
        crossover=crossover,
        mutate=mutate,
        max_iters=2000
    )
    
    best, score, history = ga.run()
    
    print("Melhor rota:", best)
    print("Distância total:", total_distance(best))
    
    # gráfico opcional
    plt.plot(history)
    plt.xlabel("Geração")
    plt.ylabel("Fitness (negativo da distância)")
    plt.title("Evolução do GA")

    
    pasta="../../reports/figs"
    os.makedirs(pasta,exist_ok=True)

    caminho=os.path.join(pasta,"graficoga.png")

    plt.savefig(caminho,dpi=300,bbox_inches="tight")
    print(f">>Gráfico salvo em:{caminho}")
    plt.show()
