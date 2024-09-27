import pytest
import platform
from os_detector import detect_os

@pytest.fixture
def mock_platform_system(monkeypatch):
    def mock_system(os_name):
        monkeypatch.setattr(platform, "system", lambda: os_name)
    return mock_system

def test_detect_linux(mock_platform_system):
    mock_platform_system("Linux")
    assert detect_os() == "Linux"

def test_detect_mac(mock_platform_system):
    mock_platform_system("Darwin")
    assert detect_os() == "macOS"

def test_detect_windows(mock_platform_system):
    mock_platform_system("Windows")
    assert detect_os() == "Windows"

def test_unsupported_os(mock_platform_system):
    mock_platform_system("Solaris")
    assert detect_os() is None
