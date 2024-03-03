# Netflix Database and API for Content Recommendation

## Project Overview

This project is designed to establish a robust backend system for a new content recommendation team at Netflix. The goal is to set up a relational database management system (RDBMS), normalize datasets for efficient querying, and create APIs that facilitate reading from and writing to the database. This README outlines the project's workflow, from data normalization to API implementation, culminating in a basic recommender system demo.

## Objectives

- Translate business requirements into data engineering tasks.
- Set up and configure a PostgreSQL RDBMS.
- Normalize data tables to ensure database efficiency and integrity.
- Develop Python APIs for seamless database interaction.
- Document the solution comprehensively for future reference and collaboration.

## Data Engineering Workflow

### Step 1: RDBMS Selection and Setup

After evaluating several RDBMS options such as MySQL, SQLite, and PostgreSQL, **PostgreSQL** was chosen for its advanced features, extensive community support, and capability to handle complex queries and large datasets.  Database connection details were stored securely in `db_config.json`.

### Step 2: Data Normalization

- The data is normalized to reduce duplication and enhance data integrity.
- The tables created include `normalized_best_movies_by_year`, `normalized_best_movies`, `normalized_best_show_by_year`,`normalized_best_shows`,`normalized_countries` and`normalized_gen`
- Each table is structured with appropriate primary keys and datatypes.

Data from various CSV files (`Best movies by Year Netflix.csv`, `Best Movies Netflix.csv`, etc.) was analyzed and normalized to reduce redundancy and improve data integrity. The normalization process involved separating distinct entities into dedicated tables and defining relationships among them.

### Step 3: Database Schema Creation

Using SQLAlchemy, a Python ORM, the database schema was defined in `table_creation.py`. This script includes class definitions for each table, which corresponds to the normalized data structures.

### Step 4: API Development

APIs were created in Python to abstract the database interaction, allowing data analysts and scientists to focus on analysis and model building. These APIs, detailed in `database.py` and `csv_importer.py`, provide functions to read and write data, leveraging SQLAlchemy for ORM capabilities.

### Step 5: Data Importation

The `main.py` script was used to import data into the database from the normalized CSV files. This script calls functions from `csv_importer.py` to load data into each table.

### Step 6: Recommender Engine Demo (Bonus)

As an additional feature, a basic recommender engine was developed in `recommender.py` to demonstrate how the APIs can be used to fetch data for content recommendation. This engine uses a simple TF-IDF and cosine similarity approach to suggest similar movies based on a given title.

## Tools and Technologies

- **Python**: The primary programming language used.
- **SQLAlchemy**: ORM library for Python, facilitating the interaction with the PostgreSQL database.
- **PostgreSQL**: Chosen RDBMS for its robustness and wide feature set.
- **pandas**: Utilized for data manipulation and analysis.
- **scikit-learn**: For machine learning components in the recommender system.
- **Logging**: For tracking events and errors during the import process and system operation.

## Setup and Execution

1. Ensure Python is installed on your system.
2. Ensure that PostgreSQL is installed and running on your system.
3. Clone the repository and navigate to the project directory.
4. Install required Python packages: SQLAlchemy, pandas
5. Run the `main.py` script to create the database and tables, and to import the data.
6. Use `recommender.py` to test the recommender engine's functionality.

## Testing

- Unit and integration tests can be written to ensure each part of the codebase functions as expected.
- The recommender engine's accuracy and performance can be evaluated using a separate test dataset or through cross-validation methods.

## Documentation

Throughout the development process, extensive documentation was created to describe each component's purpose and usage. This documentation is crucial for onboarding new team members and serves as a reference for future enhancements.

## Future Enhancements

- Enhance the recommender system with more sophisticated machine learning algorithms.
- Improve API security with authentication and authorization mechanisms.
- Scale the database architecture to accommodate growing datasets and user bases.
- Incorporate automated testing frameworks for continuous integration and deployment.

## Conclusion

This project lays the foundation for a data-driven recommendation system at Netflix. The created database and API infrastructure enable the simulation team to access and store data efficiently, facilitating the development of advanced content recommendation algorithms.

## Author

Karolis Mickus
