# Save and read user settings to and from a configuration file. Work in progress.

import configparser
 
 
def save_config():
    config = configparser.ConfigParser()
 
    # Add sections and key-value pairs
    config['General'] = {'server_country': "Default", 'ipv6': 'disabled'}
 
    # Write the configuration to a file
    with open('data/config.ini', 'w') as configfile:
        config.write(configfile)
    
    print("Configuration saved.")


def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()
 
    # Read the configuration file
    config.read('data/config.ini')
 
    # Access values from the configuration file
    server_country = config.get('General', 'server_country')
    ipv6_setting = config.get('General', 'ipv6')

    # Return a dictionary with the retrieved values
    config_values = {
        'server_country': server_country,
        'ipv6_setting': ipv6_setting,
    }
 
    return config_values
 
 
if __name__ == "__main__":
    save_config()
    print(read_config())


