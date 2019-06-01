import numpy as np, numpy.random

def generate_prob(n):
    prob = []
    total = 0

    prob = np.random.dirichlet(np.ones(n)*100,size=1)[0]

    for p in prob:
        total += p
    for (i,p) in enumerate(prob):
        prob[i] = p/total

    for p in prob:
        total += p

    print(total)
    
generate_prob(26)