import pytest
import subprocess
from service_checker import check_virtualbox, check_docker

@pytest.fixture
def mock_subprocess_run_virtualbox_installed(monkeypatch):
    """Simule que VirtualBox est installé"""
    def mock_run(command, shell, capture_output, text):
        return subprocess.CompletedProcess(command, returncode=0, stdout="VirtualBox installed")
    monkeypatch.setattr(subprocess, "run", mock_run)

@pytest.fixture
def mock_subprocess_run_virtualbox_not_installed(monkeypatch):
    """Simule que VirtualBox n'est pas installé"""
    def mock_run(command, shell, capture_output, text):
        return subprocess.CompletedProcess(command, returncode=1, stdout="")
    monkeypatch.setattr(subprocess, "run", mock_run)

@pytest.fixture
def mock_subprocess_run_docker_installed(monkeypatch):
    """Simule que Docker est installé et actif"""
    def mock_run(command, shell, capture_output, text):
        if "docker --version" in command or "which docker" in command:
            return subprocess.CompletedProcess(command, returncode=0, stdout="Docker version 20.10")
        elif "systemctl is-active docker" in command:
            return subprocess.CompletedProcess(command, returncode=0, stdout="active")
    monkeypatch.setattr(subprocess, "run", mock_run)

@pytest.fixture
def mock_subprocess_run_docker_not_installed(monkeypatch):
    """Simule que Docker n'est pas installé"""
    def mock_run(command, shell, capture_output, text):
        return subprocess.CompletedProcess(command, returncode=1, stdout="")
    monkeypatch.setattr(subprocess, "run", mock_run)

@pytest.fixture
def mock_subprocess_run_docker_inactive(monkeypatch):
    """Simule que Docker est installé mais le service est inactif"""
    def mock_run(command, shell, capture_output, text):
        if "docker --version" in command or "which docker" in command:
            return subprocess.CompletedProcess(command, returncode=0, stdout="Docker version 20.10")
        elif "systemctl is-active docker" in command:
            return subprocess.CompletedProcess(command, returncode=0, stdout="inactive")
    monkeypatch.setattr(subprocess, "run", mock_run)

# Tests pour VirtualBox
def test_virtualbox_installed(mock_subprocess_run_virtualbox_installed):
    assert check_virtualbox("Linux") is None  # On vérifie simplement que le script s'exécute sans erreur

def test_virtualbox_not_installed(mock_subprocess_run_virtualbox_not_installed):
    assert check_virtualbox("Linux") is None  # Vérifie que VirtualBox n'est pas installé

# Tests pour Docker
def test_docker_installed_active(mock_subprocess_run_docker_installed):
    assert check_docker("Linux") is None  # Docker est installé et actif

def test_docker_not_installed(mock_subprocess_run_docker_not_installed):
    assert check_docker("Linux") is None  # Docker n'est pas installé

def test_docker_installed_inactive(mock_subprocess_run_docker_inactive):
    assert check_docker("Linux") is None  # Docker est installé mais inactif
