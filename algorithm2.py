import paramenters as param
import functions as fun

def enc(i):
    if i == 0: return "ab"
    binary = "{0:b}".format(i)
    b = binary.replace("0",param.letters[0]).replace("1",param.letters[1])
    e = ""
    for j in b:
        e += j + j
    e += "ab"
    return e

def algorithm2(code):
    for j,c in enumerate(code):
        b = param.letters[1]
        prefix = ""
        for l in c:
            prefix += l
            if fun.cost(prefix) >= param.k: break

        suffix = c.replace(prefix,'')
        i = 0
        for s in suffix:
            if s == b: i+=1

        new = prefix + enc(i) + suffix + b
        code[j] = new