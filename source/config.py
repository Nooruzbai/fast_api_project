from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB_PORT = os.environ.get('POSTGRES_DB_PORT')
POSTGRES_DB_PASSWORD = os.environ.get('POSTGRES_DB_PASSWORD')
POSTGRES_DB_USER_NAME = os.environ.get('POSTGRES_DB_USER_NAME')
POSTGRES_DB_NAME = os.environ.get('POSTGRES_DB_NAME')
POSTGRES_DB_HOST_NAME = os.environ.get('POSTGRES_DB_HOST_NAME')
SECRET_KEY = os.environ.get('SECRET_KEY')


SECRET_AUTH = os.environ.get("SECRET_KEY")
