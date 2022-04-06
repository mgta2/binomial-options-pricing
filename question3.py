# Question 3

def american_call_val(v, K, N):
    """
    Function to compute the value of an American call option using the same model as in Question 1.
    The difference is that the option can be exercised at any time before expiration.
    
    This is realised in the algorithm by declaring the option's value at a given time to be the maximum of
    the binomial value and the exercise value. The binomial value contains information about the
    value of the option in the future, while the exercise value contains information about its
    value if exercised at that time.
    
    Algorithm's time complexity is O(N**2)

    Parameters
    ----------
    v : float
        Value between 0 and 1 as before.
    K : float
        Strike price.
    N : int
        Number of periods in the binomial model.

    Returns
    -------
    option_val : float
        Value of the option as predicted by this model.

    """
    
    end_node_vals = [0]*(N+1)
    
    for i in range(0, N+1):
        end_node_vals[i] = max(( ((1 + v)**(N - i)) * ((1 - v)**(i)) ) - K, 0)
    
    for level in range(N-1, -1, -1):
        
        next_node_vals = [0]*(level+1)
        
        for k in range(0, level+1):
            binomial_val = ( end_node_vals[k] + end_node_vals[k+1] ) / 2
            exercise_val = ( ((1 + v)**(level - k)) * ((1 - v)**(k)) ) - K
            
            # Note that binomial_val >= 0 so no need to take max(exercise_val, 0)
            
            next_node_vals[k] = max(binomial_val, exercise_val)
        
        end_node_vals = next_node_vals
    
    option_val = end_node_vals[0]
    
    return option_val


if __name__ == "__main__":

    # Test Cases
    
    v = 0.2
    K = 0.9
    N = 2
    
    print(american_call_val(v, K, N)) # Output: 0.165 (3 s.f.)
    
    # Note that this is higher than the European call value with same parameters (which gave 0.100).
    # This makes sense as an American call option gives the holder more freedom, so ought to be more valuable.
    
    v = 0.2
    K = 1.1
    N = 10
    
    print(american_call_val(v, K, N)) # Output: 0.218 (3 s.f.)
    v = 0.2
    K = 1.1
    N = 100
    
    print(american_call_val(v, K, N)) # Output: 0.672 (3 s.f.)