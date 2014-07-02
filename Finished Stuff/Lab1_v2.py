from random import randint
from time import time

def median(L):
    quicksort(L, 0, len(L)-1)
    
    if len(L)% 2 == 0:
        mid1 = len(L) // 2
        mid2 = (len(L) - 1) // 2
                
        median = float(L[mid1] + L[mid2]) / 2
    else:
        mid = len(L) // 2
        median = L[mid]
        
    return median

#===============================================================================

def quicksort(L, listStart, listEnd):
    if listStart < listEnd:
        index = listStart + (listEnd-listStart) / 2
        
        newIndex = partition(L, listStart, listEnd, index)
        
        quicksort(L, listStart, newIndex - 1)
        
        quicksort(L, newIndex + 1, listEnd)
#===============================================================================
def partition(L, start, end, index):
    iValue = L[index]
    L[index], L[end] = L[end], L[index]
    
    tempIndex = start
    
    for i in range(start, end):
        if L[i] < iValue:
            L[i], L[tempIndex] = L[tempIndex], L[i]
            tempIndex += 1
    
    L[tempIndex], L[end] = L[end], L[tempIndex]
    
    return tempIndex

#===============================================================================

def main(length):
    
    L = []
 
    """f = open("numbers.dat", 'r')
    
    for line in f:
        try:
            L.append(int(line[:-1]))
        except:
            pass    
    """
    
    for i in range(length):
        L.append(randint(1000,9000))
    
    print median(L)
    
    
#=============================================================================== 

if __name__ == '__main__':
    
    length = int(raw_input("Give a value:"))
    
    iTime = time()    
    
    main(length)
    
    print time() - iTime
    raw_input("Done?")