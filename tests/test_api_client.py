import pytest

from ..shared.http.api import Api


def test_api_can_auth():
    api_client = Api()
    assert isinstance(api_client.token, str) == True