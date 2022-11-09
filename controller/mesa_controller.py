from repository.mesa_repository import RepositorioMesa
from model.mesa import Mesa


class ControladorMesa:
    def __init__(self):
        self.repo = RepositorioMesa()

        # listar

    def index(self):
        return self.repo.find_all()

        # Crear

    def create(self, info_mesa):
        nueva_mesa = Mesa(info_mesa)
        return self.repo.save(nueva_mesa)

        # Leer

    def show(self, id):
        return self.repo.find_by_id(id)

        # Actualizar

    def update(self, id, info_mesa):
        mesa_actualizada = Mesa(info_mesa)
        return self.repo.update(id, mesa_actualizada)

        # Delete

    def delete(self, id):
        return self.repo.delete(id)
