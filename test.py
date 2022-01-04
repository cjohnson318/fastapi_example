import requests

BASE_URL = 'http://localhost:8000'

def test_health():
    resp = requests.get(BASE_URL + '/health')    
    assert resp.json() == {'health': 'alive'}

def test_create():
    resp = requests.post(BASE_URL + '/author/create', json={'name': 'Bill'})
    assert resp.status_code == 200

def test_list():
    resp = requests.get(BASE_URL + '/author/list')
    assert len(resp.json()) > 0
    
def test_detail():
    resp = requests.get(BASE_URL + '/author/1')
    assert resp.json()[0]['id'] == 1

def test_delete():
    resp = requests.delete(BASE_URL + '/author/1')
    assert resp

