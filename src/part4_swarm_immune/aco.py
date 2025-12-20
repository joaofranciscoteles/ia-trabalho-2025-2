import random
import numpy as np
import matplotlib.pyplot as plt
import os

# Importando o problema definido na parte 3 para garantir comparação justa
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../part3_ga'))
from problems.tsp import N, total_distance, fitness, DIST_MATRIX

class ACO:
    def __init__(self, n_ants=30, n_iters=100, alpha=1.0, beta=2.0, rho=0.1, q=100):
        self.n_ants = n_ants
        self.n_iters = n_iters
        self.alpha = alpha  # Importância do feromônio
        self.beta = beta    # Importância da heurística (visibilidade/distância)
        self.rho = rho      # Taxa de evaporação
        self.q = q          # Intensidade do feromônio
        
        # Inicializa feromônio (pequeno valor constante)
        self.pheromone = np.ones((N, N)) * 0.1
        
        # Heurística (inverso da distância)
        # Adiciona epsilon para evitar divisão por zero
        self.visibility = 1.0 / (np.array(DIST_MATRIX) + 1e-10)

    def run(self):
        best_path = None
        best_cost = float('inf')
        history = []

        for it in range(self.n_iters):
            all_paths = []
            all_costs = []

            # Construção das soluções pelas formigas
            for k in range(self.n_ants):
                path = [random.randint(0, N-1)]
                visited = set(path)

                for _ in range(N-1):
                    curr = path[-1]
                    probs = []
                    unvisited = []

                    # Calcular probabilidades para cidades não visitadas
                    for city in range(N):
                        if city not in visited:
                            tau = self.pheromone[curr][city] ** self.alpha
                            eta = self.visibility[curr][city] ** self.beta
                            probs.append(tau * eta)
                            unvisited.append(city)
                    
                    # Roleta
                    total = sum(probs)
                    probs = [p/total for p in probs]
                    next_city = random.choices(unvisited, weights=probs, k=1)[0]
                    
                    path.append(next_city)
                    visited.add(next_city)
                
                cost = total_distance(path)
                all_paths.append(path)
                all_costs.append(cost)

                if cost < best_cost:
                    best_cost = cost
                    best_path = path[:]

            history.append(best_cost)
            
            # Evaporação
            self.pheromone *= (1 - self.rho)

            # Depósito de feromônio
            for i, path in enumerate(all_paths):
                cost = all_costs[i]
                deposit = self.q / cost
                for j in range(N):
                    u, v = path[j], path[(j+1)%N]
                    self.pheromone[u][v] += deposit
                    self.pheromone[v][u] += deposit # Simétrico

        return best_path, best_cost, history