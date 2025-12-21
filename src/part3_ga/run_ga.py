from ga import GA
from problems.tsp import *
import matplotlib.pyplot as plt
import numpy as np
import time
import os

# Configurações do Experimento
N_RUNS = 30           
POP_SIZE = 100        
CX_RATE = 0.9
MUT_RATE = 0.1        
MAX_ITERS = 2000

if __name__ == "__main__":
    results_dist = []
    results_time = []
    all_histories = []

    print(f">> Iniciando {N_RUNS} execuções do Algoritmo Genético...")
    print("-" * 50)

    for i in range(N_RUNS):
        start_time = time.time()
        
        # Cria a instância do GA com uma seed variável (0, 1, 2... 29)
        # Isso garante que cada execução seja diferente, mas reprodutível se rodar de novo
        ga = GA(
            pop_size=POP_SIZE,
            cx_rate=CX_RATE,
            mut_rate=MUT_RATE,
            fitness_fn=fitness,
            create_ind=create_ind,
            crossover=crossover,
            mutate=mutate,
            max_iters=MAX_ITERS,
            seed=i 
        )
        
        best, score, history = ga.run()
        end_time = time.time()
        
        # O score vem negativo (fitness), convertemos para distância positiva
        dist = -score 
        
        results_dist.append(dist)
        results_time.append(end_time - start_time)
        
        # Converter histórico de fitness negativo para distância positiva para o gráfico
        history_dist = [-h for h in history]
        all_histories.append(history_dist)
        
        print(f"Execução {i+1:02d}/{N_RUNS} | Melhor Distância: {dist:.2f} | Tempo: {end_time - start_time:.4f}s")

    # --- CÁLCULO DAS ESTATÍSTICAS FINAIS ---
    best_overall = np.min(results_dist)
    worst_overall = np.max(results_dist)
    mean_dist = np.mean(results_dist)
    std_dist = np.std(results_dist)
    mean_time = np.mean(results_time)

    print("-" * 50)
    print("=== RELATÓRIO ESTATÍSTICO (Copiar para o LaTeX) ===")
    print(f"Melhor Distância (Mínimo): {best_overall:.2f}")
    print(f"Pior Distância (Máximo): {worst_overall:.2f}")
    print(f"Distância Média Final: {mean_dist:.2f}")
    print(f"Desvio Padrão: {std_dist:.2f}")
    print(f"Tempo Médio de Execução: {mean_time:.4f} s")
    print("-" * 50)

    # --- PLOTAGEM DO GRÁFICO DE CONVERGÊNCIA MÉDIA ---
    # Transforma a lista de listas em uma matriz para calcular a média de cada geração
    all_histories_np = np.array(all_histories)
    mean_history = np.mean(all_histories_np, axis=0)

    plt.figure(figsize=(10, 6))
    
    # Plota a média (linha forte)
    plt.plot(mean_history, linewidth=2, color='blue', label="Distância Média (30 execuções)")
    
    # (Opcional) Plota todas as execuções em cinza claro no fundo para mostrar a variação
    for h in all_histories:
         plt.plot(h, color='gray', alpha=0.1)

    plt.xlabel("Geração")
    plt.ylabel("Distância Total (Menor é melhor)")
    plt.title(f"Convergência Média do GA - TSP 20 Cidades ({N_RUNS} runs)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    plt.xlim(0, 200) 
    
    # Salvar Gráfico
    pasta = "../../reports/figs"
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "graficoga.png")

    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    print(f">> Gráfico salvo com sucesso em: {caminho}")
    # plt.show() # Descomente se quiser ver o gráfico pipocar na tela