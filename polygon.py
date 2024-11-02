class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_num_sides(self):
        return self.sides

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")