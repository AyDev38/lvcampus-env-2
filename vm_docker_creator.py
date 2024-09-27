import os
import subprocess
from colorama import Fore, Style

def load_iso_path():
    """Lire le chemin de l'ISO depuis le fichier de configuration."""
    try:
        with open("config.txt", "r") as file:
            iso_path = file.readline().strip()
            return iso_path
    except FileNotFoundError:
        print(f"{Fore.RED}Le fichier de configuration 'config.txt' est introuvable.{Style.RESET_ALL}")
        return None

def create_vm(iso_path):
    """Créer une machine virtuelle via VirtualBox avec l'ISO spécifié."""
    if iso_path is None or not os.path.isfile(iso_path):
        print(f"{Fore.RED}Le chemin ISO spécifié n'est pas valide ou n'existe pas : {iso_path}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Veuillez vérifier votre fichier de configuration et réessayer.{Style.RESET_ALL}")
        return  # Arrête la création si le chemin ISO est invalide

    try:
        # Créer la VM
        subprocess.run(["VBoxManage", "createvm", "--name", "MyLinuxVM", "--register"], check=True)
        subprocess.run(["VBoxManage", "modifyvm", "MyLinuxVM", "--memory", "2048", "--cpus", "2"], check=True)

        # Attacher l'ISO
        subprocess.run(["VBoxManage", "storagectl", "MyLinuxVM", "--name", "IDE Controller", "--add", "ide"], check=True)
        subprocess.run(["VBoxManage", "storageattach", "MyLinuxVM", "--storagectl", "IDE Controller", "--port", "0", "--device", "0", "--type", "dvddrive", "--medium", iso_path], check=True)

        print(f"{Fore.GREEN}Machine virtuelle créée avec succès avec l'ISO spécifié.{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Échec de la création de la machine virtuelle: {e}{Style.RESET_ALL}")

def create_docker_container():
    """Créer un conteneur Docker en fonction de l'entrée de l'utilisateur."""
    container_options = {
        1: "ubuntu",
        2: "debian",
        3: "rockylinux",
        4: "fedora",
        5: "python",
        6: "mariadb"
    }

    print("Quel type de conteneur souhaitez-vous créer ?")
    for num, name in container_options.items():
        print(f"{num}. {name.capitalize()}")

    choice = int(input("Veuillez choisir un numéro : "))
    container_type = container_options.get(choice)

    if container_type is None:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
        return

    persistent_volume = input("Voulez-vous rattacher un volume persistant ? (oui/non) : ").strip().lower()
    volume_option = "-v my_volume:/data" if persistent_volume == "oui" else ""

    try:
        subprocess.run(f"docker run -d --name {container_type} {volume_option} {container_type}", shell=True, check=True)
        print(f"{Fore.GREEN}Conteneur {container_type} créé avec succès.{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Échec de la création du conteneur.{Style.RESET_ALL}")
