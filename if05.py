def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    b = 0
    if a<0:
        b+=1
    if b<0:
        b+=1
    if c<0:
        b+=1
    return b


v= main(3,-3,-6)
print(v)