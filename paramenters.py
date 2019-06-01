import string
import random
import numpy as np
def generate_freq(words):
    total = 0
    freq = []
    for w in words:
        new_f = random.randint(1,99)
        freq.append(new_f)
        total += new_f

    for i,f in enumerate(freq):
        freq[i] = f/total

    return freq


#insieme di lettere (words) da codificare e relative frequenze
# w =     ['a',   'b',    'c',    'd',    'e',    'f',    'g',    'h']
w = list(string.ascii_lowercase)
# w = [0] * 5000
freq =  [0.2,   0.18,   0.25,   0.01,   0.05,   0.14,   0.15,   0.02]



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