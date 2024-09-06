from firesploit import splash, spoit
import argparse
import time
from utils import check_deepth, check_path, check_file, check_file_json

def main(args):
    splash()
    spoit(args)
    # rest of the code


parser = argparse.ArgumentParser(
    description='Process some command-line arguments.')

# Add arguments
parser.add_argument('input', nargs=1, type=check_file_json,
                    help='Path to the config file in JSON format', default="./config.json")

parser.add_argument(
    '-o', '--output', type=check_path ,help='Write the path directory to save data collected default current directory', default='.')

parser.add_argument(
    '-d', '--depth', type=check_deepth, help='The deepth of scanning min=0 (scann the first docs) default=infinit', default=None)

parser.add_argument(
    '-w', '--wordlist', type=check_file, help='The deepth of scanning min=0 (scann the first docs) default=infinit',
    default='/usr/share/wordlists/amass/all.txt')

parser.add_argument(
    '-a', '--aggressive', action='store_true', help='Enable aggressive mode',
    default=False)


# Parse arguments
args = parser.parse_args()

if __name__ == '__main__':
    main(args)
