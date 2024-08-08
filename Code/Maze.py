import random
from Node import Node

class Maze:

    _size: int
    _matrix_maze: list[list]

    def __init__(self, size):
        self._size = size
        self._matrix_maze = [[Node(0, 0, x, y) for y in range(self._size)] for x in range(self._size)]

    def __getitem__(self, index):
        return self._matrix_maze[index]
    
    def __setitem__(self, index, value):
        self._matrix[index] = value
        

    def get_size(self) -> int:
        return self._size
    
    def print_maze(self):
        for line in self._matrix_maze:
            for node in line:
                print(f"{node.name_main()}",end="  ",)
            print()
    
    
    def generate_obstacles(self):
        """Faz 60% da Matriz se tornar obstaculos"""    
        
        cont: int = 0
        aux_dict: dict = {(0,0): True, (9,9): True} # (0,0) -> começa no labirinto e (9,9) -> sai do labirinto

        while cont < ((self.get_size()**2)*0.6):
            line_num = random.randint(0, 9)
            column_num = random.randint(0, 9)

            if aux_dict.get((line_num,column_num)) != True:
                cont += 1
                
                ## Como fazer o nó que será obstaculo, assumir o -1 e o name alterar
                temp_node: Node = Node(0, -1, line_num,column_num);
                self._matrix_maze[line_num][column_num] = temp_node
                
                
         

if __name__ == "__main__":

    labirinto = Maze(10)

    labirinto.generate_obstacles()
    labirinto.print_maze()
     