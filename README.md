Riemann Zeta Function Zero Finder

Created by: Mohamed Amine

This Python script explores the zeros of the Riemann Zeta function, particularly focusing on those that lie on the critical line, where the real part of the complex argument is 1/2. The program uses several mathematical techniques and libraries to find and analyze these zeros. Below is a detailed breakdown of how the code works:


---

1. Libraries Used

mpmath: A library for arbitrary-precision arithmetic, used here to calculate the Riemann Zeta function and its zeros with high precision.

numpy: Used for array operations and numerical calculations, such as defining the range for the real and imaginary parts of the complex argument.

matplotlib: A plotting library to visualize the locations of the zeros in the complex plane.

scipy.stats: Used for statistical analysis, particularly for kernel density estimation (KDE) to visualize the distribution of the real and imaginary parts of the zeros.

multiprocessing: Enables parallel computation to speed up the process of finding zeros by splitting the task across multiple CPU cores.



---

2. Main Components

2.1. zeta_function(s)

This function computes the Riemann Zeta function for a given complex number s. It uses the mpmath.zeta() function for high-precision computation.

2.2. is_zero(s, threshold=1e-15)

This function checks if the value of the Zeta function at a given complex number s is close enough to zero. If the absolute value of the Zeta function is smaller than a defined threshold (default 1e-15), it considers the point as a root.

2.3. newton_method(s, max_iter=100, tol=1e-15)

This is an implementation of the Newton-Raphson method, a root-finding algorithm. It iteratively refines guesses for the zeros of the Zeta function. For each iteration, it updates the current guess based on the ratio of the function value to its derivative (zeta_function(s) and its derivative).

2.4. explore_zeta_space(real_min, real_max, imag_min, imag_max, step=0.05)

This function explores a specified region of the complex plane. It generates complex numbers s with real and imaginary parts in the given ranges (from real_min to real_max and imag_min to imag_max), and checks if the Zeta function at those points is zero. If not, it applies the Newton method to refine the guess for a zero.

2.5. plot_roots(roots)

This function takes the list of zeros found and plots them on a scatter plot in the complex plane, where the x-axis represents the real part and the y-axis represents the imaginary part. It provides a visual representation of where the zeros of the Zeta function lie.

2.6. find_zeros_parallel(real_min, real_max, imag_min, imag_max, step=0.05, num_processes=4)

This function leverages parallel processing to speed up the search for zeros. It splits the region of interest in the complex plane into smaller chunks, which are processed simultaneously by multiple CPU cores. It uses the multiprocessing.Pool() class to run explore_zeta_space() on each chunk of the region.

2.7. analyze_roots(roots)

After finding the zeros, this function analyzes the distribution of the real and imaginary parts of the roots. It uses kernel density estimation (KDE) to plot the distribution of real and imaginary parts. It also computes the mean and standard deviation of the real parts and checks what percentage of zeros lie near the critical line (Re(s) ≈ 0.5). The results provide numerical evidence supporting or contradicting the Riemann Hypothesis.


---

3. Execution Flow

1. Set Up Precision: The code sets the precision of the mpmath library to 100 decimal places using mpmath.mp.dps = 100.


2. Define the Region: The region of the complex plane to explore is defined with real parts from -30 to 30 and imaginary parts from -30 to 30 with a step size of 0.05.


3. Find Zeros in Parallel: The script uses multiprocessing to split the task of searching for zeros into smaller chunks and executes them in parallel, speeding up the search.


4. Plot Zeros: After collecting the zeros, the program plots their locations in the complex plane.


5. Analyze the Distribution: It analyzes the distribution of the real and imaginary parts of the zeros and computes statistical metrics like the mean and standard deviation.


6. Check for Critical Line: It checks how many zeros lie on the critical line where the real part is approximately 0.5, which supports the Riemann Hypothesis if the majority of the zeros lie on this line.




---

4. Key Features

High Precision: The script uses high-precision arithmetic with mpmath to ensure accurate calculations of the Zeta function and its zeros.

Parallel Processing: The use of multiprocessing speeds up the computation by processing chunks of the search region in parallel.

Visualization: The script generates a scatter plot of the zeros and provides a density plot of the real and imaginary parts of the zeros to help analyze their distribution.

Riemann Hypothesis Exploration: The code investigates whether the zeros lie on the critical line (Re(s) ≈ 0.5), offering numerical evidence in support of or against the Riemann Hypothesis.



---

5. Conclusion

The script provides a numerical exploration of the zeros of the Riemann Zeta function, focusing on the critical line. By leveraging high precision, parallel computation, and statistical analysis, it offers insights into the distribution of these zeros and serves as a valuable tool for investigating the Riemann Hypothesis.
