from repository.votacion_repository import RepositorioVotacion
from model.votacion import Votacion


class ControladorVotacion:
    def __init__(self):
        self.repo = RepositorioVotacion()

        # listar

    def index(self):
        return self.repo.find_all()

        # Crear

    def create(self, info_votacion):
        nueva_votacion = Votacion(info_votacion)
        return self.repo.save(nueva_votacion)

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