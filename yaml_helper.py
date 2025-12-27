from ruamel.yaml import YAML

def load_yaml(file_path, typ=None):
    yaml = YAML(typ=typ)
    with open(file_path, 'r') as file:
        data = yaml.load(file)
    return data
def save_yaml(data, file_path):
    yaml = YAML()
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
