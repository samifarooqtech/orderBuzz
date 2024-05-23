import os
from dotenv import load_dotenv  # Import for environment variables

load_dotenv()  # Load environment variables from .env file (optional)
import psycopg2  # for PostgreSQL connection
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:sami123@localhost:5432/mydatabase')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to PostgreSQL database (optional)
    @staticmethod
    def establish_db_connection():
        conn = psycopg2.connect(
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            database=os.getenv("POSTGRES_DB")
        )
        return conn