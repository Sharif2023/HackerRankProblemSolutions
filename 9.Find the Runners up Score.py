if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    #step-1: converted the list to set so, 
    #it will not store multiple same integers.
    setconvert = set(arr)
    
    #step-2: sorted the list of scores.
    setsort = sorted(setconvert)
    
    #step-3: printed the second-last integer of the list. 
    #And, it is the runner-up score.
    print(setsort[-2])
    
       