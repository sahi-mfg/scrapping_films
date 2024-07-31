from bs4 import BeautifulSoup as bs  # type: ignore
import requests  # type: ignore
import pandas as pd  # type: ignore


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


def get_a_voir_en_streaming(url: str) -> dict:
    soup = fetch_and_parse(url)
    names = soup.find_all("p", {"class": "sc-e6f263fc-0 sc-ee95228d-1 GItpw gJUtFN"})
    ratings = soup.find_all("div", {"class": "sc-8251ce8c-5 bVyLNx globalRating"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_sorties_de_la_semaine(url: str) -> dict:
    soup = fetch_and_parse(url)
    names = soup.find_all("a", {"class": "sc-e6f263fc-0 sc-ff76fb9e-1 cTWuvs fBqRWl"})
    ratings = soup.find_all("div", {"class": "sc-8251ce8c-5 fTXQip"})
    infos = {name.text: rating.text for name, rating in zip(names, ratings)}
    return infos


def get_critiques(url: str) -> pd.DataFrame:
    pass
