import platform
import subprocess
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)


def detect_os():
    """
    Detect the operating system and return its name.
    Supported: Linux, Darwin (macOS), Windows.
    """
    os_name = platform.system()

    if os_name == "Linux":
        print(Fore.GREEN + "Operating System detected: Linux")
        return "Linux"
    elif os_name == "Darwin":
        print(Fore.GREEN + "Operating System detected: macOS")
        return "macOS"
    elif os_name == "Windows":
        print(Fore.GREEN + "Operating System detected: Windows")
        return "Windows"
    else:
        print(Fore.RED + f"Unsupported Operating System: {os_name}")
        return None


def check_virtualbox(os_type):
    """Vérifie si VirtualBox est installé en fonction de l'OS."""
    try:
        if os_type == "Windows":
            # Vérifier avec 'where' pour voir si VirtualBox est installé
            result = subprocess.run("where virtualbox", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(Fore.GREEN + "VirtualBox est installé." + Style.RESET_ALL)
            else:
                print(
                    Fore.RED + "VirtualBox n'est pas installé. Vous pouvez le télécharger ici : https://www.virtualbox.org/" + Style.RESET_ALL)

        elif os_type in ["Linux", "Darwin"]:  # Linux ou macOS
            result = subprocess.run("which virtualbox", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(Fore.GREEN + "VirtualBox est installé." + Style.RESET_ALL)
            else:
                print(
                    Fore.RED + "VirtualBox n'est pas installé. Vous pouvez le télécharger ici : https://www.virtualbox.org/" + Style.RESET_ALL)
        else:
            print(Fore.RED + "OS non supporté pour la vérification de VirtualBox." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Erreur lors de la vérification de VirtualBox : {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    os_type = detect_os()  # Détecte le système d'exploitation
    if os_type:
        check_virtualbox(os_type)  # Vérifie si VirtualBox est installé
