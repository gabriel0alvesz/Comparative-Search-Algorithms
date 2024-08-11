import Generate
import statistics

import time
import tracemalloc

def memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Uso de memória de {func.__name__}: {peak / 10**6:.6f} MB (pico)")
        return result, peak/10**6
    return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Inicia a contagem de tempo
        result = func(*args, **kwargs)
        end_time = time.time()  # Termina a contagem de tempo
        elapsed_time = end_time - start_time
        print(f"Tempo de execução de {func.__name__}: {elapsed_time:.6f} segundos")
        return result, elapsed_time
    return wrapper

#@timeit
@memory_usage
def test_bfs(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.bfs(start, goal)

#@timeit
@memory_usage
def test_dfs(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.dfs(start, goal)
    
#@timeit
@memory_usage
def test_greedy(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.edges_graph()
        gerador.greedy_search(start, goal)
    
#@timeit
@memory_usage
def test_a_star(test_range, start, goal):
    for i in range(test_range):
        gerador = Generate.Generate(10)
        gerador.generate_graph(i)
        gerador.a_star(start, goal)

if __name__ == "__main__":
# Gera dados de tempo gasto e uso de memória

    # BFS
    print('BFS: ')
    memory_bfs = []
    # time_bfs = []
    for _ in range(30):
        _, elapsed_time = test_bfs(50,(0,0),(9,9))
        memory_bfs.append(elapsed_time)
        # time_bfs.append(elapsed_time)

    mean_memory_bfs = statistics.mean(memory_bfs)
    stdev_memory_bfs = statistics.stdev(memory_bfs) if len(memory_bfs) > 1 else 0
    
    # mean_time_bfs = statistics.mean(time_bfs)
    # stdev_time_bfs = statistics.stdev(time_bfs) if len(time_bfs) > 1 else 0
    # print(f"Tempo médio de execução: {mean_time_bfs:.6f} segundos")
    # print(f"Desvio padrão do tempo de execução: {stdev_time_bfs:.6f} segundos")    
    
    print(f"Memória Média de execução: {mean_memory_bfs:.6f} MB")
    print(f"Desvio padrão da memória de execução: {stdev_memory_bfs:.6f} MB")
    print('\n')

    # DFS
    print('DFS: ')
    memory_dfs = []
    # time_dfs = []
    for _ in range(30):
        _, elapsed_time = test_dfs(50,(0,0),(9,9))
        memory_dfs.append(elapsed_time)
        # time_dfs.append(elapsed_time)

    mean_memory_dfs = statistics.mean(memory_dfs)
    stdev_memory_dfs = statistics.stdev(memory_dfs) if len(memory_dfs) > 1 else 0

    # mean_time_dfs = statistics.mean(time_dfs)
    # stdev_time_dfs = statistics.stdev(time_dfs) if len(time_dfs) > 1 else 0
    # print(f"Tempo médio de execução: {mean_time_dfs:.6f} segundos")
    # print(f"Desvio padrão do tempo de execução: {stdev_time_dfs:.6f} segundos")  

    print(f"Memória Média de execução: {mean_memory_dfs:.6f} MB")
    print(f"Desvio padrão da memória de execução: {stdev_memory_dfs:.6f} MB")
    print('\n')

    # Greedy
    print('Greedy: ')
    memory_greedy = []
    # time_greedy = []
    for _ in range(30):
        _, elapsed_time = test_greedy(50,(0,0),(9,9))
        memory_greedy.append(elapsed_time)
        # time_greedy.append(elapsed_time)

    mean_memory_greedy = statistics.mean(memory_greedy)
    stdev_memory_greedy = statistics.stdev(memory_greedy) if len(memory_greedy) > 1 else 0
    
    # mean_time_greedy = statistics.mean(time_greedy)
    # stdev_time_greedy = statistics.stdev(time_greedy) if len(time_greedy) > 1 else 0
    # print(f"Tempo médio de execução: {mean_time_greedy:.6f} segundos")
    # print(f"Desvio padrão do tempo de execução: {stdev_time_greedy:.6f} segundos")      

    print(f"Memória Média de execução: {mean_memory_greedy:.6f} MB")
    print(f"Desvio padrão da memória de execução: {stdev_memory_greedy:.6f} MB")
    print('\n')

    # DFS
    print('A*: ')
    memory_a = []
    # time_a = []
    for _ in range(30):
        _, elapsed_time = test_a_star(50,(0,0),(9,9))
        memory_a.append(elapsed_time)
        # time_a.append(elapsed_time)

    mean_memory_a = statistics.mean(memory_a)
    stdev_memory_a = statistics.stdev(memory_a) if len(memory_a) > 1 else 0
    
    # mean_time_a = statistics.mean(time_a)
    # stdev_time_a = statistics.stdev(time_a) if len(time_a) > 1 else 0
    # print(f"Tempo médio de execução: {mean_time_a:.6f} segundos")
    # print(f"Desvio padrão do tempo de execução: {stdev_time_a:.6f} segundos")      
    
    print(f"Memória Média de execução: {mean_memory_a:.6f} MB")
    print(f"Desvio padrão da memória de execução: {stdev_memory_a:.6f} MB")
    print('\n')