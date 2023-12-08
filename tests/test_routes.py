import pytest
from backend.app import app as my_loan_app 

@pytest.fixture
def client():
    my_loan_app.config.update({'TESTING': True})
    with my_loan_app.test_client() as client:
        yield client


def test_loan_application(client):
    response = client.post('/api/loan_application', json={
        'businessName': 'Test Business',
        'yearEstablished': '2010',
        'loanAmount': '5000',
        'accountingProviderName': 'XERO'
    })
    assert response.status_code == 200
    assert 'preAssessmentResult' in response.json 

    response = client.post('/api/loan_application', json={})
    assert response.status_code == 400
    
def test_balance_sheet(client):
    response = client.get('/api/balance_sheet?accounting_provider_name=TestProvider')
    assert response.status_code == 200
    assert type(response.json) is list

    response = client.get('/api/balance_sheet')
    assert response.status_code == 400

def test_get_accounting_providers(client):
    response = client.get('/api/accounting_providers')
    assert response.status_code == 200

    assert isinstance(response.json, list)