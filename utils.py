import json
import firebase
import csv
from pathlib import Path
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def init_firebase(json_path):
    with open(json_path, 'r') as file:
        conf = json.load(file)

    # conf['databaseURL'] = conf.get('databaseURL', "")
    if (not 'databaseURL' in conf.keys()):
        conf['databaseURL'] = ""

    app = firebase.initialize_app(conf)
    storage = app.firestore()
    return storage

def print_collection(storage, path):
    data = storage.collection(path).get()
    for item in data:
        for key, value in item.items():
            print(f'''
    {bcolors.OKGREEN}The uid : {bcolors.ENDC}{key}
    {bcolors.OKBLUE}Other info : {bcolors.ENDC}{value}''')
            
def save_result_csv(col_name, root, ids, data, write_path : Path):
    all_keys = set()
    for entry in data:
        all_keys.update(entry.keys())

    all_keys.add('id_firesploit_obj')

    parent_path = write_path / root

    parent_path.mkdir(parents=True, exist_ok=True)

    csv_file = parent_path / f'{col_name}.csv'

    with open(csv_file , mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=all_keys)

        writer.writeheader()

        for idx, row in enumerate(data):
            row['id_firesploit_obj'] = ids[idx]
            writer.writerow(row)

def check_deepth(value):
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(f'Invalid value: {ivalue} must be more than 0')
    return ivalue

def check_path(value):
    path = Path(str(value))
    if not path.exists():
        raise argparse.ArgumentTypeError(f'Invalid value: {value} there is no suck path')
    return path

def check_file_json(file_path):
    path = Path(file_path)
    
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"The file '{file_path}' does not exist.")
    
    # Check if the file has a .json extension
    if not path.suffix == '.json':
        raise argparse.ArgumentTypeError(f"The file '{file_path}' is not a .json file.")
    
    return path

def check_file(file_path):
    path = Path(file_path)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"The file '{file_path}' does not exist.")
    return path