
"""
4.20 Population Variance vs. Sample Variance

Question: Research the reason for differences between calculating population 
variance and sample variance.

Answer: 
Population variance is calculated by dividing by the exact total number of 
data points (N). You do this when you have the data for the ENTIRE group 
you are studying.

Sample variance is used when you only have a small subset (a sample) of the 
overall population. Because a sample might not perfectly represent the extremes 
of the whole population, dividing by N tends to underestimate the true variance. 
To correct this bias, sample variance divides by (N - 1). This is known in 
statistics as "Bessel's correction," and it makes the estimate slightly larger 
and more accurate.
"""
