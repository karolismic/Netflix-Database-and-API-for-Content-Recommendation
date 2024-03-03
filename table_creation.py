from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import json

# Load database configuration from db_config.json
with open('db_config.json') as config_file:
    config = json.load(config_file)

# Database connection string
db_connection_str = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}"

# Create an engine
engine = create_engine(db_connection_str)
Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    genre_name = Column(String, nullable=False)

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer)
    score = Column(Float)
    number_of_votes = Column(Integer)
    duration = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    country_id = Column(Integer, ForeignKey('countries.id'))

class TVShow(Base):
    __tablename__ = 'tv_shows'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer)
    score = Column(Float)
    number_of_votes = Column(Integer)
    duration = Column(Integer)
    number_of_seasons = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    country_id = Column(Integer, ForeignKey('countries.id'))

class BestMovieByYear(Base):
    __tablename__ = 'best_movies_by_year'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)  # New column to store the title
    release_year = Column(Integer)  # New column to store the release year
    score = Column(Integer)  # New column to store the score
    genre_id = Column(Integer, ForeignKey('genres.id'))  # Assuming genre_id exists in the 'genres' table
    country_id = Column(Integer, ForeignKey('countries.id'))  # Assuming country_id exists in the 'countries' table

class BestShowByYear(Base):
    __tablename__ = 'best_shows_by_year'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)  # New column to store the title
    release_year = Column(Integer)  # New column to store the release year
    score = Column(Float)  # New column to store the score
    number_of_seasons = Column(Integer)  # New column to store the number of seasons
    genre_id = Column(Integer, ForeignKey('genres.id'))  # Assuming genre_id exists in the 'genres' table
    country_id = Column(Integer, ForeignKey('countries.id'))  # Assuming country_id exists in the 'countries' table

# Create all tables in the database
def create_tables(engine):
    Base.metadata.create_all(engine)
    

if __name__ == '__main__':
    create_tables()