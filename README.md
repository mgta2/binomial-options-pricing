# Multiperiod Binomial Asset Model

Time taken: Approx 7 hours (2 for research/learning finance terms, 5 for code writing/problem solving)

Assumptions: initial asset price is 1, interest rate of 0, risk-neutral measure.

## Comments

### Questions 1 to 3:

As a European call option can only be exercised at its expiration date, my guess is you only want to buy these if you believe the asset's price will rise.
American call options can be exercised at any time before expiration. Therefore, I imagine one would buy these if you are predicting high volitility. Then you can exercise the option at the right moment.

### Question 4: Finding average max value of asset during option.

This program finds the expectation of the maximum value the asset takes during the option. This relates to the above comment - one would aim to exercise an American call option at the point this maximum is attained.

### Question 5: Extending Question 2.

Changing the model to allow for different increase/decrease ratios significantly increases the complexity. The pricing algorithm goes from O(N) to O(2**N).
