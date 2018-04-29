def fibRecursive(n):
    """[summary]
    Computes the n-th fibonacci number recursive.
    Problem: This implementation is very slow.
    approximate O(2^n)

    Arguments:
        n {[int]} -- [description]
    
    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be a positive integer'

    if n <= 1:
        return n
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)

# print (fibRecursive(35))

def fibList(n):
    """[summary]
    This algorithm computes the n-th fibbonacci number
    very quick. approximate O(n)
    The algorithm use dynamic programming.
    
    Arguments:
        n {[int]} -- [description]
    
    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be a positive integer'

    listResults = [0, 1]
    for i in range(2, n+1):
        listResults.append(listResults[i-1] + listResults[i-2])
    return listResults[n]

# print(fibList(100)) # => 354224848179261915075
