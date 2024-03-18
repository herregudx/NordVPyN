import subprocess
import ascii_art
from sys import exit


def main():
    check_if_nordvpn_is_installed()
    show_basic_menu()


def login():
    # Login to NordVPN
    subprocess.run(["nordvpn", "login"])


def connect():
    # Connect to VPN
    subprocess.run(["nordvpn", "connect"])


def disconnect():
    # Disconnect from VPN
    output = subprocess.run(["nordvpn", "disconnect"])


def show_status():
    # Show status of VPN connection
    subprocess.run(["nordvpn", "status"])


def show_account_info():
    # Show account info
    subprocess.run(["nordvpn", "account"])


def show_settings():
    # Show settings
    subprocess.run(["nordvpn", "settings"])


def show_version():
    # Show NordVPN version
    subprocess.run(["nordvpn", "version"])


def clear_screen():
    # Clear the screen to keep it tidy
    subprocess.run(["clear"])


def check_if_nordvpn_is_installed():
    # Simple check to see if NordVPN is installed
    try:
        subprocess.run(["nordvpn", "-v"], stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("\nFailed to execute NordVPN binary. Are you sure it's installed?\n")
        print("Visit https://nordvpn.com/download/linux/ to download and install it.")
        print("If you are on a Debian based distro, you could try running: sudo apt-get install nordvpn\n")
        exit()


def show_basic_menu():
    clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[C]onnect, [D]isconnect, [S]tatus, [M]ore, [Q]uit: ")
        clear_screen()
        ascii_art.draw_logo()
        if menu_choice.upper() == "C":
            connect()
        elif menu_choice.upper() == "D":
            disconnect()
        if menu_choice.upper() == "S":
            show_status()
        elif menu_choice.upper() == "M":
            show_advanced_menu()
        elif menu_choice.upper() == "Q":
            exit()


def show_advanced_menu():
    clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with more advanced choices
    while True:
        menu_choice = input("\n[L]ogin, [A]ccount, [S]ettings, [V]ersion, [B]ack: ")
        clear_screen()
        ascii_art.draw_logo()
        if menu_choice.upper() == "L":
            login()
        elif menu_choice.upper() == "A":
            show_account_info()
        elif menu_choice.upper() == "S":
            show_settings()
        elif menu_choice.upper() == "V":
            show_version()
        elif menu_choice.upper() == "B":
            show_basic_menu()


# Call main if not a module.
if __name__=="__main__": 
    main()