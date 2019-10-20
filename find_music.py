import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def find_mus(song):
    site = 'https://zaycev.net/'
    url = 'https://zaycev.net/search.html?query_search='
    song_url = url + song
    response = requests.get(song_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            main_class = soup.find(class_='musicset-track-list__items')
            child_class = main_class.find(class_="musicset-track__download-link track-geo__button")
            href_music = child_class.get('href')
            full_music_href = site + href_music
        except AttributeError as att:
            print(f'Attribute error{att}')
            return('Error')
        return (full_music_href)
    else:
        return('Error')


def download_music(url, song):
    response = requests.get(url)
    with open(f'music/{song}.mp3', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    print(find_mus('qqvmghjjhg'))
