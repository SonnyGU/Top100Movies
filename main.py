# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL and store the response
response = requests.get(url=URL)
# Extract the text content from the response
movies_webpage = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(movies_webpage, "html.parser")

# Find all <h3> elements with class 'title' and extract their text,
# resulting in a list of movie titles
movie_list = [title.getText() for title in soup.find_all("h3", class_="title")]

# Reverse the list to start from the bottom
movie_list.reverse()

# Open a file for writing with UTF-8 encoding to handle special characters
with open("movieList", "w", encoding='utf-8') as file:
    # Write each movie title to the file, followed by a newline
    for movie in movie_list:
        file.write(movie + '\n')

# Print the list of movie titles
print(movie_list)
