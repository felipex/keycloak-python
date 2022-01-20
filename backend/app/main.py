from flask import Flask, jsonify, request, abort
from flask import render_template, render_template_string
import json
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

import base64
import requests
from pprint import pprint
'''
Aqui tá usando o usuário e senha. Não é bom.
'''
def c1(token, srole):

    url = "http://172.17.0.2:8080/auth/realms/myrealm/protocol/openid-connect/token"
    data = {
            "client_id": "myclient",
            "username": "felipe",
            "password": "123456",
            "grant_type": "password"
    }

    #resp = requests.post(url, data=data)
    #token = json.loads(resp.content)['access_token']
    print(token)
    pp = token.split('.')
    print(base64.b64decode(pp[1] + '='*(-len(pp[1])%4)))

    url2 = "http://172.17.0.2:8080/auth/realms/myrealm/protocol/openid-connect/auth"
    print("Access Token")
    h = {"Authorization": token} 
    d = {"Authorization": token} 
    print(h)
    resp = requests.post(url, data=data, headers=h)
    ntoken = json.loads(resp.content)['access_token']
    
    pp = ntoken.split('.')
    dtoken = json.loads(base64.b64decode(pp[1] + '='*(-len(pp[1])%4)))
    resources = dtoken["resource_access"]
  
    indexs = srole.split(':')
    if indexs[0] in resources:
        x1 = resources[indexs[0]]
        if indexs[1] in x1['roles']:
            print("Tem permissão")
        else:
            print("Não autorizado")
    else:
        print("Nem te conheço")


def c2(token, srole):

    data = {
            "client_id": "backend",
            "client_secret": "OuWjfQWehcMz66ceeLprFlQk21BX9KG6",
            "grant_type": "client_credentials"
    }

    pp = token.split('.')
    print("-----------Veio do browser")
    print(base64.b64decode(pp[1] + '='*(-len(pp[1])%4)))
    print("-----------Fim Veio do browser")

    url = "http://172.17.0.2:8080/auth/realms/myrealm/protocol/openid-connect/token"
    print("Access Token")
    h = {"Authorization": token} 
    print(h)
    resp = requests.post(url, data=data, headers=h)
    print("------- O RESULTADO TODO")
    print(resp.content)
    print("------- FIM DO RESULTADO TODO")
    ntoken = json.loads(resp.content)['access_token']
    
    pp = ntoken.split('.')
    dtoken = json.loads(base64.b64decode(pp[1] + '='*(-len(pp[1])%4)))
    print(dtoken)
    resources = dtoken["resource_access"]
  
    indexs = srole.split(':')
    if indexs[0] in resources:
        x1 = resources[indexs[0]]
        if indexs[1] in x1['roles']:
            print("Tem permissão")
        else:
            print("Não autorizado")
    else:
        print("Nem te conheço")


def c3(token, srole):
    '''
    curl -v --data "client_secret=YOUR_SECRET9&client_id=product- 
    app&username=user&token=YOUR_TOKEN" 
    http://localhost:8080/auth/realms/springdemo/protocol/openid- 
    connect/token/introspect
    '''
    data = {
            "client_id": "backend",
            "client_secret": "OuWjfQWehcMz66ceeLprFlQk21BX9KG6",
            "username": "felipe",
            "token": token 
    }

    url = "http://172.17.0.2:8080/auth/realms/myrealm/protocol/openid-connect/userinfo"

    h = {"Authorization": token} 
    #resp = requests.post(url, data=data, headers=h)
    resp = requests.post(url, data=data, headers=h)
    print(data)
    print("------- O RESULTADO TODO")
    print(resp.content)
    print("------- FIM DO RESULTADO TODO")
    ntoken = json.loads(resp.content)['access_token']
    
    pp = ntoken.split('.')
    dtoken = json.loads(base64.b64decode(pp[1] + '='*(-len(pp[1])%4)))
    print(dtoken)
    resources = dtoken["resource_access"]
  
    indexs = srole.split(':')
    if indexs[0] in resources:
        x1 = resources[indexs[0]]
        if indexs[1] in x1['roles']:
            print("Tem permissão")
        else:
            print("Não autorizado")
    else:
        print("Nem te conheço")


@app.route("/")
def home():
    return '''
    <h1>Deu certo</h1>
    '''

@app.route("/secured")
def secured():
    print("-----------Veio do browser")
    token = request.headers['Authorization'] 
    print(token)
    print("-----------fim browser")
    c3(token, 'backend:CAD')
    return '''
    <h1>Tá seguro</h1>
    '''



