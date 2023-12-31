import dotenv
import os

dotenv.load_dotenv()

DB_NAME = os.getenv("PGDATABASE")
DB_USER = os.getenv("PGUSER")
DB_PASS = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_PORT = os.getenv("PGPORT")

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

MAX_CONN = int(os.getenv('MAX_CONN', 2))
MIN_CONN = int(os.getenv('MAX_CONN', 1))
