import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import StratifiedKFold, cross_val_score

from utils import load_processed, compute_metrics, print_metrics


def choose_best_depth(X_train, y_train):
    """
    Escolhe o melhor max_depth para a árvore usando validação cruzada.
    """

    depths = list(range(1, 16))
    scores = []

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    best_score = -1
    best_depth = None

    print("\n>> Rodando validação cruzada para escolher max_depth...")

    for d in depths:
        model = DecisionTreeClassifier(
            max_depth=d,
            criterion="gini",
            random_state=42
        )

        score = cross_val_score(model, X_train, y_train, cv=cv).mean()
        scores.append(score)

        print(f"max_depth={d} -> Score={score:.4f}")

        if score > best_score:
            best_score = score
            best_depth = d

    print(f"\n>> Melhor max_depth encontrado: {best_depth}")
    print(f"Acurácia média (CV): {best_score:.4f}\n")

    return best_depth


def plot_decision_tree(model, feature_names, save_path="tree_plot.png"):
    """
    Plota a árvore completa e salva a imagem.
    """
    plt.figure(figsize=(22, 14))
    plot_tree(
        model,
        feature_names=feature_names,
        filled=True,
        rounded=True,
        fontsize=10
    )
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

    print(f"\nÁrvore de decisão salva em: {save_path}")


def train_and_evaluate(X_train, X_test, y_train, y_test, best_depth, feature_names):
    """
    Treina a árvore com o melhor max_depth e avalia no conjunto de teste.
    """

    model = DecisionTreeClassifier(
        max_depth=best_depth,
        criterion="gini",
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = compute_metrics(y_test, y_pred)
    print_metrics(metrics)

    # --- PLOTAR A ÁRVORE ---
    plot_decision_tree(model, feature_names)

    return model


def main():
    print("=== Treinando Decision Tree ===")

    # 1. Carregar dados processados
    X_train, X_test, y_train, y_test = load_processed()

    # NOMES DAS FEATURES (só pegar do train.csv)
    feature_names = [
        "age","sex","cp","trestbps","chol","fbs","restecg","thalach",
        "exang","oldpeak","slope","ca","thal"
    ]

    # 2. Escolher melhor profundidade
    best_depth = choose_best_depth(X_train, y_train)

    # 3. Treinar e avaliar
    train_and_evaluate(X_train, X_test, y_train, y_test, best_depth, feature_names)

    print("\nTreino da Árvore de Decisão concluído!")


if __name__ == "__main__":
    main()
