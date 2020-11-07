
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
      "name": "Sucess",
      "email": "sucess@mail.com",
      "gender": None
    },
    {
      "name": None,
      "email": None,
    },
  ]

url    = 'http://127.0.0.1:5005/insert'
header = {'Authorization':'Supersecreto 123456', 'Content-Type':'application/json, charset=utf-8'}

def test_insert_a():
  resp = requests.get(url, headers=header, json=students[0])
  assert resp.status_code in [418, 405]

def test_insert_b():
  resp = requests.post(url, headers=header, json=students[0])
  assert resp.status_code == 400
  assert json.loads(resp.text) == {"Erro" : "Records are invalid."}

def test_insert_c():
  resp = requests.post(url, headers=header, json=students[1])
  assert resp.status_code == 400
  assert json.loads(resp.text) == {"Erro" : "Records are invalid."}

def test_insert_d():
  resp = requests.post(url, headers=header, json=students[2])
  assert resp.status_code == 201
  assert sorted(json.loads(resp.text).items()) == sorted(students[2].items())

def test_insert_e():
  resp = requests.post(url, headers=header, json=students[3])
  assert resp.status_code == 400
  assert json.loads(resp.text) == {"Erro" : "Records are invalid."}

if __name__ == '__main__':
  test_insert_a()
  test_insert_b()
  test_insert_c()
  test_insert_d()
  test_insert_e()

