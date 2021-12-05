from Domain.aeroportValidator import AeroportValidare
from Domain.cursaValidator import CursaValidator
from Repository.repository_json import JsonRepository
from Service.aeroport_service import AeroportService
from Service.cursa_service import CursaService
from UI.console import Console


def main():
    aeroport_repository = JsonRepository('aeroporturi.json')
    aeroport_validator = AeroportValidare()
    aeroport_service = AeroportService(aeroport_repository, aeroport_validator)

    cursa_repository = JsonRepository('curse.json')
    cursa_validator = CursaValidator()
    cursa_service = CursaService(cursa_repository, cursa_validator, aeroport_repository)

    console = Console(aeroport_service, cursa_service)
    console.run_console()

if __name__ == '__main__':
    main()