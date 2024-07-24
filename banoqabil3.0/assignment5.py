#function

def max_of_three(a,b,c): 

    if a > b and a > c :
        return a
    elif b > c and b > c:
        return b
    else:
        return c
    
a=45
b=67
c=32

largest=max_of_three(a,b,c) 
print('the largest of three is',largest)   
    