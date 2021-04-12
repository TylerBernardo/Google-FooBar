def solution(l):
    output = "0"
    lSum = sum(l)
    re = lSum % 3
    l.sort()
    remains = []
    for index in range(len(l)):
        remain = l[index] % 3
        if(remain != 0):
            remains.append([remain, l[index]])
    removed = False
    for i in range(len(remains)):
        if remains[i][0] == re: #and fTwo > remains[i][1]:
            del l[l.index(remains[i][1])]
            removed = True
            break
    if removed == False and re != 0:
        for i in range(2):
            del l[l.index(remains[0][1])]
            del remains[0]
    for index in range(len(l)):
        output += str(l[(len(l) - 1) - index])
    return int(output)