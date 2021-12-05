from Domain.cursa import Cursa
from Domain.cursaValidator import CursaValidator
from Repository.repository import Repository


class CursaService:
    def __init__(self,
                 cursa_repository: Repository,
                 cursa_validator: CursaValidator,
                 aeroport_repository: Repository):
        self.cursa_repository = cursa_repository
        self.cursa_validator = cursa_validator
        self.aeroport_repository = aeroport_repository

    def add_cursa(self,
                     id_cursa: str,
                     id_aeroport_pornire: str,
                     id_aeroport_sosire: str,
                     distanta: int):
        cursa = Cursa(id_cursa, id_aeroport_pornire, id_aeroport_sosire, distanta)
        self.cursa_repository.create(cursa)
        self.cursa_validator.valideaza_cursa(cursa)

    def get_all(self):
        return self.cursa_repository.read()