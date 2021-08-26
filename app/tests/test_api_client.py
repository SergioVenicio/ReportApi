import pytest

from .. import create_app

report_app = create_app()

def test_app_has_api_instance():
    assert report_app.api is not None

def test_api_can_auth():
    api_client = report_app.api
    assert isinstance(api_client.token, str) == True