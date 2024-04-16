import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def fetch_movie_titles_by_year(year):
    url = f'https://en.wikipedia.org/wiki/{year}_in_film'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    for li in soup.select('.wikitable i'):
        movie_title = li.find_next('a').text
        movies.append(movie_title)
    print(movies)
    return movies

def fetch_movie_data(movie_title):
    api_key = '7bfcda51'  # You need to replace this with your actual OMDB API key
    url = f'http://www.omdbapi.com/?s={movie_title}&apikey={api_key}'
    print(url)
    response = requests.get(url)
    print(response)
    return response.json()

def main():
    movie_years = [
        '1994',  
        #'2007',
        #'2008',
        #'1999',  
    ]

    movie_data = []
    for year in movie_years:
        #movie_titles = fetch_movie_titles_by_year(year)
        movie_titles = ['The Matrix', 'The Godfather', 'Star Wars']
        for title in movie_titles:
            movie_info = fetch_movie_data(title)
            movie_data.append(movie_info)

    # Save the data to a JSON file
    with open('movie_data2.json', 'w') as json_file:
        json.dump(movie_data, json_file, indent=4)

    print("Movie data saved to 'movie_data.json'.")

    # Create a DataFrame
    df = pd.DataFrame(movie_data)
    df2 = pd.DataFrame()
    for search in df['Search']:
        print(f'\n\nSearch: {search}\n\n')
        df2 = pd.concat([df2, pd.DataFrame(search)], ignore_index=True)
        print(f'\n\nDF: {df}\n\n')

    # Display the DataFrame
    print("\nMovie Data:")
    # print(df2)
    
    # Plotting
    # Example: Number of movies per year

    # for search in df['Search']:
    #     df2 = pd.DataFrame(search)
    year_counts = df2['Year'].value_counts()
    year_counts_sorted = year_counts.sort_index()
    year_counts_sorted.plot(kind='bar', color='skyblue')
    plt.title('Number of Movies Released Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

def main():
    year = '1994'  # Example: movies from 1994


if __name__ == "__main__":
    main()
