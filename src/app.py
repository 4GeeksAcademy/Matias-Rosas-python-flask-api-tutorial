
from flask import Flask,jsonify
from flask import request
app = Flask(__name__)
#MAIN API:
#https://fictional-goldfish-9764jqppvgv5c9w9-3245.app.github.dev/todos

#Recordar siempre correr: pipenv run python src/app.py
# y cambiar la visibilidad del puerto a Public

todos =[{"label":"My first task","done":False},{"label":"My second task","done":False}]

@app.route('/todos', methods=['GET'])
def hello_world():
     print("Aqui esta la request de traer todos los todos")
     return jsonify(todos) 
    #En este jsonify podemos poner un mensaje para el usuario como por ejemplo: jsonify({"msg": "OK", "Este es el array: ": todos})

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body) 
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)    
    popped = todos.pop(position)
    print("Este es la task que ha sido eliminada: ", popped)
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)