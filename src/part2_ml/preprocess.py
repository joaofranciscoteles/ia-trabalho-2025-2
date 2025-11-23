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

    # -----------------------------
    # BINARIZAR O TARGET
    # 0 = saudável
    # 1 = qualquer nível de doença (1 a 4)
    # -----------------------------
    df["target"] = (df["target"] > 0).astype(int)

    # -----------------------------
    # ONE-HOT ENCODING
    # -----------------------------
    categorical_cols = ["cp", "restecg", "slope", "ca", "thal"]

    df = pd.get_dummies(df, columns=categorical_cols)

    # separar X e y
    X = df.drop(columns=["target"])
    y = df["target"]

    # split estratificado
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # salvar arquivos
    X_train.join(y_train).to_csv(f"{processed_dir}/train.csv", index=False)
    X_test.join(y_test).to_csv(f"{processed_dir}/test.csv", index=False)

    print("Preprocessamento completo!")
    print("Arquivos gerados:")
    print("- data/processed/train.csv")
    print("- data/processed/test.csv")

if __name__ == "__main__":
    main()
