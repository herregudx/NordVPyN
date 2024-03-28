# This file contains the nordvpn client commands and other relevant subprocess commands

import subprocess


def login():
    # Login to NordVPN
    subprocess.run(["nordvpn", "login"])


def connect(server_country):
    # Connect to VPN
    if server_country != "":
        subprocess.run(["nordvpn", "connect", server_country])
    else:
        subprocess.run(["nordvpn", "connect"])


def disconnect():
    # Disconnect from VPN
    subprocess.run(["nordvpn", "disconnect"])


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