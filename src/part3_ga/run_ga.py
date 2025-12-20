from ga import GA
from problems.tsp import *
import matplotlib.pyplot as plt
import os
import numpy as np

if __name__ == "__main__":
    
    ga = GA(
        pop_size=100,        
        cx_rate=0.9,
        mut_rate=0.1,       
        fitness_fn=fitness,
        create_ind=create_ind,
        crossover=crossover,
        mutate=mutate,
        max_iters=2000
    )
    
    print(">> Executando GA...")
    best, score, history = ga.run()
    
    print(f"Melhor rota encontrada: {best}")
    
    distancia_final = -score
    print(f"Distância total: {distancia_final:.2f}")
    
    
    # Converter histórico de fitness negativo para distância positiva
    history_dist = [-h for h in history]

    plt.figure(figsize=(10, 6))
    plt.plot(history_dist, linewidth=2, label="Melhor Distância")
    
    plt.xlabel("Geração")
    plt.ylabel("Distância Total")
    plt.title("Evolução do Algoritmo Genético (TSP 20 Cidades)")
    
    # Adiciona grade para facilitar leitura
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    
    plt.xlim(0, 200) 

    # Salvar
    pasta = "../../reports/figs"
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "graficoga.png")

    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    print(f">> Gráfico salvo em: {caminho}")
    plt.show()