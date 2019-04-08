# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:22:48 2019

@author: huber.288
"""


class WordSearcher():
    def __init__(self):
        self._words = []
        self._puzzle = []

    def LoadPuzzle(self, puzzle):
        lines = puzzle.splitlines()
        self._words = lines[0].split(',')
        self._puzzle = [line.split(',') for line in lines[1:]]

    def solve(self):
        self._answers = {}
        self.SearchHorizontallyForwards()
        return self._answers

    def SearchHorizontallyForwards(self):
        for word in self._words:
            L = len(word)
            for lineN, line in enumerate(self._puzzle):
                LL = len(line)
                for startN, start in enumerate(line[:LL-L+1]):
                    for letterN in range(L):
                        if line[startN+letterN] != word[letterN]:
                            # Letter doesn't match
                            break
                        if letterN == L-1:  # Found full word
                            location = []
                            for i in range(L):
                                location.append((startN+i, lineN))
                            self._answers[word] = location