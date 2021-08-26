import requests

from datetime import datetime, timedelta


VALID_METHODS = {
    'POST': requests.post,
    'GET': requests.get,
}


class Api:
    base_url = 'https://sandbox-reporting.rpdpymnt.com/api/v3'

    def __init__(self):
        self.__user = 'demo@financialhouse.io'
        self.__pwd = 'cjaiU8CV'
        self.__token = None
        self.__expires_in = None

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