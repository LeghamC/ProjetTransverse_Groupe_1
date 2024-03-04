# -------------------------------------------------------------------------------
# Name:        ???
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Arrow to aim for trajectory
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
from math import sin, cos, atan2, hypot, pi, radians, degrees


# VECTOR CLASS TO REPRESENT VECTORS IN 2D
class Vector:
    """
        Compute vectors for the arrow's trajectory when shot by the player

        Args:
            magnitude (float): Length of the vector.
            angle (float): Angle of the vector in degrees.
        """

    def __init__(self, magnitude: float = 0, angle: float = 0) -> None:
        self.magnitude = magnitude
        self.angle = angle


def add_vectors(vector1: Vector, vector2: Vector) -> Vector:
    """
        Addition of two 2D vectors.

        Args:
            vector1, vector2 (Vector): Two Vector objects.

        Returns:
            Vector: New Vector object representing the sum of vector1 and vector2.
        """
    # Convert angles to radians (trigonometric computation)
    angle1_rad = radians(vector1.angle)
    angle2_rad = radians(vector2.angle)

    # Compute x and y components of the resulting vector
    x = sin(angle1_rad) * vector1.magnitude + sin(angle2_rad) * vector2.magnitude
    y = cos(angle1_rad) * vector1.magnitude + cos(angle2_rad) * vector2.magnitude

    # Compute angle and magnitude of the resulting vector (in degrees)
    new_angle_rad = 0.5 * pi - atan2(y, x)
    new_angle_deg = degrees(new_angle_rad)
    new_magnitude = hypot(x, y)

    # Create and return the new Vector object
    new_vector = Vector(new_magnitude, new_angle_deg)
    return new_vector


# CONSTANTS FOR PHYSICS SIMULATION
gravity = Vector(0.2, 180)  # Represents the downward force
friction = 0.99  # Coefficient for simulation of friction
elasticity = 0.8  # Coefficient of kinetic energy preserved in collisions
block_elasticity = 0.7  # Coefficient of kinetic energy preserved in block collisions
