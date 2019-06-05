import paramenters as param

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
    b = param.letters[1]
    prefix = "aba"

    suffix = code.replace(prefix,'')
    i = 0
    for s in suffix:
        if s == b: i+=1
    print(prefix,enc(i), suffix)
    new = prefix + enc(i) + suffix + b
    return new