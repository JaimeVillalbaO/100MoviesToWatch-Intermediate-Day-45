import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
page = response.text

soup = BeautifulSoup(page, 'html.parser')
movies_text = soup.select(selector='h3')

movies_list = [movie.getText() for movie in movies_text]
movies_list.reverse()
# print(movies_list)

with open('movies.txt', 'w', encoding='UTF-8') as file:
    for movie in movies_list:
        file.write(f'{movie}\n')
   