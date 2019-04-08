# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:22:48 2019

@author: huber.288
"""


class WordSearcher():
    def __init__(self):
        self._words = []
        self._puzzle = []
        self._RotationState = 0

    def LoadPuzzle(self, puzzle):
        lines = puzzle.splitlines()
        self._words = lines[0].split(',')
        self._puzzle = [line.split(',') for line in lines[1:]]

    def solve(self):
        self._answers = {}
        for word in self._words:
            for _ in range(4):  # Try to find horizontally in each rotation
                location = self.SearchHorizontallyForwards(word)
                if location:  # Found it
                    for _ in range(self._RotationState):
                        location = RotateCoordinates(location, len(self._puzzle))
                    self._answers[word] = location
                    break
                location = self.SearchDiagonallyDownForward(word)
                if location:  # Found it
                    for _ in range(self._RotationState):
                        location = RotateCoordinates(location, len(self._puzzle))
                    self._answers[word] = location
                    break
                self.RotatePuzzle()
        while self._RotationState != 0:  # Rotate back to orignal state after done
            self.RotatePuzzle()
        return self._answers

    def SearchHorizontallyForwards(self, word):
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
                        return location
        return []  # If it exits loop, it didn't find it

    def SearchDiagonallyDownForward(self, word):
        L = len(word)
        for lineN, line in enumerate(self._puzzle):
            LL = len(line)
            for startN, start in enumerate(line[:LL-L+1]):
                for letterN in range(L):
                    current_line = lineN+letterN
                    current_letter = startN+letterN
                    if current_line >= len(self._puzzle) or \
                       self._puzzle[current_line][current_letter] != word[letterN]:
                        # Letter doesn't match
                        break
                    if letterN == L-1:  # Found full word
                        location = []
                        for i in range(L):
                            location.append((startN+i, lineN+i))
                        return location
        return []  # If it exits loop, it didn't find it

    def RotatePuzzle(self):
        '''Rotates puzzle 90 degrees clockwise, so that I can use
        SearchHoizontallyForwards to find all horizontal and vertical words'''
        pr = list(zip(*self._puzzle[::-1]))
        self._puzzle = [list(line) for line in pr]
        self._RotationState = (self._RotationState + 1) % 4
        # Update rotation state, which will be used to calculate unrotated locations


def RotateCoordinates(location,puzzle_width):
    '''Coordinates in rotated puzzle must be
    translated to unrotated coordinates'''
    return [(loc[1], puzzle_width-1-loc[0]) for loc in location]
