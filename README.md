# geocentric-orbit-simulator
Interactive 2D orbital simulator in Python. Input custom initial altitudes (in Earth radii) and velocity coefficients to calculate and classify trajectories (circular, elliptical, parabolic and hyperbolic).

## Features

* **Interactive Inputs:** Set the initial distance directly in **Earth Radii (ER)** (from 1.06 ER up to 235 ER, near Earth's Hill radius).
* **Velocity Scaling ($k_v \ge 1$):** Input a custom velocity multiplier based on the local initial velocity ($v_{circ}$):
  * $k_v = 1$: Circular orbit
  * $1 < k_v < \sqrt{2}$: Elliptical orbit
  * $k_v = \sqrt{2}$: Parabolic escape trajectory
  * $k_v > \sqrt{2}$: Hyperbolic escape trajectory
* **Physics-Engine Calculations:**
  * Computes the theoretical orbital period using Kepler's Third Law: $T = 2\pi\sqrt{\frac{r^3}{G \cdot M_{earth}}}$.
  * Integrates equations of motion step-by-step using high-precision astronomical constants from `astropy`.
* **Smart Visualization:** Generates a beautifully scaled 2D plot showing Earth at the center, the starting point, the trajectory, and an automatic label identifying the type of orbit achieved.

## Tech Stack & Libraries

* **Python 3**
* **NumPy**
* **Matplotlib** 
* **Astropy** 

## How It Works

1. **Input Parameters:** The script prompts the user for the starting distance in Earth Radii and the velocity multiplier $k_v$.
2. **Error Checking:** The system validates that inputs are physically reasonable.
3. **Simulation:** A loop calculates the gravitational acceleration vector at each timestep ($a = -\frac{GM}{r^2}$) and updates the satellite's position.
4. **Plotting:** Standardizes physics data into and plots the final trajectory.
