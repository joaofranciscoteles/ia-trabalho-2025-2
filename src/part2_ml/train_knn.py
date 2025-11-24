import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import json

from utils import load_processed, compute_metrics, print_metrics

def choose_best_k(X_train, y_train):
    """Encontra o melhor valor de K usando validação cruzada."""

    k_values = list(range(1, 31))
    scores = []

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    print("\n>> Rodando validação cruzada para escolher o melhor K...")

    for k in k_values:
        pipe = make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=k)
        )
        score = cross_val_score(pipe, X_train, y_train, cv=cv).mean()
        scores.append(score)

    # --- Gráfico do cotovelo ---
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, scores, marker="o")
    plt.title("Validação Cruzada — KNN (escolha do melhor K)")
    plt.xlabel("K")
    plt.ylabel("Acurácia média (CV)")
    plt.grid(True)
   

    pasta="../../reports/figs"
    os.makedirs(pasta,exist_ok=True)

    caminho=os.path.join(pasta,"escolha_melhor_k_knn.png")

    plt.savefig(caminho,dpi=300,bbox_inches="tight")
    print(f">>Gráfico salvo em:{caminho}")

    plt.show()
    plt.close()

    # Melhor K
    best_k = k_values[int(np.argmax(scores))]
    print(f">> Melhor K: {best_k}\n")

    return best_k


def train_and_evaluate(X_train, X_test, y_train, y_test, best_k):
    """Treina o modelo com o melhor K e avalia no teste."""

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    metrics = compute_metrics(y_test, y_pred)
    print_metrics(metrics)

    return model,metrics


def main():
    print("=== Treinando KNN ===")

    # 1. Carregar dados
    X_train, X_test, y_train, y_test = load_processed()

    # 2. Achar o melhor K
    best_k = choose_best_k(X_train, y_train)

    # 3. Treinar modelo final e avaliar
    model,metrics=train_and_evaluate(X_train, X_test, y_train, y_test, best_k)

    print("\nTreino KNN concluído com sucesso!")

    output_path = os.path.join("../../data","processed","knn_metrics.json")
    os.makedirs(os.path.dirname(output_path),exist_ok=True)

    with open(output_path,"w") as f:
        json.dump(metrics,f,indent=4)
    
    print(f"\nMétricas salvas em: {output_path}")
    


if __name__ == "__main__":
    main()
