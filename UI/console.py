from Service.aeroport_service import AeroportService
from Service.cursa_service import CursaService


class Console:
    def __init__(self,
                 aeroport_service: AeroportService,
                 cursa_service: CursaService):
        self.aeroport_service = aeroport_service
        self.cursa_service = cursa_service

    def ShowMenu(self):
        print('x. Iesire')

    def run_console(self):
        while True:
            self.ShowMenu()
            opt = input("Alegeti optiunes: ")
            if opt == 'aa':
                self.handle_add_aeroport()
            elif opt == 'ac':
                self.handle_add_cursa()
            elif opt == 'sa':
                self.handle_show_all(self.aeroport_service.get_all())
            elif opt == 'sc':
                self.handle_show_all(self.cursa_service.get_all())
            elif opt == 'export':
                self.handle_export()
            elif opt == 'x':
                break
            else:
                print("Optiune invalida")

    def handle_add_aeroport(self):
        try:
            id_aeroport = input("Dati id-ul: ")
            indicativ = input("Dati indicativul: ")
            lungime_max = int(input("Dati lungimes: "))
            self.aeroport_service.add_aeroport(id_aeroport,indicativ,lungime_max)
        except Exception as e:
            print(e)

    def handle_add_cursa(self):
        try:
            id_cursa = input("Dati id-ul cursei: ")
            id_aeroport_pornire = input("Dati id pornire: ")
            id_aeroport_sosire = input("Dati id sosire: ")
            distanta = int(input("Dati distanta: "))
            self.cursa_service.add_cursa(id_cursa, id_aeroport_pornire, id_aeroport_sosire, distanta)
        except Exception as e:
            print(e)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_export(self):
        try:
            filename = input('Nume fisier: ')
            self.cursa_service.export_json(filename)
        except Exception as e:
            print(e)

