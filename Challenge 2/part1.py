def solution(l, t):
    # Your code here
    #Use for loop to start at each index
    #From each index, start adding until you go over. 
    #If a sequence adds up to t, note the start and end indexes and return those, otherwise return [-1.-1]
    for index in range(len(l)):
        total = 0
        add = 0
        while total < t and (index + add) <= len(l)  -1:
            total += l[index + add]
            if total == t:
                return [index, index + add]
            add = add + 1
    return [-1,-1]
