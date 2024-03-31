# This file contains all functions related to server country selection

import subprocess


def select_server_country():
    # Let the user select which country to connect to and verify that the server exists.
    valid_country = False
    while valid_country == False:
        chosen_country = input("\nSpecify country (type 'list' to show available choices): ").title()
        if chosen_country.lower() == "list":
            subprocess.run(["nordvpn", "countries"])
        elif verify_country(chosen_country) == True:
            valid_country = True
            return chosen_country


def extract_countries(data):
    # The output from "nordvpn countries" is a mess, this function attempts to make it tidy.
    # Iterate through the given list data and extract the country names.
    countries = []
    for item in data:
        if item.strip() and not item.startswith('-') and not item.startswith('\n'):
            countries.extend(part.strip() for part in item.split('\t'))
    
    # Remove empty elements using a list comprehension.
    countries = [element for element in countries if element.strip()]

    return countries


def verify_country(name_of_country):
    # Check that the country exists among the listed countries of the 
    # command "nordvpn countries" to prevent typos or trying to set a
    # country that's not available.
    countries_output = subprocess.Popen(["nordvpn", "countries"], stdout=subprocess.PIPE, text=True).stdout.readlines()

    list_of_countries = extract_countries(countries_output)

    if name_of_country in list_of_countries:
        return True
    else:
        return False
