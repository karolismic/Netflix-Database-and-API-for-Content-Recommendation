import pandas as pd
import random

def recommend_movie():
    # Load the dataset of movies
    df_movies = pd.read_csv('normalized_best_movies.csv')
    
    # Filter movies with score greater than 8
    high_score_movies = df_movies[df_movies['SCORE'] > 8]
    
    # If there are no movies with a score greater than 8, return a message
    if high_score_movies.empty:
        return "No high score movies found."
    
    # Randomly select one movie and return its title
    random_movie = high_score_movies.sample(n=1)
    movie_title = random_movie.iloc[0]['TITLE']
    return movie_title

# Example usage:
if __name__ == "__main__":
    print(f"Recommendation of a movie with a high score of more than 8.0: {recommend_movie()}")

