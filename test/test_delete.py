
import requests

url    = 'http://127.0.0.1:5005/delete'
header = {'Authorization':'Supersecreto 123456', 'Content-Type':'application/json, charset=utf-8'}

def test_delete_a():
  resp = requests.delete(url+'/4', headers=header, data=b'{"key": 12}')
  assert resp.status_code == 200

def test_delete_b():
  resp = requests.delete(url+'/4', headers=header, data=b'{"key": 20}')
  assert resp.status_code == 401

def test_delete_c():
  resp = requests.delete(url+'/40', headers=header, data=b'{"key": 120}')
  assert resp.status_code == 404

if __name__ == '__main__':
  test_delete_a()
  test_delete_b()
  test_delete_c()

