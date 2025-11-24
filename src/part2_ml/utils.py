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

    fig, ax = plt.subplots(figsize=(8,5))
    
    ax.bar(x - width, data[:,0], width, label="KNN")
    ax.bar(x,         data[:,1], width, label="SVM")
    ax.bar(x + width, data[:,2], width, label="Decision Tree")

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_title("Comparação de Métricas - KNN vs SVM vs Decision Tree")

    plt.tight_layout()
    plt.show()
