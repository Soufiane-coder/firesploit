from firesploit import splash, spoit
import argparse


def main(args):
    splash()
    spoit(args)
    # rest of the code


parser = argparse.ArgumentParser(
    description='Process some command-line arguments.')

# Add arguments
parser.add_argument('input', nargs='?',
                    help='config file json', default="./config.json")
parser.add_argument(
    '-o', '--output', help='Output file path', default='output.txt')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Increase verbosity')

# Parse arguments
args = parser.parse_args()

if __name__ == '__main__':
    main(args)
