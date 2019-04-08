# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:18:08 2019

@author: huber.288
"""
# =============================================================================
# word='SCOTTY'
# word2=['S','C','O','T','T','Y']
# print(word==word2)
# L=len(word)
# for lineN, line in enumerate(p):
#     LL=len(line)
#     for startN, start in enumerate(line[:LL-L+1]):
#         for letterN in range(L):
#             if line[startN+letterN] != word[letterN]:  # Letter doesn't match
#                 break
#             if letterN == L-1:  # Found full word
#                 loc = []
#                 for i in range(L):
#                     loc.append((startN+i, lineN))
#                 print(loc)
# =============================================================================

pr = list(zip(*p[::-1]))
pr = [list(line) for line in pr]
