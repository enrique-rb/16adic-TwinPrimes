# 16adic-TwinPrimes
Paper and Python code for the computational investigation of a Collatz-derived framework on twin prime distribution, confirming a null result.

## Twin Primes and the 16-adic Collatz Framework

### Project Status: Frozen

This exploratory project tested a speculative connection between:
- The **16-adic residue dynamics** arising from a simplified Collatz map with fixed divisors, and
- The **distribution of twin primes** across modular residue classes.

The experiment was motivated by earlier promising results on Goldbach partitions using a similar 16-adic structure. Here, we investigated whether **residue class behavior influenced by Collatz iterations** could also explain the density of **twin prime pairs**.

### Experimental Setup

- Twin primes \( (p, p+2) \) were counted up to \( N = 10^6 \), restricted to admissible residue pairs mod \( m \in \{16, 30, 210\} \).
- The **Hardy–Littlewood heuristic** was used to estimate expected counts per residue class.
- Each residue class was associated with a Collatz-derived "fixed divisor" \( k_r \), as defined in prior work.
- We analyzed the correlation between actual twin prime counts and \( k_r \) values using Pearson correlation.

### Results Summary

Sample output (Mod 16):
```Correlation Analysis (k_r vs. Raw Twin Prime Counts):
Mod 16: r = -0.4355, p = 0.2809
Mod 30: r = -0.8879, p = 0.3043
```
**Key observations:**
1. **Negative Correlation**: There is a weak negative tendency between \( k_r \) and twin prime counts in Mod 16. The hypothesis predicted a positive one.
2. **Not Statistically Significant**: The p-value (0.28) indicates no reliable signal—this result is likely due to chance.

### Conclusion

This experiment suggests that **the 16-adic Collatz structure does *not* extend meaningfully to twin prime distributions**. In contrast, prior results for **Goldbach-style additive structures** showed much stronger and statistically significant correspondence with the same residue class framework.

Thus, the outcome strengthens the idea that the 16-adic Collatz mapping is specifically tailored to **additive pairings (Goldbach)** rather than general **prime spacing (twin primes)**.

### Final Notes

- The code remains available for replication or adaptation.
- Two correlation plots (`correlation_plot.png`, `.pdf`) are generated.
- This repository will remain archived unless future insights warrant a revisit.
  
