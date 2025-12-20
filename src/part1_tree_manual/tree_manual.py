def ask(prompt):
    while True:
        a = input(f"{prompt} (sim/não): ").strip().lower()
        if a in {"sim", "s"}:
            return "sim"
        if a in {"nao", "não", "n"}:
            return "nao"
        print("Use 'sim' ou 'não'.")


def main():
    print("=== Sistema de Recomendação de Filmes ===")
    
    # PERGUNTA 1
    q1 = ask("1. Você gosta de adrenalina?")
    
    if q1 == "sim":
        
        
        # PERGUNTA 2
        q2 = ask("2. O objetivo principal é sentir medo/susto?")
        if q2 == "sim":
            print("Recomendação: Terror")
            return

        # PERGUNTA 3
        q3 = ask("3. Você gosta de tiroteios, explosões e perseguições?")
        if q3 == "sim":
            print("Recomendação: Ação")
            return

        # PERGUNTA 4
        q4 = ask("4. Prefere resolver mistérios e crimes?")
        if q4 == "sim":
            print("Recomendação: Suspense / Policial")
            return

        # PERGUNTA 5
        q5 = ask("5. A história envolve futuro, espaço ou tecnologia avançada?")
        if q5 == "sim":
            print("Recomendação: Ficção Científica")
        else:
            print("Recomendação: Aventura") 
            
    else:
        

        # PERGUNTA 6
        q6 = ask("6. O principal objetivo é dar risada?")
        if q6 == "sim":
            print("Recomendação: Comédia")
            return

        # PERGUNTA 7
        q7 = ask("7. Você quer se emocionar ou chorar?")
        if q7 == "sim":
            print("Recomendação: Drama")
            return

        # PERGUNTA 8
        q8 = ask("8. Busca algo focado em romance/casais?")
        if q8 == "sim":
            
            q9 = ask("9. Prefere finais felizes e leves (clichês)?")
            if q9 == "sim":
                print("Recomendação: Comédia Romântica")
            else:
                print("Recomendação: Romance Dramático")
            return

        # PERGUNTA 10
        q10 = ask("10. Gosta de magia, dragões ou mundos irreais?")
        if q10 == "sim":
            print("Recomendação: Fantasia")
        else:
            print("Recomendação: Documentário / Biografia")


if __name__ == "__main__":
    main()