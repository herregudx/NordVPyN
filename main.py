# Check that the nordvpn client is installed and launch the menu

import data.commands as commands
import data.usermenu as usermenu


def main():
    commands.check_if_nordvpn_is_installed()
    usermenu.show_basic_menu()


# Call main if not a module.
if __name__ == "__main__": 
    main()