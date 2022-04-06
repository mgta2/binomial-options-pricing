# Question 1

from math import factorial

def n_choose_r(n, k):
    return factorial(n)//(factorial(k) * factorial(n-k))

def euro_call_val(v, K, N):
    """
    Function to compute the value of a European call option on an asset with starting price 1,
    using a multiperiod binomial model. Model assumes zero interest rate and equal probability of
    going up/going down.
    
    The value of the asset at the end nodes of the tree are given by max(S-K, 0).
    This function finds their average, weighted by relevant probabilities.
    
    Algorithm's time complexity is at worst O(N) (not taking into account the 'factorial' calls)
    (For large N could use an approximation to 'n_choose_r' to lower cost, e.g. Sterling's approx)
    
    Parameters
    ----------
    v : float
        Constant between 0 and 1 to model asset's volitility (small v means low volitility).
    K : float
        Strike price.
    N : int
        Number of periods in the binomial model.

    Returns
    -------
    option_val : float
        Value of the option as predicted by this model.

    """
    
    option_val = 0
    end_node_val = ((1 + v)**N) - K
    i = 0
    
    while end_node_val > 0 and i < N :
        
        option_val += n_choose_r(N, i) * end_node_val
        i += 1
        end_node_val = ( ((1 + v)**(N - i)) * ((1 - v)**(i)) ) - K
    
    if i == N:
        option_val += end_node_val
    
    option_val /= 2**N
    
    return option_val

# Test Cases

if __name__ == "__main__":
    
    v = 0.2
    K = 0.9
    N = 2
    
    print(euro_call_val(v, K, N)) # Output: 0.100 (3 s.f.)

    v = 0.2
    K = 0
    N = 10
    
    print(euro_call_val(v, K, N)) # Output: 1.0
    
    v = 0.2
    K = 1.1
    N = 10
    
    print(euro_call_val(v, K, N)) # Output: 0.218 (3 s.f.)
    
    v = 0.2
    K = 2
    N = 10
    
    print(euro_call_val(v, K, N)) # Output: 0.0579 (3 s.f.)