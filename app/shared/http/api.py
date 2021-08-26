from os import stat
import requests

from datetime import datetime, timedelta


VALID_METHODS = {
    'POST': requests.post,
    'GET': requests.get,
}


class Api:
    def __init__(self, api_url, user, pwd):
        self.base_url = f'https://{api_url}/api/v3'
        self.__user = user
        self.__pwd = pwd
        self.__token = None
        self.__expires_in = None

    @staticmethod
    def init_app(app):
        api_url = app.config.get('API_URL')
        api_user = app.config.get('API_USER')
        api_pwd = app.config.get('API_PWD')

        app.api = Api(api_url, api_user, api_pwd)
        return app

    @property
    def token(self):
        has_token = self.__token is not None
        is_not_expired = (
            self.__expires_in is not None and
            self.__expires_in < datetime.now()
        )
        if has_token and is_not_expired:
            return self.__token

        payload = {
            'email': self.__user,
            'password': self.__pwd
        }
        response = self.post('/merchant/user/login', payload)
        print(response)
        self.__token = response['token']
        self.__expires_in = datetime.now() + timedelta(minutes=10)
        return self.__token
    

    def post(self, endpoint, data):
        return self.request(
            endpoint,
            method='POST',
            data=data
        )

    def request(self, endpoint, method, data={}):
        url = f'{self.base_url}{endpoint}'
        response = VALID_METHODS[method](url, data=data)
        return response.json()