# Question 2

import question1

def euro_call_calibrate(K, option_val, N):
    """
    Function to compute v (from Question 1) such that the model prices the option's
    value at 'option_val'. The algorithm uses interval bisection. This method works as
    option_val is a polynomial (therefore continuous) in v.
    
    The 'count' variable (set to 1000) can be modified to achieve desired level of accuracy.
    
    Algorithm's time complexity is O(count * N).

    Parameters
    ----------
    K : float
        Strike price.
    option_val : float
        Value of the European call option.
    N : int
        Number of periods in binomial model.

    Returns
    -------
    v : float
        Number between 0 and 1 as in Question 1.

    """
    
    l = 0
    r = 1
    count = 1000
    
    while count > 0:
        
        count -= 1
        mid = (l+r)/2
        l_val = question1.euro_call_val(l, K, N) - option_val
        mid_val = question1.euro_call_val(mid, K, N) - option_val
        
        if l_val * mid_val > 0:
            l = mid
            
        else:
            r = mid
    
    v = mid
    
    return v


if __name__ == "__main__":

    # Test Cases
    
    N = 10
    K = 1.1
    option_val = 0.218
    
    print(euro_call_calibrate(K, option_val, N)) # Output: 0.200 (3 s.f.)
    print(question1.euro_call_val(0.200, K, N)) # Output: 0.218 (3 s.f.)
    
    N = 50
    K = 1.2
    option_val = 0.3
    
    print(euro_call_calibrate(K, option_val, N)) # Output: 0.130 (3 s.f.)
    print(question1.euro_call_val(0.130, K, N)) # Output: 0.299 (3 s.f.)