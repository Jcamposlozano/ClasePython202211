from flask import Flask, jsonify, request

from indicadores import Indicadores

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({"response": " hola mundo " })

@app.route('/indicadores', methods=['GET'])
def allIndicadores():
    i = Indicadores().ExtraeData()
    return jsonify(i)

@app.route('/indicadores', methods=['POST'])
def OneIndicator():
    i = Indicadores().ExtraeData()
    contenido_body = request.get_json()
    respuesta = i[contenido_body['indicador']]

    return jsonify({"response": respuesta })

def main():
    app.run(host = "0.0.0.0", port=("4050"), debug=True)

if __name__ == '__main__':
    try:
        main() 
    except KeyboardInterrupt:
        print('Saliendo')
        exit()





