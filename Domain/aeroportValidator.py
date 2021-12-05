
from Domain.aeroport import Aeroport

from Repository.repository import Repository


class AeroportValidare:
    def validare_aeroport(self, aeroport: Aeroport):
        erori = []
        if len(aeroport.indicativ) != 4:
            erori.append("Indicativul trebuie sa contina exact 4 caractere.")
        '''aeroporturi = self.aeroport_repository.read()
        for aeroport in aeroporturi:
            if aeroporturi.indicativ == aeroport. indicativ:
                erori.append("Indicativul trebuie sa fie unic")'''
        if aeroport.lungime_max < 1000:
                erori.append("Lungimea minim 1000 METRI")
        if erori:
            raise ValueError(erori)