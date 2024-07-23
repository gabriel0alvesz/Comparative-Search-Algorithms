import random

class Maze:

    _size: int
    _matrix_maze: list[list]

    def __init__(self, size):
        self._size = size
        self._matrix_maze = [[ 0 for j in range(0, self.get_size())]  for i in range(0,self.get_size())]

    def get_size(self) -> int:
        return self._size
    
    def print_maze(self):
        for l in self._matrix_maze:
            for num in l:
                print(f"{num} ",end="",)
            print()
    
    
    def generate_obstacles(self):
        """Faz 60% da Matriz se tornar obstaculos"""    
        
        line_num = random.randint(0, 10)
        column_num = random.randint(0, 10)

        print(line_num)
        print(column_num)
         


if __name__ == "__main__":

    labirinto = Maze(10)

    print(labirinto.get_size())
    # labirinto.print_maze()

    labirinto.generate_obstacles()
    