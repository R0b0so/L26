class Circle:
    def __init__(self, radius):
        self.radius = radius
circle1 = Circle(int(input("Enter any radius")))
print("circumference: ",circle1.radius * 3.14 * 2)
print("area:",3.14 * circle1.radius ** 2)