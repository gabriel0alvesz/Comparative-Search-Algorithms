import random

SIZE_MAZE = 10

def generate_obstacles(maze: list):
        """Faz 30% da Matriz se tornar obstaculos"""    
        
        cont: int = 0
        aux_dict: dict = {(0,0): True, (9,9): True} # (0,0) -> começa no labirinto e (9,9) -> sai do labirinto

        while cont < ((SIZE_MAZE**2)*0.3):
            line_num = random.randint(0, SIZE_MAZE-1)
            column_num = random.randint(0, SIZE_MAZE-1)

            if aux_dict.get((line_num,column_num)) != True:
                cont += 1
                
                maze_matrix[line_num][column_num] = -1


def print_maze(maze: list):
    for i in range(0, SIZE_MAZE):
        for j in range(0, SIZE_MAZE):
            print(maze_matrix[i][j], end=" ")
        print()



if __name__ == "__main__":

    for i in range(0, 50):
         
        name = f"maze_{i}.txt"

        try: 
            with open(name, 'w') as file:
                file.write(str(SIZE_MAZE)+"\n")

                maze_matrix = [[0 for _ in range(0, SIZE_MAZE)] for _ in range(0, SIZE_MAZE)]

                generate_obstacles(maze_matrix)

                for l in maze_matrix:
                    line = ' '.join(map(str, l))
                    file.write(line+"\n")
        except:
            print("Erro ao abrir arquivo!")
        
