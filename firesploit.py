import firebase
import json


def spoit(args):
    with open(args.input, 'r') as file:
        conf = json.load(file)

    # conf['databaseURL'] = conf.get('databaseURL', "")
    if (not 'databaseURL' in conf.keys()):
        conf['databaseURL'] = ""

    app = firebase.initialize_app(conf)
    storage = app.firestore()

    users = storage.collection('users').get()


def splash():

    print(r"""   
                 _____ _                     _       _ _   
                |  ___(_)_ __ ___  ___ _ __ | | ___ (_) |_ 
                | |_  | | '__/ _ \/ __| '_ \| |/ _ \| | __|
                |  _| | | | |  __/\__ \ |_) | | (_) | | |_ 
                |_|   |_|_|  \___||___/ .__/|_|\___/|_|\__|
                                      |_|                  
                                                                                                         
                """)
