# This file contain global variables with user configurations and functions to save and read 
# from a CSV configuration file.

import csv

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
    with open('data/config.csv', 'w', newline='') as csvfile:
        fieldnames = ['setting', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'setting': 'server_country', 'value': server_country})
        writer.writerow({'setting': 'ipv6_setting', 'value': ipv6_setting})
        writer.writerow({'setting': 'threat_protection_setting', 'value': threat_protection_setting})
    print("Configuration file saved.")


def read_config():
    # TODO: This function should read config from file and import it.
    return 0
