# test_main.py
import pytest
from unittest.mock import patch
from main import create_vm, create_docker_container
import subprocess  # Ajoutez cette ligne pour importer le module subprocess

@patch('subprocess.run')
def test_create_vm_success(mock_run):
    mock_run.return_value.returncode = 0  # Simuler une réussite
    assert create_vm() is True  # Vérifier le succès

@patch('subprocess.run')
def test_create_vm_failure(mock_run):
    mock_run.side_effect = subprocess.CalledProcessError(1, 'VBoxManage')  # Simuler une échec
    assert create_vm() is False  # Vérifier l'échec

@patch('subprocess.run')
def test_create_docker_container_success(mock_run):
    mock_run.return_value.returncode = 0  # Simuler une réussite
    with patch('builtins.input', side_effect=["Ubuntu", "non"]):
        assert create_docker_container() is True  # Vérifier le succès

@patch('subprocess.run')
def test_create_docker_container_failure(mock_run):
    mock_run.side_effect = subprocess.CalledProcessError(1, 'docker')  # Simuler une échec
    with patch('builtins.input', side_effect=["Ubuntu", "non"]):
        assert create_docker_container() is False  # Vérifier l'échec
