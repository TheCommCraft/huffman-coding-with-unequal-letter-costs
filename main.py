import paramenters as param
import functions as fun
from k_prefix_code import k_prefix_code



'''
a tuple f = (f(0), . . . , f((k - 1)/epsilon)) o integers
if f(0) =  0, then there must be no codeword in level 0
'''
#f = (0,10,10,10,10)


'''
Ogni nodo è un possibile costo di codeword compreso tra 0,k
Quindi tutte le possibili somme degli elementi di costs minori di k
C'è un arco da i a j se j - i è un valore in costs
'''
graph = {}




def compute_nodes(nodes = [], sum = 0):
    for c in param.costs:
        if sum + c <= param.k and sum + c not in nodes:
            nodes.append(sum + c)
            compute_nodes(nodes,sum + c)
        else: return



def compute_graph_D():
    nodes = [0]
    compute_nodes(nodes)

    for i in nodes:
        graph[i] = []
    
    for i in graph:
        for j in graph:
            if j - i in param.costs:
                graph[i].append(j)



def w_partition():
    groups = [[param.w[0]]]
    i = 1
    limit = (1 - param.freq[0]) * pow(param.epsilon, 2) / (2 * param.k)
    print(limit)
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
                print("break")
                break
        i = j

    return groups




# compute_graph_D()
# k_pref = k_prefix_code(graph,[10,1,1,1,1])

# code_cost = 0
# for k in k_pref:
#     code_cost += fun.cost(k)
#     print(k,fun.cost(k))
# print(code_cost)


param.freq = param.generate_freq(param.w)
groups = w_partition()
print(groups)