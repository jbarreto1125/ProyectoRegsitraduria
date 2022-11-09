from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controller.partido_politico_controller import ControladorPartidoPolitico

partido_politico_controller = ControladorPartidoPolitico()

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
def mostrar_partidos_politicos(id):
    par = partido_politico_controller.show(id)
    return jsonify(par)


@app.route("/partido_politico/<string:id>", methods=["DELETE"])
def eliminar_partido_politico(id):
    par = partido_politico_controller.delete(id)
    return jsonify(par)


if __name__ == "__main__":
    data_config = load_file_config()
    print(f"Server running : http://{data_config['url-backend']}:{data_config['port']}")
    serve(app, host=data_config["url-backend"], port=data_config["port"])
