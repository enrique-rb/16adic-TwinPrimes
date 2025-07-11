# 16adic-TwinPrimes

## A Computational Test of the 16-adic Collatz Framework on Twin Primes

### Project Status: Archived

This repository documents a computational investigation into a speculative link between a simplified Collatz framework and the distribution of twin primes. The project is now archived, as the investigation led to a conclusive **null result**. The code and findings are preserved here for reference and reproducibility.

---

### Overview

This project was motivated by promising results from a "16-adic framework" that successfully modeled partition densities for the Goldbach Conjecture. The central hypothesis was that this framework, derived from the dynamics of a simplified Collatz map, might also predict the density of twin prime pairs across different modular residue classes.

To test this, we conducted a rigorous computational analysis to measure the correlation between twin prime counts and two different Collatz-derived features:
1.  **A first-order divisor (`ν₂`)**: Based on the initial `3r+1` step.
2.  **A full-trajectory weight (`k_r^*`)**: A more complex feature representing the entire Collatz path of a residue.

Despite extensive testing, including the exploration of an anomalous result, the final conclusion is that no such general correlation exists.

---

### Experimental Setup

- **Data Range:** Twin primes `(p, p+2)` were counted up to `N = 10^8`.
- **Moduli Tested:** The analysis was performed for `m ∈ {16, 30, 42, 60, 210}` to test the hypothesis under various conditions.
- **Features Analyzed:** For each admissible residue `r mod m`, we computed two features:
    - `k_r = ν₂(3r + 1)`
    - `k_r^*` (the full-trajectory Collatz weight)
- **Statistical Tests:** We used both Pearson (linear) and Spearman (monotonic) correlation tests to find any potential relationships.
- **Primary Script:** All analysis was performed using the final script `twin_prime_moduli_v4.py`.

---

### 📈 Key Findings

The central finding of this research is a **null result**. Across the tested moduli and features, no consistent, statistically significant correlation was found.

An anomalous result was briefly observed for `m=30`, but was refuted with further testing.

**1. No General Correlation Found**
For the vast majority of cases, including the primary modulus of interest `m=16`, the correlation coefficients were near zero with high p-values, indicating no predictive relationship.

**2. The Anomaly at Modulo 30**
An initial test with the `k_r^*` feature produced a perfect negative correlation (`ρ = -1.0`) for `m=30`. However, this modulus has only 3 admissible classes.

**3. Refutation of the Anomaly**
To verify this, we tested against moduli with more classes (`m=42` and `m=60`). The perfect correlation immediately vanished, confirming that the `m=30` result was a **low-dimensional statistical artifact** and not a general principle.

#### Final Correlation Summary (Spearman ρ, `k_r^*` vs. Raw Counts)

| Modulus (classes) | Spearman ρ | p-value | Conclusion |
| :--- | :--- | :--- | :--- |
| 16 (8 classes) | 0.262 | 0.531 | No correlation |
| **30 (3 classes)** | **-1.000** | **0.000** | **Spurious Anomaly** |
| 42 (5 classes) | 0.100 | 0.873 | No correlation |
| 60 (6 classes) | -0.371 | 0.469 | No correlation |
| 210 (15 classes) | -0.020 | 0.945 | No correlation |

---

### Conclusion

The 16-adic Collatz framework, while predictive for Goldbach partitions, **does not extend to the distribution of twin primes.**

This null result is significant because it helps define the boundaries of the original theory. It suggests the framework's mechanism is specifically related to the nature of **additive prime problems (`p+q=n`)** and does not apply to problems of **prime spacing (`p₂ - p₁ = k`)**. This strengthens the specificity and interest of the Goldbach result.

---

### Repository Contents

- **`twin_prime_16adic_null_result.tex`**: The LaTeX source for the final research paper summarizing these findings.
- **`twin_prime_moduli_v4.py`**: The final, robust Python script used to perform the entire analysis. The data can be fully reproduced by running this script.
- **`LICENSE`**: This project is shared under the MIT License.
