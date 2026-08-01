"""Physics models for 2D geocentric orbital dynamics using Euler integration."""

from math import pi, sqrt
import numpy as np


def simulate_orbit(
    x0: float, v0: float, GM_earth: float, R_earth: float, mech_energy: float, step: int = 20000
) -> tuple[np.ndarray, np.ndarray]:
    """Simulates the 2D orbital path around Earth and returns normalized coordinates (in ER)."""
    # T_reference: reference circular period [s] used to simplify calculations on open orbits, that don't have a period
    T_reference: float = 2 * pi * sqrt(x0**3 / GM_earth)

    # Calculate time step based on orbit type
    if mech_energy < 0:
        semi_axis: float = -GM_earth / (2 * mech_energy)
        # T: actual orbital period [s] calculated from the elliptic semi-major axis
        T: float = 2 * pi * sqrt(semi_axis**3 / GM_earth)
    else:
        T: float = T_reference * 0.7  # This is to see better the curvature of open orbits

    dt: float = T / step
    check: int = 0

    x: list[float] = [x0]
    y: list[float] = [0.0]
    vx: list[float] = [0.0]
    vy: list[float] = [v0]

    distance: float = sqrt(x[-1] ** 2 + y[-1] ** 2)

    # INTEGRATION LOOP
    while distance >= R_earth and check < step:
        ax = (-GM_earth * x[-1]) / distance**3
        ay = (-GM_earth * y[-1]) / distance**3

        next_vx = vx[-1] + ax * dt
        next_vy = vy[-1] + ay * dt

        next_x = x[-1] + next_vx * dt
        next_y = y[-1] + next_vy * dt

        x.append(next_x)
        y.append(next_y)
        vx.append(next_vx)
        vy.append(next_vy)

        distance = sqrt(x[-1] ** 2 + y[-1] ** 2)
        check += 1

    # Normalize coordinates to Earth Radii (ER)
    x_ER: np.ndarray = np.array(x) / R_earth
    y_ER: np.ndarray = np.array(y) / R_earth

    return x_ER, y_ER
