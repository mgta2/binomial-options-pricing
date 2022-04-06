# Question 4

def find_max(v, N, mask):
    
    path_max = 1
    node_val = 1
    
    for i in range(0, N):
        
        if mask & (1 << i):
            node_val *= (1 + v)
        
        else:
            node_val *= (1 - v)
        
        path_max = max(path_max, node_val)
        
    return path_max
    

def average_max(v, N):
    
    """
    This function computes the expectation of max(Sj) random variable by brute force.
    It considers all possible paths down the tree (2**N of them) and finds each path's
    maximum value. The path choices (up vs down) are encoded in a bit mask.
    
    Algorithm's time complexity is O(N * 2**N).

    Parameters
    ----------
    v : float
        Number between 0 and 1 as previously.
    N : int
        Number of periods in binomial model.

    Returns
    -------
    expected_value : float
        Expected value of random variable max(Sj).
        
    """
    
    # Use bitmask to encode info about up vs down.
    
    expected_value = 0
    
    for mask in range(0, 2**N):
        
        expected_value += find_max(v, N, mask)
    
    expected_value /= 2**N
    
    return expected_value

if __name__ == "__main__":

    print(average_max(0.2, 2)) # Output: 1.16 (3 s.f.)
    print(average_max(0.2, 3)) # Output: 1.22 (3 s.f.)
    print(average_max(0.2, 10)) # Output: 1.49 (3 s.f.)

# For larger N this quickly becomes computationally infeasible.

"""
Comments:

(1) The tree has only O(N**2) lattice points in it. Therefore, a quicker algorithm could be
produced by looping over each ((1+v)**i) * ((1-v)**j) and asking how many paths have this
as their maximum. This would involve sorting the above set of floats, which would require
O(N**2 * log(N**2)) = O(N**2 * log(N)) operations. This would be significantly quicker
for large N than the above algorithm.

(2) A lower bound can be easily found by considering:

E(max(S)) = [E(max(S | "first=up")) + E(max(S | "first=down"))] / 2

Using E(max(S | "first=down")) >= 1 and solving a difference equation gives a lower bound of

(1 - x)/(1 - v) + x

where x = ((1 + v)/2)**N

"""

if __name__ == "__main__":

    v = 0.2
    N = 10
    x = ((1+v)/2)**N
    print(((1-x)/(1-v)) + x) # Output 1.25 (3 s.f.) (note that the real value is 1.49)