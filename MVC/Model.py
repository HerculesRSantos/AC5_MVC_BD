from flask import Flask, request, jsonify, make_response, render_template, redirect, session, flash
import json

# implementação de regra de negocio


tasks = [
    {
        'id': 1,
        'name': "Hercules Rodrigues dos Santos",
        "description": "Um Maluco no pedaço....Hehehe",
        "idade" :  45
    },
    {
        "id": 2,
        "name": " Eduardo da Cruz Rodrigues",
        "description": " O Otaku",
        "idade" :  22
    },
    {
        "id": 3,
        "name": "Vitor Fraga",
        "description": " Mestre do Front",
        "idade" :  20
    }
]



Grupo = json.dumps(tasks)

class Model():

    def jsonReturn():
        return Grupo

    
    
    def somaidade():
        total = 0
        for task in tasks:
            total += task.get ("idade")
        return {
            "idade_total" : total
        }


   