import os.path

# CONF = config.get_conf_dict()
homedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# base_dir = CONF['general']['base_directory']
base_dir = "."

def get_base_dir():
    return os.path.abspath(os.path.join(homedir, base_dir))