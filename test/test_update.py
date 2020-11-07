
import requests
import json


students = [
    {
      "id": None,
      "name": "error",
      "email": "erro@mailcom",
      "gender": "male"
    },
    {
      "id": None,
      "name": "To long string To long string To long string To long string To long string ",
      "email": "Paresh@mail.com",
      "gender": "male"
    },
    {
      "id": 6,
      "name": "Alterado",
      "email": "alterado@mail.com",
      "gender": None
    },
    {
      "id": 60,
      "name": "nao encontrado",
      "email": "encontrado@mail.com",
      "gender": None
    },
  ]

url    = 'http://127.0.0.1:5005/update'
header = {'Authorization':'Supersecreto 123456', 'Content-Type':'application/json, charset=utf-8'}

def test_update_a():
  resp = requests.get(url, headers=header, json=students[0])
  assert resp.status_code in [418, 405]

def test_update_b():
  resp = requests.put(url, headers=header, json=students[0])
  assert resp.status_code == 400
  assert json.loads(resp.text) == {"Erro" : "Records are invalid."}

def test_update_c():
  resp = requests.put(url, headers=header, json=students[1])
  assert resp.status_code == 400
  assert json.loads(resp.text) == {"Erro" : "Records are invalid."}

def test_update_d():
  resp = requests.put(url, headers=header, json=students[2])
  assert resp.status_code == 200
  assert sorted(json.loads(resp.text).items()) == sorted(students[2].items())

def test_update_e():
  resp = requests.put(url, headers=header, json=students[3])
  assert resp.status_code == 404
  assert json.loads(resp.text) == {'error': 'id not found'}

if __name__ == '__main__':
  test_update_a()
  test_update_b()
  test_update_c()
  test_update_d()
  test_update_e()

