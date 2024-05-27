from bs4 import BeautifulSoup as bs  # type: ignore
import requests  # type: ignore
import pandas as pd  # type: ignore
from typing import Dict


def fetch_and_parse(url: str) -> bs:
    request = requests.get(url)
    soup = bs(request.text, "html.parser")
    return soup


def get_films_du_moment(
    url: str,
) -> dict:
    soup = fetch_and_parse(url)
    names = soup.find_all("a", {"class": "sc-e6f263fc-0 sc-ff76fb9e-1 cTWuvs fBqRWl"})
    ratings = soup.find_all("div", {"class": "sc-8251ce8c-5 fTXQip"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_a_voir_en_streaming(url: str) -> Dict[str, str]:
    soup = fetch_and_parse(url)
    names = soup.find_all("p", {"class": "sc-e6f263fc-0 sc-ee95228d-1 GItpw gJUtFN"})
    ratings = soup.find_all("div", {"class": "sc-8251ce8c-5 bVyLNx globalRating"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_sorties_de_la_semaine(url: str) -> Dict[str, str]:
    soup = fetch_and_parse(url)
    names = soup.find_all("a", {"class": "elco-anchor"})
    ratings = soup.find_all("div", {"class": "elco-rating"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_critiques(url: str) -> pd.DataFrame:
    soup = fetch_and_parse(url)
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
