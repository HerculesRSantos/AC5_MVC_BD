from flask import Flask, request, jsonify, make_response, render_template, redirect, flash, session
from Model import Model
from ModelConn import ClienteModel
#from flask_mysqldb import MySQL

# Aqui fazemos somente as chamadas

# Rotas

app = Flask(__name__) 

@app.route('/v1/aula/consultar/', methods=["GET"])
def consultar():
    return Model.jsonReturn()


@app.route('/v1/aula/consultar/somar', methods=["GET"])
def somar():
    return Model.somaidade()






@app.route('/v1/aula/cadastrar', methods=["GET"])
def cadastrarEmail():
    return ClienteModel.cadastrarEmail()



#@app.route('/v1/aula/cadastrar/atualizar', methods=["GET"])
#def atualizar():
 #   return ClienteModel.atualizar()



if __name__ == '__main__':
    app.run(debug=True,port= 5000)