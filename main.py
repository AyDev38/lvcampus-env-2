import os_detector
import service_checker
from colorama import Fore, Style
from vm_docker_creator import load_iso_path, create_vm, create_docker_container  # Importer les fonctions

if __name__ == "__main__":
    os_type = os_detector.detect_os()
    service_checker.check_virtualbox(os_type)
    service_checker.check_docker(os_type)

    # Charger le chemin de l'ISO
    iso_path = load_iso_path()

    choice = input("Souhaitez-vous créer une VM (1) ou un conteneur Docker (2) ? (tapez 1 ou 2) : ")

    if choice == "1":
        create_vm(iso_path)
    elif choice == "2":
        create_docker_container()
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
