import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("You must specify either the radius or the diameter.")
        if radius is not None and diameter is not None:
            raise ValueError("You can only specify one of radius or diameter.")
        
        # Initialize internal representation based on which is provided
        if radius is not None:
            self._radius = float(radius)
        else:
            self._radius = float(diameter) / 2

    # --- Properties for radius and diameter ---
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = float(value) / 2

    # --- Circle abilities ---
    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    # --- String representation ---
    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return f"Circle({self.radius})"

    # --- Addition of two circles (returns a new one) ---
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    # --- Comparisons ---
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

# Testing Methods   
c1 = Circle(radius=4)
c2 = Circle(diameter=10)
c3 = c1 + c2

print(c1)  # Circle(radius=4.00, diameter=8.00, area=50.27)
print(c2)  # Circle(radius=5.00, diameter=10.00, area=78.54)
print(c3)  # Circle(radius=9.00, diameter=18.00, area=254.47)

print(c1 < c2)  # True
print(c1 == Circle(radius=4))  # True

circles = [c2, c1, c3]
print(sorted(circles))  # sorted by radius


# Bonus

import turtle

circles = [Circle(radius=40), Circle(radius=20), Circle(radius=60)]
sorted_circles = sorted(circles)

t = turtle.Turtle()
t.speed("fastest")

for c in sorted_circles:
    t.penup()
    t.goto(0, -c.radius)  # center each circle
    t.pendown()
    t.circle(c.radius)

turtle.done()