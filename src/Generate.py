import networkx as nx
import heapq
import matplotlib.pyplot as plt
from Maze import Maze
from Node import Node

class Generate:
    """Classe auxiliadora: Representa o labirinto no formato de grafo ponderado\n
        Fornece métodos e funções aplicavéis ao grafo.
    """

    def __init__(self, size_maze: int):
        self.maze_matrix = Maze(size_maze)
        self.size_maze = size_maze
        self.positions_node = dict()
        self.maze_graph = nx.Graph()
    
    def generate_graph(self, num_file: int):
        
        self.maze_matrix.build_maze(num_file=num_file)
        # self.maze_matrix.print_maze()

        for i in range(0, self.size_maze):
            for j in range(0, self.size_maze):
                temp_node = self.maze_matrix[i][j]
                self.maze_graph.add_node(temp_node, label=temp_node.name)
                self.positions_node[(i,j)] = temp_node
    
    def edges_graph(self):

        for i in range(0,self.size_maze):
            for j in range(0,self.size_maze):
                node = self.positions_node[(i, j)]

                if i > 0:  # acima
                    neighbor = self.positions_node[(i - 1, j)]
                    self.maze_graph.add_edge(node, neighbor)
                if i < self.size_maze-1:  # abaixo
                    neighbor = self.positions_node[(i + 1, j)]
                    self.maze_graph.add_edge(node, neighbor)
                if j > 0:  # esquerda
                    neighbor = self.positions_node[(i, j - 1)]
                    self.maze_graph.add_edge(node, neighbor)
                if j < self.size_maze-1:  # direita
                    neighbor = self.positions_node[(i, j + 1)]
                    self.maze_graph.add_edge(node, neighbor)

    def edges_graph_without_obstacle(self):
        for i in range(0, self.size_maze):
            for j in range(0, self.size_maze):
                node = self.positions_node[(i, j)]
                if node.obstacle != -1:
                    # Verifica o vizinho acima
                    if i > 0:
                        neighbor = self.positions_node[(i - 1, j)]
                        if neighbor.obstacle != -1:
                            self.maze_graph.add_edge(node, neighbor)
                    
                    # Verifica o vizinho abaixo
                    if i < self.size_maze - 1:
                        neighbor = self.positions_node[(i + 1, j)]
                        if neighbor.obstacle != -1:
                            self.maze_graph.add_edge(node, neighbor)
                    
                    # Verifica o vizinho à esquerda
                    if j > 0:
                        neighbor = self.positions_node[(i, j - 1)]
                        if neighbor.obstacle != -1:
                            self.maze_graph.add_edge(node, neighbor)
                    
                    # Verifica o vizinho à direita
                    if j < self.size_maze - 1:
                        neighbor = self.positions_node[(i, j + 1)]
                        if neighbor.obstacle != -1:
                            self.maze_graph.add_edge(node, neighbor)

    def print_graph(self):
        plt.figure()

        # Necessário usar desta forma as posições devido ao matplotlib
        pos = {node: (node.position_y, -node.position_x) for node in self.maze_graph.nodes}
        labels = {node: node.repr_obstacle() for node in self.maze_graph.nodes}
        edge_labels = nx.get_edge_attributes(self.maze_graph, 'weight')

        nx.draw(self.maze_graph, pos, labels=labels, with_labels=True, node_size=400, node_color='skyblue', font_size=10, font_color='black')
        nx.draw_networkx_edge_labels(self.maze_graph, pos, edge_labels=edge_labels)
        

        plt.savefig("./assets/matrix_to_graph.png")
        

    def manhattan_distance_heuristic(self, node_actual: Node, goal_position: Node):
        distance = abs(goal_position.position_x - node_actual.position_x) + abs(goal_position.position_y - node_actual.position_y)
        return distance
    
    def greedy_search(self, initial_position: tuple, finish_position: tuple):
        
        start = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == initial_position)
        goal = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == finish_position)

        # Fila de prioridade 
        open_set = []
        heapq.heappush(open_set, (0, start))

        # Rastrear o caminho
        came_from = dict()
        came_from[start] = None

        while open_set:
            # Tupla de proriade e proximo nó
            priority, current = heapq.heappop(open_set)
 
            if current == goal:
                # Reconstrói o caminho do objetivo até o início
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]  # Retorna o caminho na ordem correta

            # vizinhos do nó atual
            for neighbor in self.maze_graph.neighbors(current):
                if neighbor.obstacle != -1 and neighbor not in came_from:
                    
                    priority = self.manhattan_distance_heuristic(neighbor, goal)
                    
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current

        return None


    def a_star(self, initial_position: tuple, finish_position: tuple):
        
        self.edges_graph_without_obstacle()
        
        start = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == initial_position)
        goal = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == finish_position)

        try:
            caminho = nx.astar_path(self.maze_graph, start, goal, self.manhattan_distance_heuristic)
        except:
            caminho = "Não é possível"
        print(caminho)


    def bfs(self,initial_position: tuple, finish_position: tuple):
        
        self.edges_graph_without_obstacle()
        
        start = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == initial_position)
        goal = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == finish_position)
        
        aux_bfs = nx.bfs_tree(self.maze_graph,start)
        
        try:
            next(node for node in aux_bfs.nodes if node == goal)
            possible = "É possível"
        except:
            possible = "Não é possível"
        
        print(possible)

    def dfs(self,initial_position: tuple, finish_position: tuple):

        self.edges_graph_without_obstacle()
        
        start = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == initial_position)
        goal = next(node for node in self.maze_graph.nodes if (node.position_x, node.position_y) == finish_position)
        
        aux_bfs = nx.dfs_tree(self.maze_graph,start)
        
        try:
            next(node for node in aux_bfs.nodes if node == goal)
            possible = "É possível"
        except:
            possible = "Não é possível"
        
        print(possible)
                
if __name__ == "__main__":

    gerador = Generate(10)

    gerador.generate_graph(2)
    
    gerador.a_star((0,0), (9,9))

    gerador.print_graph()