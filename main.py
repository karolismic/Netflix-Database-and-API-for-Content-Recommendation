import pandas as pd
from sqlalchemy.exc import IntegrityError
from database import DatabaseSession, engine
from table_creation import create_tables, Genre, Country, Movie, TVShow, BestMovieByYear, BestShowByYear
import numpy as np
import logging

# Set up basic logging with a simpler format
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Call the function to create tables
create_tables(engine)
logger.info("Tables have been created successfully.")


def import_csv_data(session, model, csv_file):
    df = pd.read_csv(csv_file)
    try:
        for _, row in df.iterrows():
            # Convert column names to lowercase to match the model's attribute names
            row_dict = {key.lower(): value for key, value in row.to_dict().items()}
            row_dict.pop('index', None)  # Remove the 'index' key if it exists
            
            # Handle NaN values and convert them to None
            for key, value in row_dict.items():
                if pd.isna(value):
                    row_dict[key] = None

            session.add(model(**row_dict))
        
        session.commit()  # Commit once after all rows have been processed
        logger.info(f"Data from {csv_file} has been imported successfully into {model.__tablename__}.")
    except IntegrityError as e:
        session.rollback()  # Rollback the transaction if there's an error
        logger.error(f"IntegrityError: {e.orig.pgerror}")
    except ValueError as e:
        logger.error(f"ValueError: {e}")
    except Exception as e:
        session.rollback()
        logger.error(f"Unexpected error: {e}")

def main():
    # Using the context manager to ensure the session is closed after use
    with DatabaseSession() as session:
        # Import data from CSV files
        import_csv_data(session, Genre, 'normalized_genres.csv')
        import_csv_data(session, Country, 'normalized_countries.csv')
        import_csv_data(session, Movie, 'normalized_best_movies.csv')
        import_csv_data(session, TVShow, 'normalized_best_shows.csv')
        import_csv_data(session, BestMovieByYear, 'normalized_best_movie_by_year.csv')
        import_csv_data(session, BestShowByYear, 'normalized_best_show_by_year.csv')

if __name__ == '__main__':
    main()
