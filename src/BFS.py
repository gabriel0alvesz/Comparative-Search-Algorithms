import networkx as nx
import Generate

if __name__ == "__main__":

    for i in range(50):
        aux_labirinto = Generate.Generate(10)
        aux_labirinto.generate_graph(i)
        aux_labirinto.edges_graph_without_obstacle()
        print(f'Grafo {i}: ')
        start = next(node for node in aux_labirinto.maze_graph.nodes if (node.position_x, node.position_y) == (0,0))
        aux_bfs = nx.bfs_tree(aux_labirinto.maze_graph,start)
        try:
            goal = next(node for node in aux_bfs.nodes if (node.position_x, node.position_y) == (9,9))
        except:
            goal = "Não é possível"
        print(goal)