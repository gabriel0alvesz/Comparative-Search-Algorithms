import random
from Node import Node

QTD_MAZES = 50

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
                print(f"{node.repr_obstacle()}",end="  ",)
            print()
    
    def build_maze(self, num_file: int) -> list:
        
        aux_matrix = list()
        
        file_name = f"./Mazes/maze_{num_file}.txt"
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    
                    line_file = list(map(int, line.split()))
                    aux_matrix.append(line_file)
        except:
            print("Erro ao abir o arquivo!")

        self.create_maze_nodes(aux_matrix)
        
            
    def create_maze_nodes(self, aux_matrix: list):
        
        if self._size != len(aux_matrix):
            print("tamanhos diferentes")
        else:
            
            for i in range(0, self._size):
                for j in range(0, self._size):

                    self._matrix_maze[i][j].obstacle = aux_matrix[i][j]

if __name__ == "__main__":

    labirinto = Maze(10)

    labirinto.build_maze(31)

    labirinto.print_maze()