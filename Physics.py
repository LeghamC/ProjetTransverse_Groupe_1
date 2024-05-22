# -------------------------------------------------------------------------------
# Name:        Aux Quatre Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Vector class used for physics
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
from math import sin, cos, atan2, hypot, pi, radians, degrees, sqrt


# VECTOR CLASS TO REPRESENT VECTORS IN 2D
class Vector:
    """
    represent 2D vectors and includes various vector operations/constants for physics simulation.
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def magnitude(self):
        """Computes/returns the magnitude of the vector using the Pythagorean theorem."""
        return sqrt(self.x*self.x + self.y*self.y)

    def angle(self):
        """Computes/returns the angle of the vector in radians using the atan2 function
         (takes into account the signs of both vector components)."""
        return atan2(self.y, self.x)

    def __add__(self, v: "Vector"):
        """Return a new vector that represent the sum of two vectors' components."""
        return Vector(self.x + v.x, self.y + v.y)

    def __mul__(self, scalar: float):
        """Return a vector that got multiplied by a scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        """Gives the vector under string form"""
        return f"[{self.x}, {self.y}]"


def make_vector_polar(magnitude: float, angle: float):
    """ Convert angle in degrees to radians then create a Vector with the polar coordinates"""
    angle = radians(angle)
    x = magnitude * cos(angle)
    y = magnitude * sin(angle)
    return Vector(x, y)


# CONSTANTS FOR PHYSICS SIMULATION
gravity = Vector(0, -9.8)  # Represents the downward force
friction = 0.99  # Coefficient for simulation of friction
elasticity = 0.8  # Coefficient of kinetic energy preserved in collisions
block_elasticity = 0.7  # Coefficient of kinetic energy preserved in block collisions
