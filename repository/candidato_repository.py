from model.candidato import Candidato
from repository.repository_interface import InterfaceRepository
from repository.partido_politico_repository import RepositorioPartidoPolitico


class RepositorioCandidato(InterfaceRepository[Candidato]):

    def __init__(self):
        super().__init__()
        self.repo_par = RepositorioPartidoPolitico()

    def find_all(self):
        lista_candidatos = super().find_all()
        for x in lista_candidatos:
            id_par = x["id_partido_politico"]
            del x["id_partido_politico"]
            x["partido_politico"] = self.repo_par.find_by_id(id_par)
        return lista_candidatos

    def find_by_id(self, id):
        candidato = super().find_by_id(id)
        id_par = candidato["id_partido_politico"]
        del candidato["id_partido_politico"]
        candidato["partido_politico"] = self.repo_par.find_by_id(id_par)
        return candidato
