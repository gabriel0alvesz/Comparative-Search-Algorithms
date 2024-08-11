import Generate

import time
import tracemalloc

def memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Uso de memória de {func.__name__}: {peak / 10**6:.6f} MB (pico)")
        return result
    return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Inicia a contagem de tempo
        result = func(*args, **kwargs)
        end_time = time.time()  # Termina a contagem de tempo
        elapsed_time = end_time - start_time
        print(f"Tempo de execução de {func.__name__}: {elapsed_time:.6f} segundos")
        return result
    return wrapper

@timeit
@memory_usage
def test_bfs(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.bfs(start, goal)

@timeit
@memory_usage
def test_dfs(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.dfs(start, goal)
    
@timeit
@memory_usage
def test_greedy(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.edges_graph()
        print(gerador.greedy_search(start, goal))
    
@timeit
@memory_usage
def test_a_star(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.a_star(start, goal)

if __name__ == "__main__":

    # BFS
    print('BFS: ')
    test_bfs(50,(0,0),(9,9))
    print('\n')
    
    # DFS
    print('DFS: ')
    test_dfs(50,(0,0),(9,9))
    print('\n')

    # Greedy
    print('Greedy: ')
    test_greedy(50,(0,0),(9,9))
    print('\n')
    
    # DFS
    print('A*: ')
    test_a_star(50,(0,0),(9,9))
    print('\n')