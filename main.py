from films import (
    get_films_du_moment,
    get_a_voir_en_streaming,
    get_sorties_de_la_semaine,
    get_critiques,
)
import pandas as pd  # type: ignore
import logging


logging.basicConfig(level=logging.INFO)

BASE_URL = "https://www.senscritique.com/films"

def main() -> None:
    films_du_moment = get_films_du_moment(f"{BASE_URL}/toujours-a-l-affiche")
    a_voir_en_streaming = get_a_voir_en_streaming(f"{BASE_URL}/streaming")
    sorties_de_la_semaine = get_sorties_de_la_semaine(f"{BASE_URL}/cette-semaine")
    films = {**films_du_moment, **a_voir_en_streaming, **sorties_de_la_semaine}
    df1 = pd.DataFrame(films.items(), columns=["Film", "Note"])
    logging.info(f'films database: {df1}')
    df1.to_excel("Base_Nom_Prenoms_ISE3_mission1.xlsx", index=False)

    # Critiques
    df2 = get_critiques(BASE_URL)
    logging.info(f'critiques database: {df2}')
    df2.to_excel("Base_Nom_Prenoms_ISE3_mission2.xlsx", index=False)


if __name__ == "__main__":
    main()
   
