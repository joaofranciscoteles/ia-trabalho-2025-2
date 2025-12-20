from aco import ACO
from clonalg import CLONALG
import matplotlib.pyplot as plt
import os
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    # Default aumentado para garantir convergência em problemas maiores
    parser.add_argument('--iters', type=int, default=300) 
    args = parser.parse_args()

    # Rodar ACO
    print(f">> Executando ACO ({args.iters} iterações)...")
    aco = ACO(n_iters=args.iters)
    best_aco, cost_aco, hist_aco = aco.run()
    print(f"Melhor ACO: {cost_aco:.2f}")

    # Rodar CLONALG
    print(f">> Executando CLONALG ({args.iters} iterações)...")
    clo = CLONALG(n_iters=args.iters)
    best_clo, cost_clo, hist_clo = clo.run()
    print(f"Melhor CLONALG: {cost_clo:.2f}")

    # --- PLOTAGEM MELHORADA ---
    plt.figure(figsize=(12, 7))
    
    # Plotar ACO
    plt.plot(hist_aco, label=f"ACO (Final: {cost_aco:.1f})", linewidth=2)
    
    # Plotar CLONALG
    plt.plot(hist_clo, label=f"CLONALG (Final: {cost_clo:.1f})", linewidth=2, linestyle='--')

    plt.xlabel("Iterações")
    plt.ylabel("Distância (Menor é melhor)")
    plt.title("Comparação de Convergência: Enxame vs Imunes")
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.6)

    # Ajuste fino: Se a diferença inicial for gigantesca, usamos escala logarítmica
    #plt.yscale('log') # Descomente se os valores iniciais forem muito altos

    # Salvar
    save_dir = "../../reports/figs"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, "comparison_part4.png")
    
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"Gráfico salvo em {save_path}")
    plt.show()

if __name__ == "__main__":
    main()