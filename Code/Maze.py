import random
from Node import Node

class Maze:

    _size: int
    _matrix_maze: list[list]

    def __init__(self, size):
        self._size = size
        self._matrix_maze = [[0 for j in range(0, self.get_size())]  for i in range(0,self.get_size())]
        
        for i in range(0,size):
            for j in range(0,size):
                self._matrix_maze[i][j] = Node(0,0,i,j)

    def get_size(self) -> int:
        return self._size
    
    def print_maze(self):
        for line in self._matrix_maze:
            for node in line:
                print(f"{node.name} => {node.value}",end="  ",)
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
                self._matrix_maze[line_num][column_num].value = -1
                
         

if __name__ == "__main__":

    labirinto = Maze(10)

    labirinto.generate_obstacles()
    labirinto.print_maze()
     