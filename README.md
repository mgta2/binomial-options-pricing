# Multiperiod Binomial Asset Model

## Introduction

The aim of this project is to understand the multiperiod binomial options pricing model.
For simplicity, only calls (and not puts) will be considered.
This model splits the lifetime of an option into N periods and assumes that at each stage the asset's value will change by a factor of (1+v) or (1-v).
The code assumes an initial asset price of 1, equal probability of going up or down, and a borrowing/lending currency interest rate of zero.
One can visualise this model as a directed graph where each path represents a different series of events (e.g. asset goes: up, up, down, up, down).

Calculating the option's value is done by working backwards from the end nodes, where the option's value is max(S-K, 0) where S is the asset's value and K is the strike price (since one would only choose to exercise the option if it is profitable).
The process of working backwards differs slightly for European vs American options, as unlike their European counterparts, American options can be exercised at any time before the option's expiration date.

### Sources:

Mainly Wikipedia.

## Questions

1. Write a function which determines the value of a European call option, for given v, N and K.

2. Write a function which calibrates v to give a specific option value (under the above function).

3. Write a function which determines the value of an American call option, for given v, N and K.

4. Write a function which returns the expectation of the maximum value the asset attains throughout the option's lifetime.

5. Assume v is no longer constant, but rather we have a different v for each period in the model. Given a collection of European call option values (where no two have the same expiration date) calibrate an N-tuple of v's that result in these option values.

## Comments

### Questions 1 to 3:

As a European call option can only be exercised at its expiration date, my guess is you only want to buy these if you believe the asset's price will rise.
American call options can be exercised at any time before expiration. Therefore, I imagine one would buy these if you are predicting high volitility. Then you can exercise the option at the right moment.

### Question 4: Finding average max value of asset during option.

This program finds the expectation of the maximum value the asset takes during the option. This relates to the above comment - one would aim to exercise an American call option at the point this maximum is attained.

### Question 5: Extending Question 2.

Changing the model to allow for different increase/decrease ratios significantly increases the complexity. The pricing algorithm goes from O(N) to O(2**N).
