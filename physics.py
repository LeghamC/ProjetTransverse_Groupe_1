# -------------------------------------------------------------------------------
# Name:        ???
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Arrow to aim for trajectory
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
from math import sin, cos, atan2, hypot, pi, radians, degrees, sqrt


# VECTOR CLASS TO REPRESENT VECTORS IN 2D
class Vector:
    """
        Compute vectors for the arrow's trajectory when shot by the player

        Args:
            magnitude (float): Length of the vector.
            angle (float): Angle of the vector in degrees.
        """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def angle(self):
        return atan2(self.y, self.x)

    def __add__(self, v: "Vector"):
        return Vector(self.x + v.x, self.y + v.y)

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"[{self.x}, {self.y}]"


def make_vector_polar(magnitude: float, angle: float):
    angle = radians(angle)
    x = magnitude * cos(angle)
    y = magnitude * sin(angle)
    return Vector(x, y)


# CONSTANTS FOR PHYSICS SIMULATION
gravity = Vector(0, -9.8)  # Represents the downward force
friction = 0.99  # Coefficient for simulation of friction
elasticity = 0.8  # Coefficient of kinetic energy preserved in collisions
block_elasticity = 0.7  # Coefficient of kinetic energy preserved in block collisions
