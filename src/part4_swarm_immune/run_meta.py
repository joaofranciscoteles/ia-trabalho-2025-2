from aco import ACO
from clonalg import CLONALG
import matplotlib.pyplot as plt
import numpy as np
import time
import os
import random
import argparse

# Configurações do Experimento
N_RUNS = 30           # Rigor estatístico
ITERS = 1000          # Iterações por rodada

def run_experiment(algo_class, name, n_runs, iters):
    print(f">> Iniciando {n_runs} execuções de {name}...")
    
    results_cost = []
    results_time = []
    all_histories = []

    for i in range(n_runs):
        # Configurar seed para reprodutibilidade
        current_seed = 42 + i
        random.seed(current_seed)
        np.random.seed(current_seed)
        
        start_time = time.time()
        
        # Instancia e roda o algoritmo
        model = algo_class(n_iters=iters)
        best_sol, best_cost, history = model.run()
        
        end_time = time.time()
        
        results_cost.append(best_cost)
        results_time.append(end_time - start_time)
        all_histories.append(history)
        
        # Feedback visual simples
        if (i+1) % 5 == 0:
            print(f"   [{name}] Execução {i+1}/{n_runs} concluída.")

    # Estatísticas
    stats = {
        "best": np.min(results_cost),
        "worst": np.max(results_cost),
        "mean": np.mean(results_cost),
        "std": np.std(results_cost),
        "time_mean": np.mean(results_time)
    }
    
    # Média do histórico para o gráfico
    # Garante que todos tenham o mesmo tamanho
    min_len = min(len(h) for h in all_histories)
    histories_trimmed = [h[:min_len] for h in all_histories]
    mean_history = np.mean(histories_trimmed, axis=0)
    
    return stats, mean_history

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--iters', type=int, default=ITERS)
    parser.add_argument('--seed', type=int, default=42) # Apenas para compatibilidade, seeds variam no loop
    args = parser.parse_args()

    # 1. Rodar ACO
    stats_aco, hist_aco = run_experiment(ACO, "ACO", N_RUNS, args.iters)
    
    # 2. Rodar CLONALG
    stats_clo, hist_clo = run_experiment(CLONALG, "CLONALG", N_RUNS, args.iters)

    # 3. Imprimir Tabela para o Relatório
    print("\n" + "="*60)
    print("=== TABELA COMPARATIVA (Copiar para o LaTeX) ===")
    print(f"{'Métrica':<20} | {'ACO':<15} | {'CLONALG':<15}")
    print("-" * 60)
    print(f"{'Melhor Solução':<20} | {stats_aco['best']:<15.2f} | {stats_clo['best']:<15.2f}")
    print(f"{'Pior Solução':<20} | {stats_aco['worst']:<15.2f} | {stats_clo['worst']:<15.2f}")
    print(f"{'Média':<20} | {stats_aco['mean']:<15.2f} | {stats_clo['mean']:<15.2f}")
    print(f"{'Desvio Padrão':<20} | {stats_aco['std']:<15.2f} | {stats_clo['std']:<15.2f}")
    print(f"{'Tempo Médio (s)':<20} | {stats_aco['time_mean']:<15.4f} | {stats_clo['time_mean']:<15.4f}")
    print("="*60 + "\n")

    # 4. Plotar Gráfico Comparativo
    plt.figure(figsize=(10, 6))
    
    plt.plot(hist_aco, label=f"ACO (Média Final: {stats_aco['mean']:.1f})", linewidth=2)
    plt.plot(hist_clo, label=f"CLONALG (Média Final: {stats_clo['mean']:.1f})", linewidth=2, linestyle='--')

    plt.xlabel("Iterações")
    plt.ylabel("Distância (Menor é melhor)")
    plt.title(f"Comparativo de Convergência (Média de {N_RUNS} execuções)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.xlim(0, 200)

    # Salvar
    pasta = "../../reports/figs"
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "comparison_part4.png")
    
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    print(f">> Gráfico salvo em: {caminho}")
    # plt.show()

if __name__ == "__main__":
    main()