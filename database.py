from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

# Load database configuration from db_config.json
with open('db_config.json') as config_file:
    config = json.load(config_file)

# Database connection string
db_connection_str = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}"

# Create an engine
engine = create_engine(db_connection_str)

# Create a session factory
SessionFactory = sessionmaker(bind=engine)

# Context manager for database sessions
class DatabaseSession:
    def __enter__(self):
        self.session = SessionFactory()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
