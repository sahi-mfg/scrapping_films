from films import (
    get_films_du_moment,
    get_a_voir_en_streaming,
    get_sorties_de_la_semaine,
    get_critiques,
)
import pandas as pd  # type: ignore

if __name__ == "__main__":
    # Films
    films_du_moment = get_films_du_moment()
    a_voir_en_streaming = get_a_voir_en_streaming()
    sorties_de_la_semaine = get_sorties_de_la_semaine(
        "https://www.senscritique.com/films"
    )
    films = {**films_du_moment, **a_voir_en_streaming, **sorties_de_la_semaine}
    df1 = pd.DataFrame(films.items(), columns=["Film", "Note"])
    print(df1)
    df1.to_excel("Base_Nom_Prenoms_ISE3_mission1.xlsx", index=False)

    # Critiques
    df2 = get_critiques("https://www.senscritique.com/films")
    print(df2)
    df2.to_excel("Base_Nom_Prenoms_ISE3_mission2.xlsx", index=False)
