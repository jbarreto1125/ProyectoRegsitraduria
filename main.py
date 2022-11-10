from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controller.partido_politico_controller import ControladorPartidoPolitico
from controller.mesa_controller import ControladorMesa
from controller.candidato_controller import ControladorCandidato

partido_politico_controller = ControladorPartidoPolitico()
mesa_controller = ControladorMesa()
candidato_controller = ControladorCandidato

app = Flask(__name__)
cors = CORS(app)


def load_file_config():
    with open("config.json") as f:
        data = json.load(f)
    return data


@app.route("/partido_politico", methods=["POST"])
def crear_partido_politico():
    info_partido_politico = request.get_json()
    partido_politico_creado = partido_politico_controller.create(info_partido_politico)
    return jsonify(partido_politico_creado)


@app.route("/partido_politico/<string:id>", methods=["PUT"])
def actualizar_partido_politico(id):
    info_partido_politico = request.get_json()
    partido_politico_actualizado = partido_politico_controller.update(id, info_partido_politico)
    return jsonify(partido_politico_actualizado)


@app.route("/partidos_politicos", methods=["GET"])
def listar_partidos_politicos():
    lista_partidos_politicos = partido_politico_controller.index()
    return jsonify(lista_partidos_politicos)


@app.route("/partido_politico/<string:id>", methods=["GET"])
def mostrar_partido_politico(id):
    par = partido_politico_controller.show(id)
    return jsonify(par)


@app.route("/partido_politico/<string:id>", methods=["DELETE"])
def eliminar_partido_politico(id):
    par = partido_politico_controller.delete(id)
    return jsonify(par)


@app.route("/mesa", methods=["POST"])
def crear_mesa():
    info_mesa = request.get_json()
    mesa_creada = mesa_controller.create(info_mesa)
    return jsonify(mesa_creada)


@app.route("/mesa/<string:id>", methods=["PUT"])
def actualizar_mesa(id):
    info_mesa = request.get_json()
    mesa_actualizada = mesa_controller.update(id, info_mesa)
    return jsonify(mesa_actualizada)


@app.route("/mesas", methods=["GET"])
def listar_mesas():
    lista_mesas = mesa_controller.index()
    return jsonify(lista_mesas)


@app.route("/mesa/<string:id>", methods=["GET"])
def mostrar_mesa(id):
    mes = mesa_controller.show(id)
    return jsonify(mes)


@app.route("/mesa/<string:id>", methods=["DELETE"])
def eliminar_mesa(id):
    mes = mesa_controller.delete(id)
    return jsonify(mes)


@app.route("/candidato", methods=["POST"])
def crear_candidato():
    info_candidato = request.get_json()
    candidato_creado = candidato_controller.create(info_candidato)
    return jsonify(candidato_creado[0]), candidato_creado[1]


@app.route("/candidato/<string:id>", methods=["PUT"])
def actualizar_candidato(id):
    info_candidato = request.get_json()
    candidato_actualizado = candidato_controller.update(id, info_candidato)
    return jsonify(candidato_actualizado)


@app.route("/candidatos", methods=["GET"])
def listar_candidatos():
    lista_candidatos = candidato_controller.index()
    return jsonify(lista_candidatos)


@app.route("/candidato/<string:id>", methods=["GET"])
def mostrar_candidato(id):
    can = candidato_controller.show(id)
    return jsonify(can)


@app.route("/candidato/<string:id>", methods=["DELETE"])
def eliminar_candidato(id):
    can = candidato_controller.delete(id)
    return jsonify(can)


if __name__ == "__main__":
    data_config = load_file_config()
    print(f"Server running : http://{data_config['url-backend']}:{data_config['port']}")
    serve(app, host=data_config["url-backend"], port=data_config["port"])
