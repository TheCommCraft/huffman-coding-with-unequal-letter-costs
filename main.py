import math

import paramenters as param
import functions as fun
from algorithm1 import k_prefix_code
from algorithm2 import algorithm2


def compute_nodes(nodes = [], sum = 0):
    for c in param.costs:
        if sum + c <= param.k and sum + c not in nodes:
            nodes.append(sum + c)
            compute_nodes(nodes,sum + c)
        else: return

def compute_graph_D():
    nodes = [0]
    compute_nodes(nodes)
    graph = {}
    for i in nodes:
        graph[i] = []
    
    for i in graph:
        for j in graph:
            if j - i in param.costs:
                graph[i].append(j)
    return graph

def w_partition():
    groups = [[param.w[0]]]
    i = 1
    limit = (1 - param.freq[0]) * pow(param.epsilon, 2) / (2 * param.k)

    while(i < len(param.w) and param.freq[i] > limit):
        groups.append([param.w[i]])
        i += 1

    while (i < len(param.w)):
        sum = 0
        j = i
        groups.append([])
        while(j < len(param.w)):
            if sum + param.freq[j] <= 2 * limit:
                sum += param.freq[j]
                groups[len(groups) - 1].append(param.w[j])
                j += 1
            else: 
                break
        i = j
    return groups

def main():
    graph = compute_graph_D()

    groups = w_partition()

    f = [0] * (int((param.k-1)/param.epsilon) + 1)
    for i,g in enumerate(groups):
        if i == 0 and param.costs[0] < 1:
            # dimensione della massima parola di costo < 1
            q = math.floor(1 / param.costs[0])
            f[0] = q if i % param.costs[0] != 0 else q - 1
        else:
            f[i] = len(g)

    k_pref = k_prefix_code(graph,f)

    if not fun.check_prefix_free(k_pref):
        print("Codice non prefix-free, utilizzo dell'algoritmo 2")
        algorithm2(k_pref)

    code = {}
    for i,word in enumerate(param.w):
        code[word] = k_pref[i]
    return code




#genero le frequenze delle parole di w
param.freq = param.generate_freq(param.w)

#genero il codice di costo minimo
code = main()

#calcolo il costo del codice
total = 0
for c in code:
    total += fun.cost(code[c])
    print(c, ":",code[c],"-",fun.cost(code[c]))
print("Costo totale del codice:", fun.code_cost(code, param.w,param.freq))
mean = total / len(code)
print("Costo medio delle codewords:", mean)