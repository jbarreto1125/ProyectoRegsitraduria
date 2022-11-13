from model.votacion import Votacion
from repository.repository_interface import InterfaceRepository
from repository.candidato_repository import RepositorioCandidato
from repository.mesa_repository import RepositorioMesa


class RepositorioVotacion(InterfaceRepository[Votacion]):
    def __init__(self):
        super().__init__()
        self.repo_can = RepositorioCandidato()
        self.repo_mes = RepositorioMesa()
    def find_all(self):
        lista_votaciones = super().find_all()
        for x in lista_votaciones:
            id_mes = x["id_mesa"]
            id_can = x["id_candidato"]
            del x["id_mesa"]
            del x["id_candidato"]
            x["mesa"] = self.repo_mes.find_by_id(id_mes)
            x["candidato"] = self.repo_can.find_by_id(id_can)

        return lista_votaciones

