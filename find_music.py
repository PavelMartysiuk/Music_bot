import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def check_connect(site_url):
    try:
        response = requests.get(site_url)
    except Exception as exc:
        print(f'Error:{exc}')
    except HTTPError as httperr:
        print(f'Error {httperr}')
    if response.status_code == 404:
        print('Page not found')
    return response.text


def download_music(song):
    SITE = 'https://zaycev.net'
    search_url = 'https://zaycev.net/search.html?query_search='
    song_url = search_url + song
    response = check_connect(song_url)
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        music_href = soup.find('a', class_='musicset-track__download-link track-geo__button').get('href')
        full_music_href = SITE + music_href
        music_in_binary = requests.get(full_music_href).content
        return music_in_binary


if __name__ == '__main__':
    print(download_music())
