class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            # Vector-vector addition
            return Vector2D(self.x + other.x,  self.y + other.y)
            # Vector-tuple addition
        elif isinstance(other, tuple):
            return Vector2D(self.x + other[0],  self.y + other[1])
        return NotImplemented

    def __radd__(self, other):
            # Tuple-vector addition
        if isinstance(other, tuple):
            return Vector2D(self.x + other[0],  self.y + other[1])
        return NotImplemented

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"





v1 = Vector2D(1,2)
print(v1)
v2 = Vector2D(2, 3)
t1 = (1, 4)
addition1 = v1 + v2
print("____________")
print(addition1)
addition2 = v1 + t1
print(addition2)