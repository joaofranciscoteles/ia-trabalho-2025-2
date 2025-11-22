import pandas as pd
from sklearn.model_selection import train_test_split
import os

def main():

    # caminhos
    raw_path = "../../data/raw/cleveland.csv"
    processed_dir = "../../data/processed"

    os.makedirs(processed_dir, exist_ok=True)

    # carregar
    df = pd.read_csv(raw_path, header=None)

    # nomes das colunas
    df.columns = [
        "age","sex","cp","trestbps","chol","fbs","restecg","thalach",
        "exang","oldpeak","slope","ca","thal","target"
    ]

    # trocar ? por NaN
    df = df.replace("?", None)

    # remover linhas inválidas
    df = df.dropna()

    # converter tudo para float
    df = df.astype(float)

    # separar X e y
    X = df.drop(columns=["target"])
    y = df["target"]

    # split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # salvar
    X_train.join(y_train).to_csv(f"{processed_dir}/train.csv", index=False)
    X_test.join(y_test).to_csv(f"{processed_dir}/test.csv", index=False)

    print("Preprocessamento completo.")
    print("Arquivos gerados em data/processed/")

if __name__ == "__main__":
    main()
