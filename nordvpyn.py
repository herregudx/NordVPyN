import subprocess
from sys import exit


def login():
    # Login to NordVPN
    subprocess.run(["nordvpn", "login"])


def connect():
    # Connect to VPN
    subprocess.run(["nordvpn", "connect"])


def status():
    # Show status of VPN connection
    subprocess.run(["nordvpn", "status"])


def disconnect():
    # Disconnect from VPN
    subprocess.run(["nordvpn", "disconnect"])


def clear_screen():
    # Clear the screen to keep it tidy
    subprocess.run(["clear"])


def check_if_nordvpn_is_installed():
    # Simple check to see if NordVPN is installed
    try:
        installed = subprocess.run("nordvpn", stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("\nFailed to execute NordVPN binary. Are you sure it's installed?\n")
        exit()


def main():
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[C]onnect, [D]isconnect, [S]tatus, [L]ogin, [Q]uit: ")
        clear_screen()
        if menu_choice.upper() == "C":
            connect()
        elif menu_choice.upper() == "D":
            disconnect()
        if menu_choice.upper() == "S":
            status()
        elif menu_choice.upper() == "L":
            login()
        elif menu_choice.upper() == "Q":
            exit()


# Call main if not a module.
if __name__=="__main__": 
    check_if_nordvpn_is_installed()
    main()
