import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ------------------------
# Carregamento do dataset
# ------------------------
def load_processed():
    base_dir = "../../data/processed"
    train_path = os.path.join(base_dir, "train.csv")
    test_path = os.path.join(base_dir, "test.csv")

    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)

    X_train = df_train.drop(columns=["target"]).values
    y_train = df_train["target"].values

    X_test = df_test.drop(columns=["target"]).values
    y_test = df_test["target"].values

    return X_train, X_test, y_train, y_test


# ------------------------
# Métricas
# ------------------------
def compute_metrics(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average="macro", zero_division=0),
        "recall": recall_score(y_true, y_pred, average="macro", zero_division=0),
        "f1": f1_score(y_true, y_pred, average="macro", zero_division=0)
    }

def print_metrics(metrics_dict):
    print("\n===== MÉTRICAS =====")
    for metric, value in metrics_dict.items():
        print(f"{metric.capitalize()}: {value:.4f}")


def plot_metrics_comparison(knn_metrics, svm_metrics, tree_metrics):
    labels = ["Acurácia", "Precisão", "Recall", "F1"]
    models = ["KNN", "SVM", "Decision Tree"]

    data = np.array([
        [knn_metrics["accuracy"], svm_metrics["accuracy"], tree_metrics["accuracy"]],
        [knn_metrics["precision"], svm_metrics["precision"], tree_metrics["precision"]],
        [knn_metrics["recall"], svm_metrics["recall"], tree_metrics["recall"]],
        [knn_metrics["f1"], svm_metrics["f1"], tree_metrics["f1"]],
    ])

    x = np.arange(len(labels))
    width = 0.25

    plt.style.use("seaborn-v0_8")  # deixa mais bonito

    fig, ax = plt.subplots(figsize=(10,6))

    bars1 = ax.bar(x - width, data[:,0], width, label="KNN")
    bars2 = ax.bar(x,         data[:,1], width, label="SVM")
    bars3 = ax.bar(x + width, data[:,2], width, label="Decision Tree")

    # Títulos e legendas
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel("Valor", fontsize=12)
    ax.set_title("Comparação de Métricas entre Classificadores", fontsize=16, fontweight="bold")
    ax.legend(fontsize=12)

    # Adiciona valores nas barras
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2,
                height + 0.01,
                f"{height:.2f}",
                ha="center",
                va="bottom",
                fontsize=10
            )

    add_labels(bars1)
    add_labels(bars2)
    add_labels(bars3)

    ax.set_ylim(0, 1.15)  # deixa espaço para os números

    plt.tight_layout()

    plt.savefig("../../reports/figs/plot_comparision.png",dpi=300)
    plt.show()

