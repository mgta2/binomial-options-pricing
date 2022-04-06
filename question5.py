# Question 5

def new_euro_call_val(v, K):
    """
    Extension of Question 1 to allow for changing v values.
    
    Algorithm's time complexity is O(2**N).
    
    Parameters
    ----------
    v : float[N]
        N-tuple of floats between 0 and 1.
    K : float
        Strike price.

    Returns
    -------
    option_val : float
        Value of the option as predicted by this model.
    
    """
    
    N = len(v)
    option_price = 0
    
    # Use a bit mask.
    
    for i in range(0, 2**N):
        
        x = 1
        
        for j in range(0, N):
            
            if i & (1 << j):
                x *= (1 + v[j])
            else:
                x *= (1 - v[j])
        
        option_price += max(x - K, 0)
    
    option_price /= 2**N
    
    return option_price


v = (0.2, 0.3, 0.5)
K = 1.1
print(new_euro_call_val(v, K)) # Output: 0.232 (3 s.f.)

v = (0.1, 0.7, 0.2, 0.5, 0.5)
K = 0.9
print(new_euro_call_val(v, K)) # Output 0.459 (3 s.f.)


def new_euro_call_calibrate(K, option_vals):
    """
    This function extends Question 2. We are given N European option calls, all with
    different expiry dates. We model each period of the binomial model as an expiration date.
    (We could take a larger N to model the expiry dates not being equally spaced apart.)
    v[0] is calculated using interval bisection, then v[1] and so on.
    
    Algorithm's time complexity is O(N * count * 2**N)
    
    Parameters
    ----------
    K : float
        Strike price.
    option_vals : float[N]
        N-tuple containing option values.

    Returns
    -------
    v : float[N]
        Value of the options associated to given v's.
    """
    
    N = len(option_vals)
    v = []
    
    for i in range(0, N):
        
        l = 0
        r = 1
        count = 1000
        
        while count > 0:
            
            count -= 1
            mid = (l+r)/2
            l_val = new_euro_call_val(v + [l], K) - option_vals[i]
            mid_val = new_euro_call_val(v + [mid], K) - option_vals[i]
            
            if l_val * mid_val > 0:
                l = mid
            
            else:
                r = mid
        
        v.append(mid)
    
    return v


# Test Cases

K = 1.1
option_vals = (0.1, 0.3, 0.5)

print(new_euro_call_calibrate(K, option_vals)) # Output: [0.300, 0.7, 0.824]

print(new_euro_call_val( [0.3], K )) # Output: 0.100
print(new_euro_call_val( (0.3, 0.7), K )) # Output: 0.300
print(new_euro_call_val( (0.3, 0.7, 0.824), K )) # Output: 0.500

