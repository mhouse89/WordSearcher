# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:29:41 2019

@author: huber.288
"""

import sys
from WordSearcher import WordSearcher

def main():
    if len(sys.argv)<2:
        file = 'Puzzle1.txt'
    else:
        file = sys.argv[1]
    WS = WordSearcher()
    WS.LoadFromFile(file)
    WS.solve()
    output = WS.Output()
    print(output)

if __name__ == "__main__":
    main()