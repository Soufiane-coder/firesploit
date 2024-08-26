import firebase
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils import init_firebase


with open('/usr/share/wordlists/amass/all.txt' , 'r') as wordlistfile:
    lines = wordlistfile.readlines()

wordlist = [line.strip() for line in lines]
wordlist_length = len(wordlist)

def spoit(args):
    storage = init_firebase(args.input)
    found = []

    for index, word in enumerate(wordlist):
        print(f'{(100 * (index + 1) / wordlist_length):.4f}%', end='\r')
        try:
            storage.collection(word).get()
            found.append(word)
            print('\n', word)
        except Exception as e:
            # print(f"error {e}")
            pass
    print(found)



def splash():

    print(r"""   
                 _____ _                     _       _ _   
                |  ___(_)_ __ ___  ___ _ __ | | ___ (_) |_ 
                | |_  | | '__/ _ \/ __| '_ \| |/ _ \| | __|
                |  _| | | | |  __/\__ \ |_) | | (_) | | |_ 
                |_|   |_|_|  \___||___/ .__/|_|\___/|_|\__|
                                      |_|                  
                                                                                                         
                """)
