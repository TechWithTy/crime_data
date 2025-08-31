import os


CRIME_DATA_BASE_URL = os.getenv("CRIME_DATA_BASE_URL", "").rstrip("/")
CRIME_DATA_API_KEY = os.getenv("CRIME_DATA_API_KEY")
CRIME_DATA_TIMEOUT = float(os.getenv("CRIME_DATA_TIMEOUT", "15"))