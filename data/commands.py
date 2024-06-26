# This file contains the nordvpn client commands and other relevant subprocess commands

import subprocess
import data.ascii_art as ascii_art
import data.country as country
from colorama import Fore, Style


def login():
    # Login to NordVPN
    subprocess.run(["nordvpn", "login"])


def quick_connect():
    # Connect to VPN
    subprocess.run(["nordvpn", "connect"])


def connect():
    # Connect to VPN through a specific country
    server_country = country.select_server_country()
    clear_screen()
    ascii_art.draw_logo()
    subprocess.run(["nordvpn", "connect", server_country])


def disconnect():
    # Disconnect from VPN and capture the output to truncate the second string where
    # it want's the user to rate the connection.
    disconnect_output = subprocess.run(["nordvpn", "disconnect"], capture_output=True, text=True)

    if "disconnected" in str(disconnect_output):
        print(f"{Fore.GREEN}You are disconnected from NordVPN.{Style.RESET_ALL}")
    else:
        print(Fore.GREEN + "You are not connected to NordVPN." + Style.RESET_ALL)


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