# main.py
from os_detector import detect_os
from service_checker import check_virtualbox, check_docker


def main():
    os_type = detect_os()

    if os_type:
        check_virtualbox(os_type)
        check_docker(os_type)


if __name__ == "__main__":
    main()
