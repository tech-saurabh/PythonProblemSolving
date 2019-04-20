def arraycheck(array):
    """
    checking array if it contains sequence (1,2,3)
    in it
    
    """
    for i in range(len(array)-2):
        if(array[i]==1 and array[i+1]==2 and array[i+2]==3):
            return(True)
    return(False)
            

array=list(map(int,input().split()))
result=arraycheck(array)
print(result)
