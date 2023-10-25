import os
from dotenv import load_dotenv
load_dotenv()

# Database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')