# This file contain global variables with user configurations and functions to save and read 
# from a CSV configuration file.

import pickle

def init():
    # Variable to specify which country to connect to. This string can be left empty
    # to let the nordvpn-client select automatically.
    global server_country
    server_country = "Default"

    # IPv6
    global ipv6_setting
    ipv6_setting = "disabled"

    # Threat Protection Lite
    global threat_protection_setting
    threat_protection_setting = "disabled"


def save_config():
    # TODO
    print("N/A")


def read_config():
    # TODO
    print("N/A")
