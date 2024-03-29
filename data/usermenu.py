# This file contains the menu the user can interact with

import data.ascii_art as ascii_art
import data.commands as commands
import data.config as config


def show_basic_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[1]:Connect, [2]:Disconnect, [3]:Status, [4]:More, [0]:Quit: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice == "1":
            commands.connect(config.server_country)
        elif menu_choice == "2":
            commands.disconnect()
        elif menu_choice == "3":
            commands.show_status()
        elif menu_choice == "4":
            show_advanced_menu()
        elif menu_choice == "0":
            exit()


def show_advanced_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with more advanced choices
    while True:
        menu_choice = input("\n[1]:Account, [2]:Settings, [3]:Config, [4]:Version, [9]:Back: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice == "1":
            commands.show_account_info()
        elif menu_choice == "2":
            commands.show_settings()
        elif menu_choice == "3":
            show_config_menu()
        elif menu_choice == "4":
            commands.show_version()
        elif menu_choice == "9":
            show_basic_menu()


def show_config_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[1]:Login, [2]:Country, [9]:Back: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice == "1":
            commands.login()
        elif menu_choice == "2":
            commands.set_server_country()
        elif menu_choice == "9":
            show_basic_menu()