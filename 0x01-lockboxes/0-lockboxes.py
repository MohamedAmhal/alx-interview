#!/usr/bin/python3
def canUnlockAll(boxes) :

    """
    this function to check the boxs!!
    parameters:
    @boxes : define a list to list for the box
    """
    liste = []
    n = len(boxes) 
    for i in range(n):
        if i == 0:
            liste.append("YES")
        else :
            liste.append("NO")
    while (liste.count("YES") != 0):
        for i in range(n):
            if liste[i] == "YES" :
                m = i
                break
        r = len(boxes[m])
        for j in range(r):
            try :
                index = boxes[m][j]
                if liste[index] == "NO" :
                    liste[index] = "YES"
            except :
                continue
        liste[m] = "YES AND CHECKED !"
    for i in range(n):
        if liste[i] == "NO" :
            return False
    
    return True
