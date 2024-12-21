# Signature: 4d 6f 68 61 6d 65 64 20 41 6d 69 6e 65
# Mohamed Amine in hex

import mpmath
import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero
import multiprocessing
import scipy.stats as stats

mpmath.mp.dps = 100

def zeta_function(s):
    return mpmath.zeta(s)

def is_zero(s, threshold=1e-15):
    return abs(zeta_function(s)) < threshold

def newton_method(s, max_iter=100, tol=1e-15):
    for _ in range(max_iter):
        zeta_value = zeta_function(s)
        zeta_prime = mpmath.diff(zeta_function, s)
        if abs(zeta_value) < tol:
            return s
        s = s - zeta_value / zeta_prime
    return s

def explore_zeta_space(real_min, real_max, imag_min, imag_max, step=0.05):
    roots = []
    for real_part in np.arange(real_min, real_max, step):
        for imag_part in np.arange(imag_min, imag_max, step):
            s = mpmath.mpc(real_part, imag_part)
            if is_zero(s):
                roots.append(s)
            else:
                root = newton_method(s)
                if is_zero(root):
                    roots.append(root)
    return roots

def plot_roots(roots):
    if roots:
        roots = np.array(roots)
        plt.scatter(roots.real, roots.imag, color='red', s=1)
        plt.title("Locations of the Zeros of the Riemann Zeta Function")
        plt.xlabel("Real part")
        plt.ylabel("Imaginary part")
        plt.grid(True)
        plt.show()
    else:
        print("No zeros found in the given space.")

def find_zeros_parallel(real_min, real_max, imag_min, imag_max, step=0.05, num_processes=4):
    pool = multiprocessing.Pool(processes=num_processes)
    chunks = np.linspace(real_min, real_max, num_processes + 1)
    chunks_range = [(chunks[i], chunks[i+1], imag_min, imag_max, step) for i in range(len(chunks) - 1)]
    results = pool.starmap(explore_zeta_space, chunks_range)
    pool.close()
    pool.join()
    all_roots = [root for sublist in results for root in sublist]
    return all_roots

def analyze_roots(roots):
    if not roots:
        print("No zeros found for analysis.")
        return
    real_parts = [root.real for root in roots]
    imag_parts = [root.imag for root in roots]
    real_distribution = stats.gaussian_kde(real_parts)
    imag_distribution = stats.gaussian_kde(imag_parts)
    
    plt.subplot(1, 2, 1)
    plt.plot(np.linspace(min(real_parts), max(real_parts), 500), real_distribution(np.linspace(min(real_parts), max(real_parts), 500)))
    plt.title("Real Parts Distribution")
    plt.xlabel("Real Part")
    plt.ylabel("Density")
    
    plt.subplot(1, 2, 2)
    plt.plot(np.linspace(min(imag_parts), max(imag_parts), 500), imag_distribution(np.linspace(min(imag_parts), max(imag_parts), 500)))
    plt.title("Imaginary Parts Distribution")
    plt.xlabel("Imaginary Part")
    plt.ylabel("Density")
    
    plt.tight_layout()
    plt.show()

    real_mean = np.mean(real_parts)
    real_std = np.std(real_parts)
    
    print("Real Part Mean: ", real_mean)
    print("Real Part Std Dev: ", real_std)
    zeros_on_critical_line = sum(0.48 < real < 0.52 for real in real_parts)
    total_zeros = len(real_parts)
    percentage_on_line = (zeros_on_critical_line / total_zeros) * 100
    
    print(f"Percentage of zeros on the critical line (Re(s) ≈ 1/2): {percentage_on_line:.2f}%")
    
    if abs(real_mean - 0.5) < 0.05:
        print("The zeros appear to be concentrated around Re(s) = 1/2, supporting the hypothesis.")
    else:
        print("The zeros do not appear to be concentrated around Re(s) = 1/2, further exploration needed.")
    
    if percentage_on_line > 95:
        print("The majority of the zeros lie on the critical line, providing strong numerical evidence supporting the Riemann Hypothesis.")

real_min, real_max = -30, 30
imag_min, imag_max = -30, 30
step = 0.05

roots = find_zeros_parallel(real_min, real_max, imag_min, imag_max, step)

plot_roots(roots)

analyze_roots(roots)

# Signature: 4d 6f 68 61 6d 65 64 20 41 6d 69 6e 65
# Mohamed Amine in hex
