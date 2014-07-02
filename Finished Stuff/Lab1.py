from random import randint
from time import time

def median(L):
    L = sortify(L)
    
    if len(L)% 2 == 0:
        mid1 = len(L) // 2
        mid2 = (len(L) - 1) // 2
                
        median = float(L[mid1] + L[mid2]) / 2
    else:
        mid = len(L) // 2
        median = L[mid]
        
    return median

#===============================================================================

def sortify(L1):
    L2 = []
    
    for num in L1:
        if len(L2) == 0:
            L2.append(num)
        else:
            for i in range(len(L2)):
                if num < L2[i]:
                    L2.insert(i, num)
                    break
            else:
                L2.append(num)
        
    return L2

#===============================================================================

def main():
    
    L = []
 
    """f = open("test.dat", 'r')
    
    for line in f:
        try:
            L.append(int(line[:-1]))
        except:
            pass    
    """
    
    for i in range(10000):
        L.append(randint(1000,9000))
        
    
    print median(L)
    
    
#=============================================================================== 

if __name__ == '__main__':
    iTime = time()
    main()
    
    print time() - iTime