from repository.candidato_repository import RepositorioCandidato
from model.candidato import Candidato
from repository.partido_politico_repository import RepositorioPartidoPolitico


class ControladorCandidato:
    def __init__(self):
        self.repo = RepositorioCandidato()
        self.repo_partido_politico = RepositorioPartidoPolitico()

        # listar

    def index(self):
        return self.repo.find_all()

        # Crear

    def create(self, info_candidato):
        try:
            res = self.repo_partido_politico.find_by_id(info_candidato["id_partido_politico"])
        except:
            return {"message": "El Partido Politico con id " + info_candidato[
                "id_partido_politico"] + "no existe"}, 404
        if len(res) == 0:
            return {"message": "El Partido Politico con id " + info_candidato[
                "id_partido_politico"] + "no existe"}, 404

        nuevo_candidato = Candidato(info_candidato)
        return self.repo.save(nuevo_candidato), 200

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
