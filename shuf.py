#!/usr/local/cs/bin/python3

import random, sys, argparse

"""Python 3 Script that Implements the GNU shuf command with same arguments"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin)
    parser.add_argument('--echo','-e', type=str, nargs='+')
    parser.add_argument('--input-range', '-i', type=str)
    parser.add_argument('--head-count', '-n', type=int)
    parser.add_argument('--repeat', '-r', action='store_true')
    args = parser.parse_args()

        
    if(args.echo):
        lines = args.echo

    numCount = -1
    if(args.head_count):
        numCount = args.head_count

    if(args.input_range):
        if(args.echo):
            sys.stderr.write("ERROR: Echo and Input-Range options cannot be used together\n")
            return

        beforeDash = True
        firstNum = ""
        secNum = ""
        for element in args.input_range:
            if(element == '-'):
                beforeDash = False
                continue
            if(beforeDash):
                firstNum += element
            else:
                secNum += element
        
        firstNum = int(firstNum)
        secNum = int(secNum)
        if(firstNum > secNum):
            sys.stderr.write("ERROR: Range Invalid\n")
            return

        lines = list(range(firstNum, secNum+1))
        

    if(not args.echo and not args.input_range):
        try:
            lines = args.file.read().split()
        except:
            sys.stderr.write("ERROR: File Invalid")


    random.shuffle(lines)
    

    if(args.repeat):
        x = 0
        while x != numCount:
            print(random.choice(lines))
            x += 1
    else:
        if(args.head_count):
            i = 0
            while i < numCount and i < len(lines):
                print(lines[i])
                i += 1
        else:
            for element in lines:
                print(element)

    

if __name__ == "__main__":
    main()
