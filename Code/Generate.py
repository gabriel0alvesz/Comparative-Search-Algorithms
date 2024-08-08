import networkx as nx
import math as mh
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
    
    def generate_graph(self):
        
        self.maze_matrix.generate_obstacles() # gera os obstaculos da matriz
        self.maze_matrix.print_maze()

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
    
    def print_graph(self):
        
        # Necessário usar desta forma as posições devido ao matplotlib
        pos = {node: (node.position_y, -node.position_x) for node in self.maze_graph.nodes}
        labels = {node: node.name for node in self.maze_graph.nodes}
        edge_labels = nx.get_edge_attributes(self.maze_graph, 'weight')

        nx.draw(self.maze_graph, pos, labels=labels, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
        nx.draw_networkx_edge_labels(self.maze_graph, pos, edge_labels=edge_labels)
        
        plt.savefig("assets/matrix_to_graph.png")
        plt.show()

    def euclidean_distance_heuristic(self, node_actual: Node):
        goal_position = self.size_maze-1
        distance = mh.sqrt( ((goal_position - node_actual.position_x)**2) + ((goal_position - node_actual.position_y)**2))

        return distance;
        
if __name__ == "__main__":

    gerador = Generate(10)

    gerador.generate_graph()
    gerador.edges_graph()

    gerador.print_graph()