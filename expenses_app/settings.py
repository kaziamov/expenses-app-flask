import dotenv
import os
# from urllib.parse import urlparse


dotenv.load_dotenv()

DB_NAME = os.getenv("PG_DATABASE", "postgres")
DB_USER = os.getenv("PG_USER", "postgres")
DB_PASS = os.getenv("PG_PASSWORD", "postgres")
DB_HOST = str(os.getenv("PG_HOST", "0.0.0.0"))
DB_PORT = int(os.getenv("PG_PORT", 5432))

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

MAX_CONN = os.getenv('MAX_CONN', 2)
MIN_CONN = os.getenv('MAX_CONN', 1)
