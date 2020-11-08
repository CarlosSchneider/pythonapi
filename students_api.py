#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request, jsonify, session
import json
import re
# import ssl

# SSLcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# SSLcontext.load_cert_chain(certfile='server.crt', keyfile='server.key')


htmlbones = """
  <!DOCTYPE html>
  <html lang="pt-br">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>{}</title>
    </head>
    <body>
      <div><pre style="margin: 10px; white-space: pre-wrap;">
        {}
      </pre></div>
    </body>
    <footer>
    <div>
    <p> Request from: {}</p>
    <p> Sistema desenvolvido para testes de dispobilidade de dados por API.<br />Carlos A. Schneider - 2020</p>
    </div>
    </footer>
  </html>
  """

emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

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

app = Flask(__name__)

def validar_chave(request):
  return True \
    if request.headers.get('Authorization') == 'Supersecreto 123456' \
    else False

# ***   INFORMACOES DE COMO USAR A API   ***
@app.route('/info', methods=['GET'])
def readme():
  with open('README.md', 'r', encoding='utf8') as f:
    data = f.read()
  return data

@app.route('/info.html', methods=['GET'])
def readmeformated():
  return htmlbones.format("Título", readme(), 
  "{} - {} - {}".format(request.remote_addr, request.remote_user, request.user_agent))

# ***   LEITURA DOS REGISTROS DA TABELA   ***
@app.route('/load/', methods=['GET'])
def load_all():
  try:
    if not validar_chave(request):
      return jsonify({'error': 'unauthorized'}), 401
    name = request.args.get('name')
    data = students
    if name:
      data = [field for field in data if name in field["name"]]
    return jsonify(data)
  except Exception as e:
    return jsonify({'error': 'data not found', "Exception": e}), 404

@app.route('/load/<int:id>', methods=['GET'])
def load_by_id(id):
  try:
    if not validar_chave(request):
      return jsonify({'error': 'unauthorized'}), 401
    data = students
    data = [field for field in data if field["id"] == id]
    if len(data) < 1:
      return jsonify({'error': 'data not found'}), 404
    return jsonify(data[0])
  except Exception as e:
    return jsonify({'error': 'undefind error', "Exception": e}), 500


# ***   VALIDAR DADOS PARA REGISTRO    ***
def record_isvalid(record):
  between = lambda value,mim,max: (value >= mim and value <= max)
  if not record:
    record = request.json
  if not record:
    return {"value": False, "column": "all"}
  if not between(len(str(record.get('name'))), 5, 60):
    return {"value": False, "column": "name"}
  if not re.search(emailregex, str(record.get('email'))):
    return {"value": False, "column": "email"}
  return {"value": True}

@app.route('/isvalid', methods=['POST'])
def isvalid():
  valid = record_isvalid(request.json)
  if not valid.get("value"):
    return jsonify(valid), 400
  return jsonify(valid)


# ***   GRAVACAO DE NOVOS REGISTROS DA TABELA   ***
@app.route('/insert', methods=['POST'])
def insert_record():
  try:
    if not validar_chave(request):
      return jsonify({'error': 'unauthorized'}), 401
    if request.method != 'POST':
      return "Invalid method", 418
    record = request.json
    isvalid = record_isvalid(record)
    if not isvalid.get("value"):
      return jsonify({"Erro" : "Records are invalid."}), 400
    record['id'] = len(students) + 1
    students.append(record)
    return jsonify(record), 201
  except Exception as e:
    return jsonify({'error': 'undefind error', "Exception": e}), 500


# ***   ALTERACAO DE REGISTROS DA TABELA   ***
@app.route('/update', methods=['PUT'])
def update_record():
  try:
    if not validar_chave(request):
      return jsonify({'error': 'unauthorized'}), 401
    if request.method != 'PUT':
      return "Invalid method", 418
    record = request.json
    isvalid = record_isvalid(record)
    if not isvalid.get("value"):
      return jsonify({"Erro" : "Records are invalid."}), 400
    data = students
    idx  = [index for index, field in enumerate(data) if field['id'] == record['id']]
    if len(idx) != 1:
      return jsonify({'error': 'id not found'}), 404
    students[idx[0]] = record
    return jsonify(students[idx[0]])
  except Exception as e:
    return jsonify({'error': 'undefind error', "Exception": e}), 500

# ***   EXCLUSAO DE REGISTRO DA TABELA   ***
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
  try:
    if not validar_chave(request):
      return jsonify({'error': 'unauthorized'}), 401
    if request.method != 'DELETE':
      return "Invalid method", 418
    data = request.data
    data = json.loads(data.decode())
    if data['key'] != (id * 3):
      return jsonify({'error': 'invalid key'}), 401
    data = students
    idx  = [index for index, field in enumerate(data) if field['id'] == id]
    if len(idx) != 1:
      return jsonify({'error': 'id not found'}), 404
    data = students.pop(idx[0])
    return jsonify({"status": "record deleted", "record": data})
  except Exception as e:
    return jsonify({'error': 'undefind error', "Exception": e}), 500


app.run(debug=True, host='0.0.0.0', port=5005)
# app.run(debug=True, port=5005, host='0.0.0.0', ssl_context=SSLcontext)
#FIM

