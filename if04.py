def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    p= 0

    if a>0:
       p+=1
        
      
       
    if b>0:
        p+=1
       
    if c>0:
       p+=1
    
    
    return p
        
        
    
v = main(3,-3,-6)
print(v)