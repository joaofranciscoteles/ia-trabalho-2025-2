import random
import copy
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../part3_ga'))
from problems.tsp import N, total_distance, create_ind

class CLONALG:
    def __init__(self, pop_size=50, sel_size=10, clone_factor=5, n_iters=200):
        self.pop_size = pop_size
        self.sel_size = sel_size # Quantos melhores selecionar
        self.clone_factor = clone_factor # Fator beta
        self.n_iters = n_iters
        self.pop = [create_ind() for _ in range(pop_size)]

    def mutate(self, ind, rate):
        # Mutação baseada em trocas (swap)
        # Taxa mais alta = mais trocas
        new_ind = ind[:]
        n_swaps = max(1, int(rate * N)) # Pelo menos 1 troca
        
        for _ in range(n_swaps):
            i, j = random.sample(range(N), 2)
            new_ind[i], new_ind[j] = new_ind[j], new_ind[i]
        
        return new_ind

    def run(self):
        best_overall = None
        best_val = float('inf')
        history = []

        for it in range(self.n_iters):
            # 1. Avaliação (Afinidade = 1/distancia ou negativo da distancia)
            # Aqui queremos MINIMIZAR distância, então ordenamos por menor distancia
            scores = [(total_distance(ind), ind) for ind in self.pop]
            scores.sort(key=lambda x: x[0]) # Menor é melhor

            if scores[0][0] < best_val:
                best_val = scores[0][0]
                best_overall = scores[0][1][:]
            
            history.append(best_val)

            # 2. Seleção
            selected = scores[:self.sel_size]

            # 3. Clonagem e Hipermutação
            clones_pop = []
            for rank, (score, ind) in enumerate(selected):
                # Quanto melhor o rank (menor índice), mais clones
                n_clones = int(self.clone_factor * self.pop_size / (rank + 1))
                
                # Quanto melhor o rank, MENOR a taxa de mutação (preservar)
                mut_rate = (rank + 1) / self.sel_size 

                for _ in range(n_clones):
                    clones_pop.append(self.mutate(ind, mut_rate))

            # 4. Seleção dos clones (adiciona à nova população)
            # Avalia clones
            clone_scores = [(total_distance(c), c) for c in clones_pop]
            clone_scores.sort(key=lambda x: x[0])
            
            # Pega os melhores clones para formar nova população
            # Completa o resto com aleatórios (diversidade - Receptor Editing)
            new_pop = [c for _, c in clone_scores[:self.pop_size - 10]]
            new_pop += [create_ind() for _ in range(10)]
            
            self.pop = new_pop[:self.pop_size]

        return best_overall, best_val, history