import random
import math

# --- CONFIGURAÇÃO DO PROBLEMA ---
# Seed fixa para garantir que as cidades sejam sempre as mesmas (reprodutibilidade)
random.seed(42)

N_CITIES = 20
MAP_SIZE = 100

# Gera 20 cidades com coordenadas (x, y) aleatórias
cities = [(random.randint(0, MAP_SIZE), random.randint(0, MAP_SIZE)) for _ in range(N_CITIES)]

N = len(cities)

# --- OTIMIZAÇÃO: MATRIZ DE DISTÂNCIAS ---
# Pré-calcula a distância entre todas as cidades para evitar contas repetidas
def calculate_dist(a, b):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

# Matriz NxN onde DIST_MATRIX[i][j] é a distância da cidade i para a j
DIST_MATRIX = [[calculate_dist(i, j) for j in range(N)] for i in range(N)]

# --- FUNÇÕES OBJETIVO ---

def total_distance(ind):
    """Calcula a distância total de uma rota (percorre a lista e volta ao início)."""
    d = 0
    for i in range(N):
        # Acessa a matriz pré-calculada
        city_a = ind[i]
        city_b = ind[(i + 1) % N] # O % N garante o retorno à cidade inicial
        d += DIST_MATRIX[city_a][city_b]
    return d

def fitness(ind):
    """O fitness é negativo porque o GA busca MAXIMIZAR, mas nós queremos MINIMIZAR a distância."""
    return -total_distance(ind)

# --- OPERADORES GENÉTICOS ---

def create_ind():
    """Cria um indivíduo aleatório (permutação de 0 a N-1)."""
    lst = list(range(N))
    random.shuffle(lst)
    return lst

def crossover_ox1(parent1, parent2):
    """
    Operador Order Crossover (OX1) para gerar UM filho.
    Preserva uma sub-rota do pai1 e preenche o resto com a ordem do pai2.
    """
    size = len(parent1)
    p1 = random.randint(0, size - 2)
    p2 = random.randint(p1 + 1, size - 1)
    
    child = [None] * size
    
    # Herda o segmento do primeiro pai
    child[p1:p2] = parent1[p1:p2]
    
    # Preenche os buracos com os genes do segundo pai (na ordem em que aparecem)
    fill = [item for item in parent2 if item not in child]
    
    current_fill = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[current_fill]
            current_fill += 1
            
    return child

def crossover(a, b):
    """Gera dois filhos invertendo os papéis dos pais."""
    child1 = crossover_ox1(a, b)
    child2 = crossover_ox1(b, a) # Inverte para gerar diversidade
    return child1, child2

def mutate(ind):
    """Swap Mutation: Troca duas cidades de lugar."""
    new_ind = ind[:] # Cria uma cópia para não alterar o original sem querer
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    
    # Troca
    new_ind[i], new_ind[j] = new_ind[j], new_ind[i]
    return new_ind