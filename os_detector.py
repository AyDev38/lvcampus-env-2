import platform
from colorama import init, Fore

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

if __name__ == "__main__":
    detect_os()
