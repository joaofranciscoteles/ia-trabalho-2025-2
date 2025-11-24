import numpy as np
import matplotlib.pyplot as plt
import json
import os

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from utils import load_processed, compute_metrics, print_metrics


def choose_best_svm(X_train, y_train):
    """
    Realiza uma busca simples de hiperparâmetros (Grid Search manual)
    testando vários valores de C, gamma e kernels.
    """

    C_values = [0.1, 1, 10, 100]
    gamma_values = ["scale", "auto"]
    kernels = ["linear", "rbf"]

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    best_score = -1
    best_params = None

    print("\n>> Rodando validação cruzada para SVM...")

    for kernel in kernels:
        for C in C_values:
            for gamma in gamma_values:

                # SVM linear NÃO usa gamma → pular esse caso
                if kernel == "linear" and gamma != "scale":
                    continue

                pipe = make_pipeline(
                    StandardScaler(),
                    SVC(C=C, kernel=kernel, gamma=gamma)
                )

                score = cross_val_score(pipe, X_train, y_train, cv=cv).mean()

                print(f"Kernel={kernel}, C={C}, gamma={gamma} -> Score={score:.4f}")

                if score > best_score:
                    best_score = score
                    best_params = (kernel, C, gamma)

    print("\n>> Melhor combinação encontrada:")
    print(f"Kernel={best_params[0]}, C={best_params[1]}, gamma={best_params[2]}")
    print(f"Acurácia média (CV): {best_score:.4f}\n")

    return best_params


def train_and_evaluate(X_train, X_test, y_train, y_test, best_params):
    """Treina o SVM final e avalia no conjunto de teste."""

    kernel, C, gamma = best_params

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVC(C=C, kernel=kernel, gamma=gamma)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    metrics = compute_metrics(y_test, y_pred)
    print_metrics(metrics)

    return model,metrics


def main():
    print("=== Treinando SVM ===")

    X_train, X_test, y_train, y_test = load_processed()

    # 1. Validar hiperparâmetros
    best_params = choose_best_svm(X_train, y_train)

    # 2. Treinar modelo final
    model,metrics=train_and_evaluate(X_train, X_test, y_train, y_test, best_params)

    print("\nTreino SVM concluído!")

    output_path = os.path.join("../../data","processed","svm_metrics.json")
    os.makedirs(os.path.dirname(output_path),exist_ok=True)

    with open(output_path,"w") as f:
        json.dump(metrics,f,indent=4)
    
    print(f"\nMétricas salvas em: {output_path}")
    




if __name__ == "__main__":
    main()
