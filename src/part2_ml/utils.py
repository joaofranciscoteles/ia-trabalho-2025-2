import os
import pandas as pd
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
