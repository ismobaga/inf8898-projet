

def generateIndex(p, n):
    result = []
    lastIdx = 0
    if len(p):
        lastIdx = p[-1]
    for i in range(lastIdx+1, n):
        if i : 
            tmp = [p + [i]]
            result += tmp
            if len(tmp[0]) < n:
                result += generateIndex(tmp[0], n)
        else:
            result += [[]]

    return result

def getAP(indexes, elts, i):
    idx = [0] + indexes[i] + [None]
    return [
        elts[idx[j]:idx[j+1]] for j in range((len(idx) - 1)) 
    ]

# while True:
#     i = int(input("Size : "))
#     idxes = [[]] + generateIndex([], i)
#     print("La tialle est de : ", len(idxes))


elts = list(range(4))
idxes = [[]] + generateIndex([], len(elts))
while True:
    print("-"*20)
    print("Elements", elts)
    
    print("idxes:" , idxes)

    i = int(input("Gimme i : "))
    p = getAP(idxes, elts, i)

    print(f"P[{i}] : {p}")

