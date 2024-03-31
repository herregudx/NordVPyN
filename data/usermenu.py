# This file contains the menu the user can interact with

import data.ascii_art as ascii_art
import data.commands as commands


def show_basic_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with choices
    while True:
        menu_choice = input("\n[1]:Quick-connect, [2]:Connect, [3]:Disconnect, [4]:Status, [9]:More, [0]:Quit: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice == "1":
            commands.quick_connect()
        elif menu_choice == "2":
            commands.connect()
        elif menu_choice == "3":
            commands.disconnect()
        elif menu_choice == "4":
            commands.show_status()
        elif menu_choice == "9":
            show_advanced_menu()
        elif menu_choice == "0":
            exit()


def show_advanced_menu():
    commands.clear_screen()
    ascii_art.draw_logo()
    # Show the user a menu with more advanced choices
    while True:
        menu_choice = input("\n[1]:Login, [2]:Settings, [3]:Account, [4]:Version, [9]:Back, [0]Quit: ")
        commands.clear_screen()
        ascii_art.draw_logo()
        if menu_choice == "1":
            commands.login()
        elif menu_choice == "2":
            commands.show_settings()
        elif menu_choice == "3":
            commands.show_account_info()
        elif menu_choice == "4":
            commands.show_version()
        elif menu_choice == "9":
            show_basic_menu()
        elif menu_choice == "0":
            exit()
