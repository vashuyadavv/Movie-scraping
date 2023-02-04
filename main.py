from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL )
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)

all_movies = soup.find_all(name="h3", class_="title")
movies_text = [movie.getText() for movie in all_movies]
# print(len(movies_text))
movies = movies_text[::-1]

with open("movies.txt", "w") as movie_file:
    for movie in movies:
        movie_file.write(f"{movie} \n")