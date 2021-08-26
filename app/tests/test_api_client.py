import pytest

from .. import create_app

report_app = create_app()
api_client = report_app.api


def test_app_has_api_instance():
    assert report_app.api is not None

def test_api_can_auth():
    assert api_client.token is not None


def test_api_get_transaction():
    response = api_client.get_transaction('1035491-1620206531-1307')
    assert '1035491-1620206531-1307' in str(response)

def test_api_list_transactions():
    response = api_client.list_transactions(data={
        'fromDate': '2021-01-01',
        'toDate': '2021-08-01',
        'paymentMethod': 'CREDITCARD'
    })
    assert isinstance(response, dict) == True

def test_api_list_transactions_report_response_has_items():
    response = api_client.list_transactions_report(data={
        'fromDate': '2021-01-01',
        'toDate': '2021-08-01',
        'paymentMethod': 'CREDITCARD'
    })
    assert len(response.get('response', [])) > 0

def test_api_list_transactions_report():
    response = api_client.list_transactions_report(data={
        'fromDate': '2021-01-01',
        'toDate': '2021-08-01',
        'paymentMethod': 'CREDITCARD'
    })
    assert isinstance(response, dict) == True

def test_api_list_transactions_report_status_is_not_declined():
    response = api_client.list_transactions_report(data={
        'fromDate': '2021-01-01',
        'toDate': '2021-08-01',
        'paymentMethod': 'CREDITCARD'
    })
    status =  response.get('status')
    assert status != 'DECLINED'

def test_api_list_transactions_report_response_has_items():
    response = api_client.list_transactions_report(data={
        'fromDate': '2021-01-01',
        'toDate': '2021-08-01',
        'paymentMethod': 'CREDITCARD'
    })
    response =  response.get('response')
    assert len(response) > 0