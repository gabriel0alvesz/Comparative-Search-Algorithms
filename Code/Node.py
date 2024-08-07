class Node:
    temp_weight: float
    value: int
    position_x: int
    position_y: int
    name: str

    def __init__(self, weight: float, value: int, x: int, y: int):
        self.name = f"{x},{y}"
        self.temp_weight = weight
        self.value = value
        self.position_x = x
        self.position_y = y
    
    
    def __hash__(self):
        return hash((self.position_x, self.position_y))

    # Compara nós com base em todos os atributos
    def __eq__(self, other):
        return (self.position_x, self.position_y) == (other.position_x, other.position_y)        
    
    def __str__(self):
        return f"(x:{self.position_x}, y:{self.position_y})"