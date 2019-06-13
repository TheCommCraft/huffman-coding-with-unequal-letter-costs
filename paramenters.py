import string
import random
import numpy as np

# generare n frequenze crescenti che sommano a 1
def generate_freq(words):
    total = round(len(words) * (len(words) + 1) / 2)
    freq = []
    prova = 0
    for i in range(len(words)):
        freq.append((len(words) - i) / total)
        prova += (len(words) - i) / total

    return freq

#insieme di lettere (words) da codificare e relative frequenze
w = list(string.ascii_lowercase)


#lettere dell'alfabeto che formano le codewords e relativi costi
letters =   ['a',   'b',    'c']
costs =     [0.5,     1 ,     4]
epsilon = 2

k = 9