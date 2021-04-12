def solution(x, y):
    gens = 0
    x = int(x)
    y = int(y)
    while (x != 1) or (y != 1):
        if x < 1 or y < 1:
            gens = "impossible"
            break
        if x == 1:
            gens += y - 1 
            break
        if y == 1:
            gens += x - 1 
            break
        if x > y:
            #Reduce x by y
            gens += int(x/y)
            x %= y
            x = int(x)
        else:
            #reduce y by x
            gens += int(y / x)
            y %= x
            y = int(y)
    return str(gens)
    #Done in 3 hours,12 minutes