def ask(prompt):
    while True:
        a = input(f"{prompt} (sim/não): ").strip().lower()
        if a in {"sim", "s"}:
            return "sim"
        if a in {"nao", "não", "n"}:
            return "nao"
        print("Use 'sim' ou 'não'.")


def main():
    
    q1  = ask("1. Você gosta de adrenalina?")
    if q1 == "sim":
        q10 = ask("10. Prefere ritmo acelerado?")
        if q10 == "sim":
            print("Recomendação: Ação")
        else:
            print("Recomendação: Aventura")
        return


    q2 = ask("2. Gosta de filmes leves e engraçados?")
    if q2 == "sim":
        print("Recomendação: Comédia")
        return

    q4 = ask("4. Gosta de tensão/medo?")
    if q4 == "sim":
        print("Recomendação: Terror")
        return

    q3 = ask("3. Gosta de histórias emocionais e profundas?")
    if q3 == "sim":
        print("Recomendação: Drama")
        return

    q5 = ask("5. Gosta de histórias românticas/afetivas?")
    if q5 == "sim":
        print("Recomendação: Romance")
        return

    q6 = ask("6. A história te leva para fora da realidade comum?")
    if q6 == "sim":
        q8 = ask("8. Aparecem tecnologia/futuro/espaço?")
        if q8 == "sim":
            print("Recomendação: Ficção Científica")
        else:
            print("Recomendação: Fantasia")
        return

    
    q9 = ask("9. Gosta de jornadas/viagens/descobertas?")
    if q9 == "sim":
        print("Recomendação: Aventura")
    else:
        print("Recomendação: Drama")


if __name__ == "__main__":
    main()