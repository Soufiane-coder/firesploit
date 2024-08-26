import json
import firebase

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