import json

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

    def export_json(self, export_filename):
        result = {}
        curse = self.cursa_repository.read()
        for aeroport in self.aeroport_repository.read():
            id_from_aerport = [cursa.id_aeroport_sosire for cursa in curse if cursa.id_aeroport_pornire == aeroport.id_entity]
            result[aeroport.indicativ] = [self.aeroport_repository.read(id_aeroport_sosire).indicativ
                                          for id_aeroport_sosire in id_from_aerport]
        with open(export_filename, 'w') as f:
            json.dump(result, f)
