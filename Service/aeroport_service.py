
from Domain.aeroport import Aeroport
from Domain.aeroportValidator import AeroportValidare
from Repository.repository import Repository


class AeroportService:
    def __init__(self,
                 aeroport_repository: Repository,
                 aeroport_validator: AeroportValidare):
        self.aeroport_repository = aeroport_repository
        self.aeroport_validator = aeroport_validator

    def add_aeroport(self,
                     id_aeroport: str,
                     indicativ: str,
                     lungime_max: int):
        aeroport = Aeroport(id_aeroport, indicativ, lungime_max)
        self.aeroport_validator.validare_aeroport(aeroport,
                                                  self.aeroport_repository)
        self.aeroport_repository.create(aeroport)


    def get_all(self):
        return self.aeroport_repository.read()