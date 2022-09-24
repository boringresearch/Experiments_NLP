#!/usr/bin/python

import sys, getopt
from jiwer import wer

def main(argv):
    predfile = ''
    gocfile = ''
    try:
        opts, args = getopt.getopt(argv,"hp:l:",["pred=","label="])
    except getopt.GetoptError:
        print('test.py -i <predfile> -o <gocfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <predfile> -o <gocfile>')
            sys.exit()
        elif opt in ("-p", "--pred"):
            predfile = arg
        elif opt in ("-l", "--label"):
            gocfile = arg
    print('Pred file is "', predfile)
    print('Label file is "', gocfile)

    with open(predfile,'r') as f, open(gocfile,'r') as g:
        pred = f.readlines()
        goc = g.readlines()
    
    error = wer(pred, goc)
    print("WER:", error)

if __name__ == "__main__":
   main(sys.argv[1:])
