import sys
import math

def compute_average_velocity(n, h, theta, w, s):
    """
    Computes the average velocity based on channel parameters.

    Args:
        n (float): Manning coefficient [s/m^(1/3)]
        h (float): Water depth [m]
        theta (float): Bank slope [rad] 
        w (float): Bottom width [m]
        s (float): Channel slope [-]

    Returns:
        float: Average velocity [m/s]
    """
    # Hydraulic radius
    Rh = 0.5 * h * (w + 2 * h / math.tan(theta)) / (w + 2 * h / math.sin(theta))
    return (1/n) * Rh**(2/3) * s**(1/2)

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print("""
    Available functions:

    compute_average_velocity(n, h, theta, w, s)
        Computes the average velocity based on channel parameters.
        Args:
            n (float): Manning coefficient [s/m^(1/3)]
            h (float): Water depth [m]
            theta (float): Bank slope [rad]
            w (float): Bottom width [m]
            s (float): Channel slope [-]
        Returns:
            float: Average velocity [m/s]
    Usage:
        python ComputeFr.py n h theta w s
    """)
        sys.exit(0)
    if len(sys.argv) != 6:
        print("Usage: python ComputeFr.py n h theta w s")
        sys.exit(1)

    n = float(sys.argv[1])
    h = float(sys.argv[2])
    theta = float(sys.argv[3])
    w = float(sys.argv[4])
    s = float(sys.argv[5])

    avg_velocity = compute_average_velocity(n, h, theta, w, s)
    print(f"Average velocity: {avg_velocity} m/s")

    g = 9.81  # gravitational acceleration [m/s^2]
    Fr = avg_velocity / (g * h) ** 0.5
    print(f"Froude number: {Fr}")

    # Calculate cross-sectional area
    area = h * (w + h / math.tan(theta))
    discharge = avg_velocity * area
    print(f"Total discharge: {discharge} m^3/s")