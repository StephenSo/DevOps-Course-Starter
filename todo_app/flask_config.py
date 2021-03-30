import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    KEY = os.environ.get('SECRET_APIKEY')
    TOKEN = os.environ.get('SECRET_APITOKEN')
    BOARD_ID = os.environ.get('BOARD_ID')
    
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")