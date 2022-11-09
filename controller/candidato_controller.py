from repository.candidato_repository import RepositorioCandidato
from model.candidato import Candidato


class ControladorCandidato:
    def __init__(self):
        self.repo = RepositorioCandidato()

        # listar

    def index(self):
        return self.repo.find_all()

        # Crear

    def create(self, info_candidato):
        nuevo_candidato = Candidato(info_candidato)
        return self.repo.save(nuevo_candidato)

        # Leer

    def show(self, id):
        return self.repo.find_by_id(id)

        # Actualizar

    def update(self, id, info_candidato):
        candidato_actualizado = Candidato(info_candidato)
        return self.repo.update(id, candidato_actualizado)

        # Delete

    def delete(self, id):
        return self.repo.delete(id)