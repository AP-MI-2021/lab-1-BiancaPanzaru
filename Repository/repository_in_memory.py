from Domain.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, id_entity=None):
        if id_entity is None:
            return list(self.entitati.values())

        if id_entity in self.entitati:
            return self.entitati[id_entity]
        else:
            return None

    def adauga(self, entitate: Entity):
        if self.read(entitate.id_entity) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entitati[entitate.id_entity] = entitate

    def sterge(self, id_entity: str):
        if self.read(id_entity) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        del self.entitati[id_entity]

    def modifica(self, entitate: Entity):
        if self.read(entitate.id_entity) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self.entitati[entitate.id_entity] = entitate