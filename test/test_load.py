
import requests
import json


students = [
    {
      "id": 1,
      "name": "Hardik",
      "email": "hardik@gmail.com",
      "gender": "male"
    },
    {
      "id": 2,
      "name": "Paresh",
      "email": "Paresh@gmail.com",
      "gender": "male"
    },
    {
      "id": 3,
      "name": "Kiran",
      "email": "kiran@gmail.com",
      "gender": "female"
    },
    {
      "id": 4,
      "name": "Mahesh",
      "email": "mahesh@gmail.com",
      "gender": "male"
    },
    {
      "id": 5,
      "name": "Karan",
      "email": "karan@gmail.com",
      "gender": "male"
    },
  ]

url    = 'http://127.0.0.1:5005/load'
header = {'Authorization':'Supersecreto 123456', 'Content-Type':'application/json, charset=utf-8'}

def test_load_a():
  resp = requests.get(url, headers=header)
  assert resp.status_code == 200
  assert sorted(json.loads(resp.text)[0].items()) == sorted(students[0].items())

def test_load_b():
  resp = requests.get(url+'/3', headers=header)
  assert resp.status_code == 200
  assert sorted(json.loads(resp.text).items()) == sorted(students[2].items())

def test_load_c():
  resp = requests.get(url, headers=header, params={"name": "ran"})
  assert resp.status_code == 200
  assert sorted(json.loads(resp.text)[1].items()) == sorted(students[4].items())

def test_load_d():
  resp = requests.get(url+'/30', headers=header)
  assert resp.status_code == 404

if __name__ == '__main__':
  test_load_a()
  test_load_b()
  test_load_c()
  test_load_d()