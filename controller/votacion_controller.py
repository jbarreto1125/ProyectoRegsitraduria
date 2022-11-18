from repository.votacion_repository import RepositorioVotacion
from repository.candidato_repository import RepositorioCandidato
from repository.mesa_repository import RepositorioMesa
from model.votacion import Votacion


class ControladorVotacion:
    def __init__(self):
        self.repo = RepositorioVotacion()
        self.repo_candidato = RepositorioCandidato()
        self.repo_mesa = RepositorioMesa()

        # listar

    def index(self):
        return self.repo.find_all()

        # Crear

    def create(self, info_votacion):
        try:
            vot = self.repo_mesa.find_by_id(info_votacion["id_mesa"])

        except:
            return {"message": "La Mesa con id " + info_votacion["id_mesa"] + " no existe"}, 400
        try:
            vot = self.repo_candidato.find_by_id(info_votacion["id_candidato"])

        except:
            return {"message": "El Candidato con id " + info_votacion["id_candidato"] + " no existe"}, 400

        nueva_votacion = Votacion(info_votacion)
        return self.repo.save(nueva_votacion), 200

        # Leer

    def show(self, id):
        return self.repo.find_by_id(id)

        # Actualizar

    def update(self, id, info_votacion):
        voto_actualizado = Votacion(info_votacion)
        return self.repo.update(id, voto_actualizado)

        # Delete

    def delete(self, id):
        return self.repo.delete(id)

    def find_by_mesa(self, id_mesa):
        resultados = self.repo.query({"id_mesa": id_mesa})
        for x in resultados:
            del x["id_mesa"]
            id_candidato = x["id_candidato"]
            del x["id_candidato"]
            x["candidato"] = self.repo_candidato.find_by_id(id_candidato)
        return resultados

    def find_by_candidato(self, id_candidato):
        resultados = self.repo.query({"id_candidato": id_candidato})
        for x in resultados:
            del x["id_candidato"]
            id_mesa = x["id_mesa"]
            del x["id_mesa"]
            x["mesa"] = self.repo_mesa.find_by_id(id_mesa)
        return resultados
