import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.KEY = os.environ.get('SECRET_APIKEY')
        self.TOKEN = os.environ.get('SECRET_APITOKEN')
        self.BOARD_NAME = os.environ.get('BOARD_NAME')
        
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        