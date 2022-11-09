from model.partido_politico import PartidoPolitico
from repository.partido_politico_repository import RepositorioPartidoPolitico


class ControladorPartidoPolitico:
    def __init__(self):
        self.repo = RepositorioPartidoPolitico()

    # listar
    def index(self):
        return self.repo.find_all()

    # Crear
    def create(self, info_partido_politico):
        nuevo_partido_politico = PartidoPolitico(info_partido_politico)
        return self.repo.save(nuevo_partido_politico)

    # Leer
    def show(self, id):
        return self.repo.find_by_id(id)

    # Actualizar
    def update(self, id, info_partido_politico):
        partido_politico_actualizado = PartidoPolitico(info_partido_politico)
        return self.repo.update(id, partido_politico_actualizado)

    # Delete
    def delete(self, id):
        return self.repo.delete(id)
