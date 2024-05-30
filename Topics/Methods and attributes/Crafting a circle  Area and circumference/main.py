import math

# Define the Circle class with radius as a parameter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Define the get_area method
    def get_area(self):
        return math.pi * self.radius ** 2

    # Define the get_circumference method
    def get_circumference(self):
        return 2 * math.pi * self.radius

# Get the radius from the user
radius = float(input())

# Create an instance of the Circle class with the given radius
circle = Circle(radius)

# Call the get_area method and print the result rounded to 2 decimal places
print(format(circle.get_area(), '.2f'))

# Call the get_circumference method and print the result rounded to 2 decimal places
print(format(circle.get_circumference(), '.2f'))