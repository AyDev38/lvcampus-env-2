import pytest
import subprocess
import os
from vm_docker_creator import load_iso_path, create_vm, create_docker_container
import io

@pytest.fixture
def mock_subprocess_run_success(monkeypatch):
    """Simule une exécution réussie des commandes subprocess.run."""
    def mock_run(command, check, shell=False):
        return subprocess.CompletedProcess(command, returncode=0)
    monkeypatch.setattr(subprocess, "run", mock_run)

@pytest.fixture
def mock_subprocess_run_failure(monkeypatch):
    """Simule une exécution échouée des commandes subprocess.run."""
    def mock_run(command, check, shell=False):
        raise subprocess.CalledProcessError(returncode=1, cmd=command)
    monkeypatch.setattr(subprocess, "run", mock_run)

@pytest.fixture
def mock_os_path_isfile(monkeypatch):
    """Simule que le chemin ISO est toujours valide."""
    def mock_isfile(path):
        return True  # Simule que le fichier ISO est valide
    monkeypatch.setattr(os.path, "isfile", mock_isfile)

@pytest.fixture
def mock_input(monkeypatch):
    """Simule l'entrée utilisateur pour la sélection de conteneurs."""
    def mock_input_func(prompt):
        if "Quel type de conteneur" in prompt:
            return "1"  # Simule la sélection de 'ubuntu'
        if "Voulez-vous rattacher un volume persistant" in prompt:
            return "non"  # Simule une réponse 'non' pour le volume persistant
        return "1"  # Valeur par défaut pour tout autre input
    monkeypatch.setattr("builtins.input", mock_input_func)

# Correction du test load_iso_path
def test_load_iso_path_success(monkeypatch):
    """Teste si le chemin ISO est correctement lu depuis config.txt."""
    mock_path = "C:/Users/aymer/Downloads/ubuntu-24.04.1-desktop-amd64.iso"
    
    # Utilise StringIO pour simuler un fichier lisible
    def mock_open(*args, **kwargs):
        return io.StringIO(mock_path)
    
    monkeypatch.setattr("builtins.open", mock_open)
    iso_path = load_iso_path()
    assert iso_path == mock_path

def test_load_iso_path_file_not_found(monkeypatch):
    """Teste le comportement lorsque config.txt est introuvable."""
    with monkeypatch.context() as m:
        # Lever explicitement l'exception FileNotFoundError
        m.setattr("builtins.open", lambda x, y: (_ for _ in ()).throw(FileNotFoundError))
        iso_path = load_iso_path()
        assert iso_path is None

# Tests pour la fonction create_vm
def test_create_vm_success(mock_subprocess_run_success, mock_os_path_isfile):
    """Test si la VM est créée avec succès."""
    iso_path = "C:/Users/aymer/Downloads/ubuntu-24.04.1-desktop-amd64.iso"
    create_vm(iso_path)
    # Si aucune exception n'est levée, on considère que la VM est créée avec succès

def test_create_vm_invalid_iso(monkeypatch):
    """Teste si la VM échoue à être créée avec un ISO invalide."""
    with monkeypatch.context() as m:
        m.setattr(os.path, "isfile", lambda x: False)  # Simule un fichier ISO invalide
        create_vm("/invalid/path/to/iso")
        # Vérifie que la VM n'est pas créée avec un chemin ISO invalide

def test_create_vm_failure(mock_subprocess_run_failure, mock_os_path_isfile):
    """Test si une erreur se produit lors de la création de la VM."""
    iso_path = "C:/Users/aymer/Downloads/ubuntu-24.04.1-desktop-amd64.iso"
    create_vm(iso_path)
    # Si une exception subprocess.CalledProcessError est capturée, l'échec est simulé

# Correction du test create_docker_container
def test_create_docker_container_success(mock_subprocess_run_success, mock_input):
    """Test si le conteneur Docker est créé avec succès."""
    create_docker_container()
    # Simule la création réussie d'un conteneur Docker

def test_create_docker_container_failure(mock_subprocess_run_failure, mock_input):
    """Test si une erreur se produit lors de la création d'un conteneur Docker."""
    create_docker_container()
    # Simule l'échec de la création d'un conteneur Docker
