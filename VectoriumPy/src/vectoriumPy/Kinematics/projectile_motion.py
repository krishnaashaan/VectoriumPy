"""
Thiis module deals with projectile motion.
"""
def projectile_motion(u,θ,t,g=9.81):
    """
    Calculate the horizontal and vertical components of projectile motion.

    Parameters:
    u (float): Initial velocity (m/s)
    θ (float): Angle of projection (degrees)
    t (float): Time of flight (s)
    g (float, optional): Acceleration due to gravity (m/s²). Default is 9.81 m/s².

    Returns:
    tuple: A tuple containing the horizontal and vertical components of projectile motion.
    """
    import numpy as np
    # Convert angle from degrees to radians
    θ_rad = np.radians(θ)

    # Calculate horizontal and vertical components
    horizontal_component = u * np.cos(θ_rad) * t
    vertical_component = u * np.sin(θ_rad) * t - 0.5 * g * t**2

    return horizontal_component, vertical_component
    # Calculate displacement and time of flight
# Working on this function, will be added in the next update.