import re
import sys


def main():
    prev_line_no = None
    for line in sys.stdin:
        line = line[:-1]
        tokens = line.split(' ')
        text = ''.join(tokens)
        text = text.replace('_', ' ')
        print(text)
if __name__ == '__main__':
    main()
