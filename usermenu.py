# This file contains the menu the user can interact with

import ascii_art
import commands
import country


# Variable to specify which country to connect to. This string can be left empty
# to let the nordvpn-client select automatically.
server_country = ""


def show_basic_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[C]onnect, [D]isconnect, [S]tatus, [M]ore, [Q]uit: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice.upper() == "C":
            commands.connect(server_country)
        elif menu_choice.upper() == "D":
            commands.disconnect()
        elif menu_choice.upper() == "S":
            commands.show_status()
        elif menu_choice.upper() == "M":
            show_advanced_menu()
        elif menu_choice.upper() == "Q":
            exit()


def show_advanced_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with more advanced choices
    while True:
        menu_choice = input("\n[A]ccount, [S]ettings, [C]onfig, [V]ersion, [B]ack: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice.upper() == "A":
            commands.show_account_info()
        elif menu_choice.upper() == "S":
            commands.show_settings()
        elif menu_choice.upper() == "C":
            show_config_menu()
        elif menu_choice.upper() == "V":
            commands.show_version()
        elif menu_choice.upper() == "B":
            show_basic_menu()


def show_config_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[L]ogin, [C]ountry, [B]ack: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice.upper() == "L":
            commands.login()
        elif menu_choice.upper() == "C":
            set_server_country()
        elif menu_choice.upper() == "B":
            show_basic_menu()


def set_server_country():
    # Attempts to set the server_country variable
    global server_country
    server_country = country.select_server_country()
