from pathlib import Path
from utils import init_firebase , save_result_csv
import threading


def verify_col(storage , path, root, write_path):
    try:
        data = storage.collection(root + path + '/').get()
    except Exception as e:
        # print(f"error {e}")
        return False
    ids = [list(obj.keys())[0] for obj in data]
    data = [list(obj.values())[0] for obj in data]
    save_result_csv(path, root, ids, data, write_path)
    return (root + path, ids)
    
def loop_over(storage, args, root='', wordlist=[]):
    wordlist_length = len(wordlist)
    for index, word in enumerate(wordlist):
        # test the word if it is in the path for the root='' the path would be just f'word'
        print(f'{(100 * (index + 1) / wordlist_length):.4f}%', end='\r')
        result = verify_col(storage, word, root, args.output)
        # if there is the collection, loop over the new path of each document
        if(result):
            # deepth = queue_deepth.get()
            threads = []

            current_depth = int(f'{result[0]}/id/'.count('/') / 2)
        
            if(args.depth != None and current_depth > args.depth):
                return

            for id in result[1]:
                thread = threading.Thread(target=loop_over, args=(storage,args, f'{result[0]}/{id}/', wordlist))
                threads.append(thread)
                thread.start()
                print(f'{result[0]}/{id}/')

            # This script will slow the program so each document will be scanned before goind to other
            if(not args.aggressive):
                for thread in threads:
                    thread.join()


def spoit(args):
    if(args.aggressive):
        print('Aggressive mode')
    storage = init_firebase(args.input[0])
    with open(args.wordlist , 'r') as wordlist_file:
        lines = wordlist_file.readlines()

    wordlist = [line.strip() for line in lines]
    #wordlist = ['user', 'users', 'somethin', 'else', 'to', 'search', 'for', 'routines', 'times' , 'reports', 'statistics']
    
    loop_over(storage, args, wordlist=wordlist)


def splash():

    print(r"""   
                 _____ _                     _       _ _   
                |  ___(_)_ __ ___  ___ _ __ | | ___ (_) |_ 
                | |_  | | '__/ _ \/ __| '_ \| |/ _ \| | __|
                |  _| | | | |  __/\__ \ |_) | | (_) | | |_ 
                |_|   |_|_|  \___||___/ .__/|_|\___/|_|\__|
                                      |_|                  
                                                                                                         
                """)
