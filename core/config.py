import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    RATE_LIMIT = int(os.getenv('AEGIS_RATE_LIMIT', 5))
    TIMEOUT = int(os.getenv('AEGIS_TIMEOUT', 10))
    OUTPUT_DIR = os.getenv('AEGIS_OUTPUT_DIR', './reports')
    USER_AGENT = os.getenv('AEGIS_USER_AGENT', 'Aegis-Scout/1.0 (+https://bugbounty.com/research)')
    DB_PATH = os.getenv('AEGIS_DB_PATH', './db/aegis_audit.db')
