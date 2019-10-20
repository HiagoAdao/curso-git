from flask import Flask, jsonify, request
from calculadora.calculadora import Calculadora

app = Flask(__name__)
calculadora = Calculadora()

# GET
@app.route('/somar')
def calcula_soma():
    '''Rota para obter o nomes dos dispositivos'''
    try:
        body = request.get_json()
        response = calculadora.somar(
            body.get("elemento1"), body.get("elemento2"))
    except Exception as err:
        return jsonify({"message": err})

    return jsonify(response), 200

@app.route('/subtrair')
def calcula_subtracao():
    '''Rota para obter o nomes dos dispositivos'''
    try:
        body = request.get_json()
        response = calculadora.subtrair(
            body.get("elemento1"), body.get("elemento2"))
    except Exception as err:
        return jsonify({"message": err})

    return jsonify(response), 200

@app.route('/multiplicar')
def calcula_multiplicacao():
    '''Rota para obter o nomes dos dispositivos'''
    try:
        body = request.get_json()
        response = calculadora.multiplicar(
            body.get("elemento1"), body.get("elemento2"))
    except Exception as err:
        return jsonify({"message": err})

    return jsonify(response), 200

@app.route('/dividir')
def calcula_divisao():
    '''Rota para obter o nomes dos dispositivos'''
    try:
        body = request.get_json()
        response = calculadora.dividir(
            body.get("elemento1"), body.get("elemento2"))
    except Exception as err:
        return jsonify({"message": err})

    return jsonify(response), 200

@app.route('/elevar-quadrado')
def calcula_elevacao_ao_quadrado():
    '''Rota para obter o nomes dos dispositivos'''
    try:
        body = request.get_json()
        response = calculadora.elevar_ao_quadrado(body.get("elemento1"))
    except Exception as err:
        return jsonify({"message": err})

    return jsonify(response), 200

@app.route('/porcentagem')
def calcula_porcentagem():
    '''Rota para obter o nomes dos dispositivos'''
    try:
        body = request.get_json()
        response = calculadora.porcentagem(
            body.get("elemento1"), body.get("elemento2"))
    except Exception as err:
        return jsonify({"message": err})

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
