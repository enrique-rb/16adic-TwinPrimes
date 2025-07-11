import numpy as np
from sympy import primerange, isprime, gcd
from math import log
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt
from tqdm import tqdm
from sympy import factorint

# Configuration
N = 10**8               # Upper bound
MODULI = [16, 30, 42, 60, 210]  # Moduli to test
PRECISION = 6           # Decimal places
C2 = 0.6601618158468696 # Twin prime constant

# ------------------------------------------
# Dynamic Generation (Optimized with sets)
# ------------------------------------------
def get_admissible_residues(m):
    """Generate admissible pairs as a set for O(1) lookups."""
    return {(a, (a + 2) % m) for a in range(m) if gcd(a * (a + 2), m) == 1}

def compute_k_r(m, admissible):
    """Calculate k_r = ν₂(3r + 1) for admissible residues."""
    return {a: (3*a + 1 & - (3*a + 1)).bit_length() - 1 for a, _ in admissible}

ADMISSIBLE = {m: get_admissible_residues(m) for m in MODULI}  # Dict of sets
k_r = {m: compute_k_r(m, ADMISSIBLE[m]) for m in MODULI}

# ------------------------------------------
# Collatz Weighted Steps
# ------------------------------------------
def collatz_weight(r):
    weight = 0
    while r != 1:
        if r % 2 == 0:
            r //= 2
        else:
            step = 3 * r + 1
            weight += (step & -step).bit_length() - 1
            r = step // (step & -step)
    return weight

k_r_star = {m: {a: collatz_weight(a) for a, _ in ADMISSIBLE[m]} for m in MODULI}

# ------------------------------------------
# Mathematical Core
# ------------------------------------------
def hardy_littlewood(N, a, m):
    # primes_m = {p for p in primerange(1, m) if m % p == 0}
    primes_m = set(factorint(m).keys())
    product = 1.0
    for p in primes_m:
        if (a * (a + 2)) % p == 0:
            product *= (1 + 1/(p - 2))
    phi2 = len(ADMISSIBLE[m])
    k = k_r_star[m].get(a, 1)
    return 2 * C2 * (N / (log(N)**2)) * (product / phi2) * (1 + k/log(N))

# ------------------------------------------
# Analysis Pipeline
# ------------------------------------------
def test_moduli(N, moduli):
    results = {}
    for m in moduli:
        counts = {a: 0 for a, _ in ADMISSIBLE[m]}
        primes = list(primerange(3, N))
        
        for p in tqdm(primes, desc=f"Mod {m}"):
            a = p % m
            if (a, (a + 2) % m) in ADMISSIBLE[m] and isprime(p + 2):
                counts[a] += 1
        
        hl_predictions = {a: hardy_littlewood(N, a, m) for a, _ in ADMISSIBLE[m]}
        results[m] = {
            'counts': counts,
            'HL_predictions': hl_predictions,
            'total_twins': sum(counts.values())
        }
    return results

def print_results(results, precision=PRECISION):
    """Print formatted results table."""
    for m, data in results.items():
        print(f"\nModulus {m}:")
        print("-" * (50 + precision * 2))
        print(f"{'Residue':<10}{'Twins Count':<15}{'HL Prediction':<20}{'Ratio (Count/HL)':<20}")
        print("-" * (50 + precision * 2))
        for a in sorted(data['counts'].keys()):
            cnt = data['counts'][a]
            hl = data['HL_predictions'][a]
            print(f"{a:<10}{cnt:<15}{hl:.{precision}f}{'':<5}{cnt/hl:.{precision}f}")
        print(f"\nTotal twins: {data['total_twins']}")

def analyze_correlations(results, m):
    """Compute Pearson/Spearman correlations between k_r and twin counts."""
    counts = results[m]['counts']
    residues = sorted(counts.keys())
    
    # Prepare data
    y = [counts[a] for a in residues]
    x_nu2 = [k_r[m].get(a, 1) for a in residues]  # ν₂(3r+1)
    x_star = [k_r_star[m].get(a, 1) for a in residues]  # Full Collatz weight
    
    # Compute correlations
    pearson_nu2, p_pearson_nu2 = pearsonr(x_nu2, y)
    spearman_nu2, p_spearman_nu2 = spearmanr(x_nu2, y)
    pearson_star, p_pearson_star = pearsonr(x_star, y)
    spearman_star, p_spearman_star = spearmanr(x_star, y)
    
    print(f"\nMod {m} Correlations:")
    print(f"Pearson (ν₂): r = {pearson_nu2:.4f}, p = {p_pearson_nu2:.4g}")
    print(f"Spearman (ν₂): ρ = {spearman_nu2:.4f}, p = {p_spearman_nu2:.4g}")
    print(f"Pearson (k_r^*): r = {pearson_star:.4f}, p = {p_pearson_star:.4g}")
    print(f"Spearman (k_r^*): ρ = {spearman_star:.4f}, p = {p_spearman_star:.4g}")

# ------------------------------------------
# Main Execution
# ------------------------------------------
if __name__ == "__main__":
    print(f"Analyzing twin primes up to N = {N:_} with moduli {MODULI}...")
    results = test_moduli(N, MODULI)
    print_results(results)
    
    for m in MODULI:
        analyze_correlations(results, m)