from math import pi, sqrt
import sys
from astropy.constants import GM_earth, R_earth
import matplotlib.pyplot as plt
import numpy as np

from physics import simulate_orbit

# CONSTANTS EXTRACTION
GM_earth_val: float = GM_earth.value
R_earth_val: float = R_earth.value

# TAKING USER INPUT
x0_ER: float = float(input("Insert initial distance in ER, approx. between 1.06 (ISS) and 235 (Hill's radius): "))
k_v: float = float(input("Insert a coefficient of multiplication for velocity. k=1: circular, 1<k<sqrt(2): ellipse, sqrt(2): escape: "))

# CHECKING INPUTS
if x0_ER < 1 or x0_ER > 235:
    print("Invalid initial distance!")
    sys.exit()

if k_v < 1:
    print("The coefficient cannot be less than 1!")
    sys.exit()

# DEFINING INITIAL PARAMETERS
x0: float = R_earth_val * x0_ER
v_circ: float = sqrt(GM_earth_val / x0)
v0: float = k_v * v_circ

# MECHANICAL ENERGY CALCULATION
# Satellite mass is simplified since it appears in all terms.
# If energy is negative the orbit will be closed, else parabolic (E=0) or hyperbolic (E>0).
mech_energy: float = 0.5 * v0**2 - GM_earth_val / x0

# RUN SIMULATION
x_ER, y_ER = simulate_orbit(x0, v0, GM_earth_val, R_earth_val, mech_energy)

# CLASSIFY ORBIT TYPE AND COLOR
if k_v == 1.0:
    orbit_type: str = "The orbit is a circumference"
    orbit_color: str = "limegreen"
elif 1.0 < k_v < 1.41:
    orbit_type: str = "The orbit is an ellipse"
    orbit_color: str = "powderblue"
elif 1.41 <= k_v < 1.42:
    orbit_type: str = "The orbit is a parabola"
    orbit_color: str = "maroon"
else:
    orbit_type: str = "The orbit is a hyperbola"
    orbit_color: str = "gold"

# PLOTTING
fig, ax = plt.subplots(figsize=(8, 8))

earth = plt.Circle((0, 0), 1.0, color="royalblue", alpha=0.6, label="Earth")
ax.add_patch(earth)

ax.plot(x_ER, y_ER, color=orbit_color, linewidth=2, label="Satellite trajectory")
ax.plot(x_ER[0], y_ER[0], "ro", markersize=8, label="Starting point")

ax.text(
    x_ER[0],
    y_ER[0] + 0.4,
    orbit_type,
    color=orbit_color,
    fontsize=11,
    fontweight="bold",
    bbox=dict(facecolor="white", alpha=0.8, edgecolor="none"),
)

ax.set_xlabel("X Distance [Earth Radii - ER]", fontsize=11)
ax.set_ylabel("Y Distance [Earth Radii - ER]", fontsize=11)
ax.set_title("Geocentric Orbital Simulation", fontsize=14, fontweight="bold", pad=15)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_aspect("equal", adjustable="box")
ax.legend(loc="upper right")

max_coordinate = max(max(abs(x_ER)), max(abs(y_ER)))
limits = max_coordinate * 1.1

ax.set_xlim(-limits, limits)
ax.set_ylim(-limits, limits)

plt.show()
