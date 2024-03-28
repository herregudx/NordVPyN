import subprocess
import usermenu
from sys import exit


def main():
    check_if_nordvpn_is_installed()
    usermenu.show_basic_menu()


def check_if_nordvpn_is_installed():
    # Simple check to see if NordVPN is installed
    try:
        subprocess.run(["nordvpn", "-v"], stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("\nFailed to execute NordVPN binary. Are you sure it's installed?\n")
        print("Visit https://nordvpn.com/download/linux/ to download and install it.")
        print("If you are on a Debian based distro, you could try running: sudo apt-get install nordvpn\n")
        exit()


# Call main if not a module.
if __name__=="__main__": 
    main()