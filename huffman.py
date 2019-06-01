import string

# alphabet = list(string.ascii_lowercase)

# prob = list()
# print(alphabet)


alphabet = ['a','b','c','d','e','f']
prob = [0.7,0.05,0.025,0.02,0.05,0.2]
code = []

def merge_smallest(tmpA,tmpP):
    smallest_index_1 = tmpP.index(min(tmpP))
    new_simbol = tmpA[smallest_index_1]
    new_prob = tmpP[smallest_index_1]
    del tmpA[smallest_index_1]
    del tmpP[smallest_index_1]

    smallest_index_2 = tmpP.index(min(tmpP))
    new_simbol += tmpA[smallest_index_2]
    new_prob += tmpP[smallest_index_2]
    del tmpA[smallest_index_2]
    del tmpP[smallest_index_2]
    tmpA.append(new_simbol)
    tmpP.append(new_prob)


def huffman(a, p):
    tmpA = a.copy()
    tmpP = p.copy()

    if len(tmpA) > 2:
        merge_smallest(tmpA, tmpP)
        tmpC = huffman(tmpA,tmpP)
        code = []
        split = []
        for c in tmpC:
            if c[1] in a:
                code.append(c)
            else:
                split.append(c)
        next_code = 0
        for l in a:
            for s in split:
                if l in s[1]:
                    code.append([s[0] + str(next_code), l])
                    next_code+=1

        print("tmpA", tmpA)
        print("tmpC", tmpC)
        print("split",split)
        print("code",code)
        print()
        return code
    else: 
        return [
        ["0",tmpA[0]],
        ["1",tmpA[1]]
        ]
    
def mean_length(code,prob):
    return None

print("final code",huffman(alphabet,prob))
