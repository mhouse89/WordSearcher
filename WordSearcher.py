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
