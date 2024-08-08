class Node:
    weight: float
    obstacle: int
    position_x: int
    position_y: int
    name: str

    def __init__(self, weight: float, x: int, y: int):
        self.weight = weight 
        self.position_x = x
        self.position_y = y
        self.name = f"{self.position_x},{self.position_y}"
    
    
    def __hash__(self):
        return hash((self.position_x, self.position_y))

    # Compara nós com base em todos os atributos
    def __eq__(self, other):
        return (self.position_x, self.position_y) == (other.position_x, other.position_y)        
    
    def __str__(self):
        return f"(x:{self.position_x}, y:{self.position_y})"
