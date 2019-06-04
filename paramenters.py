import string
import random
import numpy as np

# generare n frequenze crescenti
def generate_freq(words):
    total = round(len(words) * (len(words) + 1) / 2)
    count = 0
    freq = []
    prova = 0
    for i in range(len(words)):
        freq.append((len(words) - i) / total)
        prova += (len(words) - i) / total

    return freq


#insieme di lettere (words) da codificare e relative frequenze
# w =     ['a',   'b',    'c',    'd',    'e',    'f',    'g',    'h']
w = list(string.ascii_lowercase)

# freq =  [0.2,   0.18,   0.25,   0.01,   0.05,   0.14,   0.15,   0.02]



'''
- l1 <= l2 <= l3 ... <= lr
ASSUMPTION 1.
each li for i >= 2 is an integer multiple of epsilon
l2 equals 1
epsilon is either an integer multiple of l1 or evenly divides l1
all codeword costs are integer multiples of min{ l1, epsilon }
'''
#lettere dell'alfabeto che formano le codewords e relativi costi
letters =   ['a',   'b',    'c']
costs =     [0.5,     1 ,     4]
epsilon = 2


'''
choose k = theta(log(1/epsilon)/epsilon)
so k - 1 is a multiple of epsilon
'''
k = 9