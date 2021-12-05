from Domain.cursa import Cursa


class CursaValidator:
    def valideaza_cursa(self, cursa: Cursa):
        erori = []
        if cursa.id_aeroport_pornire is None:
            erori.append("id_aeroport_pornire nu poate fi nul")
        if cursa.id_aeroport_sosire is None:
            erori.append("id_aeroport_sosirenu poate fi nul")
        if cursa.id_aeroport_pornire == cursa.id_aeroport_sosire:
            erori.append("Trebuie sa fie distincte")
        if cursa.distanta < 500:
            erori.append("Distanta minim 500 KM")
        if erori:
            raise ValueError(erori)