from bs4 import BeautifulSoup as bs  # type: ignore
import requests  # type: ignore
import pandas as pd  # type: ignore


def get_films_du_moment(
    base_url: str = "https://www.senscritique.com/films",
) -> dict:
    url = base_url + "/toujours-a-l-affiche"
    request = requests.get(url)
    soup = bs(request.text, "html.parser")
    names = soup.find_all("a", {"class": "sc-e6f263fc-0 sc-df6b780a-1 cTWuvs lbhoSA"})

    ratings = soup.find_all("div", {"class": "sc-8251ce8c-5 fTXQip"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_a_voir_en_streaming(
    base_url: str = "https://www.senscritique.com/films",
) -> dict:
    url = base_url + "/streaming"
    request = requests.get(url)
    soup = bs(request.text, "html.parser")
    names = soup.find_all("p", {"class": "sc-e6f263fc-0 sc-ee95228d-1 GItpw gJUtFN"})
    ratings = soup.find_all("div", {"class": "sc-8251ce8c-5 bVyLNx globalRating"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_sorties_de_la_semaine(base_url: str) -> dict:
    url = base_url + "/cette-semaine"
    request = requests.get(url)
    soup = bs(request.text, "html.parser")
    names = soup.find_all("a", {"class": "elco-anchor"})
    ratings = soup.find_all("div", {"class": "elco-rating"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_critiques(base_url: str) -> pd.DataFrame:
    request = requests.get(base_url)
    soup = bs(request.text, "html.parser")
    name_critic = soup.find_all(
        "a", {"class": "sc-e6f263fc-0 sc-b7da4c5c-2 GItpw gvGKDY"}
    )
    likes_critic = soup.find_all(
        "p", {"class": "sc-e6f263fc-0 sc-8d1083e0-1 GItpw XTOao"}
    )
    comments_critic = soup.find_all(
        "p", {"class": "sc-e6f263fc-0 sc-3fcb6f61-1 GItpw djcKen"}
    )
    content_critic = soup.find_all(
        "div", {"class": "sc-8251ce8c-3 gbAIun sc-4db36029-3 iepouY"}
    )
    rating_critic = soup.find_all(
        "div", {"class": "sc-8251ce8c-3 gbAIun sc-4db36029-3 iepouY"}
    )
    photos_critic = soup.find_all("a", {"class": "sc-1a97d7be-3 fZBrFn"})
    date_critic = soup.find_all(
        "p", {"class": "sc-e6f263fc-0 sc-3b5d9ff1-0 GItpw dOiIbg"}
    )
    data = {
        "Dates": [date.text for date in date_critic],
        "Name": [name.text for name in name_critic],
        "Likes": [like.text for like in likes_critic],
        "Comments": [comment.text for comment in comments_critic],
        "Content": [content.text for content in content_critic],
        "Rating": [rating.text for rating in rating_critic],
        "Photos": [photo.text for photo in photos_critic],
    }
    df = pd.DataFrame(data)
    return df
