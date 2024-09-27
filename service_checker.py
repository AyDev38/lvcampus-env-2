import subprocess
import os
from colorama import Fore, Style

def check_virtualbox(os_type):
    """Vérifie si VirtualBox est installé en fonction de l'OS."""
    try:
        if os_type == "Windows":
            # Vérifier avec 'where' pour voir si VirtualBox est installé
            result = subprocess.run("where virtualbox", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(Fore.GREEN + "VirtualBox est installé." + Style.RESET_ALL)
            else:
                print(Fore.RED + "VirtualBox n'est pas installé. Vous pouvez le télécharger ici : https://www.virtualbox.org/" + Style.RESET_ALL)

        elif os_type in ["Linux", "Darwin"]:  # Linux ou macOS
            result = subprocess.run("which virtualbox", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(Fore.GREEN + "VirtualBox est installé." + Style.RESET_ALL)
            else:
                print(Fore.RED + "VirtualBox n'est pas installé. Vous pouvez le télécharger ici : https://www.virtualbox.org/" + Style.RESET_ALL)
        else:
            print(Fore.RED + "OS non supporté pour la vérification de VirtualBox." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Erreur lors de la vérification de VirtualBox : {e}" + Style.RESET_ALL)

def check_docker(os_type):
    """Vérifie si Docker est installé et si le service est actif."""
    try:
        if os_type == "Windows":
            command = "docker --version"
        elif os_type in ["Linux", "Darwin"]:  # Linux ou macOS
            command = "which docker"
        else:
            print(Fore.RED + "OS non supporté pour la vérification de Docker." + Style.RESET_ALL)
            return

        # Vérification de l'installation de Docker
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "Docker est installé." + Style.RESET_ALL)
            # Vérification si le service Docker est actif
            if os_type == "Windows":
                service_command = "sc query com.docker.service"
                service_result = subprocess.run(service_command, shell=True, capture_output=True, text=True)
                if "RUNNING" in service_result.stdout:
                    print(Fore.GREEN + "Le service Docker est actif." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Le service Docker n'est pas actif. Vous devez exécuter le script en tant qu'administrateur." + Style.RESET_ALL)
            else:  # Pour Linux et macOS
                service_command = "systemctl is-active docker"
                service_result = subprocess.run(service_command, shell=True, capture_output=True, text=True)
                if "active" in service_result.stdout:
                    print(Fore.GREEN + "Le service Docker est actif." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Le service Docker n'est pas actif. Tentative d'activation..." + Style.RESET_ALL)
                    subprocess.run("sudo systemctl start docker", shell=True)
        else:
            print(Fore.RED + "Docker n'est pas installé. Vous pouvez le télécharger ici : https://www.docker.com/get-started" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Erreur lors de la vérification de Docker : {e}" + Style.RESET_ALL)
