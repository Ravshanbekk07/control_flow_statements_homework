def main(b):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """

    # if a > 0 and a%2:
    #    return 'positive odd number'

    
    
    
    if b<0 and (b+48)%2 ==0:
        print('negative even number')
    
    return 
    

v = main(-24)
print(v)