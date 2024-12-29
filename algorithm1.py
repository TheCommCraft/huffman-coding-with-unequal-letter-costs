import paramenters as param
import functions as fun

def k_prefix_code(graph,f):
    s = []
    v = {}
    codewords = fun.all_codewords(param.k)
    # caso f[0] > 0
    if f[0] > 0:
        af0 = param.letters[0]*f[0]
        s.append(af0)
        for l in graph:
            if l < 1: v[l] = 1
            else: break

    max_level = int((param.k-1)/param.epsilon)
    for i in range(1,max_level + 1):
        min_cost = 1 + (i - 1) * param.epsilon
        max_cost = 1 + i * param.epsilon

        # costruisco il vettore v
        for l in graph:
            # se il nodo è di livello i
            if l >= min_cost and l < max_cost:
                if l not in v: v[l] = 0
                for c in param.costs:
                    if l - c in codewords:
                        v[l] += vs(s,codewords[l - c])
        
        # aggiungo le codewords che rispettano i constraints
        l = 1 + i * param.epsilon - min(param.costs[0], param.epsilon)
        if v[l] < f[i] or f[i] == 0: print(l, "inconsistent")
        else:
            count = f[i]
            for c in codewords[l]:
                no_k_prefix = False
                for el in s:
                    if fun.k_prefix(el,c):
                        no_k_prefix = True
                        break
                if not no_k_prefix:
                    s.append(c)
                    count -= 1
                    if count == 0: 
                        break

            v[l] -= f[i]


    # se non ho abbastanza codewords aggiungo le codewords di costo minimo
    # tra quelle di costo >= k che non hanno prefissi di costo < k
    if len(s) < len(param.w):
        max_cost = param.k
        while len(s) < len(param.w):
            for c in codewords[max_cost]:
                no_k_prefix = False
                for el in s:
                    if fun.k_prefix(el,c):
                        no_k_prefix = True
                        break
                if not no_k_prefix:
                    s.append(c)
                    if len(s) >= len(param.w): break

            if len(s) < len(param.w):
                max_cost += param.costs[0]
                codewords[max_cost] = []
                fun.create_codewords(codewords[max_cost], max_cost)
    return s


def vs(set_s, strings):
    count = 0
    for s in strings:
        no_prefix = True
        for el in set_s:
            if fun.k_prefix(el, s):
                no_prefix = False
                break
        if no_prefix: count+=1
    return count