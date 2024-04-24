import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import datetime

def fetch_movie_titles_by_year(year: str):
    url = f'https://en.wikipedia.org/wiki/{year}_in_film'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    for li in soup.select('.wikitable i'):
        movie_title = li.find_next('a').text
        movies.append(movie_title)
        print(".", end="")
    #print(movies)
    print("\n")
    return movies

def fetch_movie_data(movie_title):
    api_key = '7bfcda51'  # You need to replace this with your actual OMDB API key
    url = f'http://www.omdbapi.com/?s={movie_title}&apikey={api_key}'
    response = requests.get(url)
    return response.json()

def main():
    movie_years = [
        '2020',  
        #'2008',
        #'1999',  
    ]

    movie_data = []
    movie_titles = []
    for year in movie_years:
        movie_titles.extend(fetch_movie_titles_by_year(year))
        for title in movie_titles:
            movie_info = fetch_movie_data(title)
            movie_data.append(movie_info)
    # movie_titles = ['The Matrix', 'The Godfather', 'Star Wars']
    for title in movie_titles:
        movie_info = fetch_movie_data(title)
        movie_data.append(movie_info)
    file_name = ('./kc-python23/01 Homework/webscraper/'  +
                datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') +
                '_movie_data.json'
                )
    with open(file_name, 'w') as json_file:
        json.dump(movie_data, json_file, indent=4)
    print("Movie data: ", movie_data)
    movie_data_details = []
    for dict in movie_data:
        movie_data_details.extend(dict['Search'])
    df = pd.DataFrame(movie_data_details)
    print("\nMovie Data:")
    print(df)

    year_counts = df['Year'].value_counts()
    year_counts_sorted = year_counts.sort_index()
    year_counts_sorted.plot(kind='bar', color='skyblue')
    plt.title('Number of Movies Released Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()    

if __name__ == '__main__':
    main()