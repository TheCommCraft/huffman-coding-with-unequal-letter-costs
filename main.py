import paramenters as param
import functions as fun
from algorithm1 import k_prefix_code
import algorithm2 as a2


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
    print("Creazione grafo")
    graph = compute_graph_D()

    print("Partizione di w")
    groups = w_partition()

    print("Creazione dei vincoli f")
    f = [0] * (int((param.k-1)/param.epsilon) + 1)
    for i,g in enumerate(groups):
        f[i] = len(g)
    print("Creazione k-prefix code")
    k_pref = k_prefix_code(graph,f)

    print("Creazione codice ottimo")
    code = {}
    for i,word in enumerate(param.w):
        code[word] = k_pref[i]
    return code



param.freq = param.generate_freq(param.w)
code = main()

print(code,fun.code_cost(code, param.w,param.freq))