import os

from dotenv import load_dotenv


load_dotenv()


class DefaultConfig:
    DEBUG = os.getenv('DEBUG', False)
    API_URL = os.getenv('API_URL', None)
    API_USER = os.getenv('API_USER', None)
    API_PWD = os.getenv('API_PWD', None)

    if API_URL is None or API_USER is None or API_PWD is None:
        raise "Invalid config"


class TestConfig(DefaultConfig):
    API_URL = "sandbox-" + os.getenv('API_URL', None)
    TESTING = True
    DEBUG = True
