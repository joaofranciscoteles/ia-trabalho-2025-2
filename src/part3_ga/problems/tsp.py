import random 
import math

cities = [
    (0,0),
    (1,5),
    (5,3),
    (6,7),
    (2,9),
    (8,1),
    (4,6),
    (7,8)
]

N = len(cities)

def dist(a,b):
    ax,ay = cities[a]
    bx,by = cities[b]

    return math.sqrt((ax-bx)**2 + (ay-by)**2)

def total_distance(ind):

    d=0

    for i in range(N):
        a=ind[i]
        b = ind[(i+1) % N]

        d +=dist(a,b)
    
    return d

def fitness(ind):
    return -total_distance(ind)

def create_ind():
    lst=list(range(N))
    random.shuffle(lst)
    return lst

def crossover(a,b):

    p1=random.randint(0,N-2)
    p2=random.randint(p1+1,N-1)

    child=[None]*N

    child[p1:p2]=a[p1:p2]

    fill = [x for x in b if x not in child]

    k=0

    for i in range (N):
        if child[i] is None:
            child[i]= fill[k]
            k+=1
    return child,child[:]

def mutate(ind):
   
    i = random.randint(0,N-1)
    j = random.randint(0,N-1)
    
    ind[i], ind[j] = ind[j], ind[i]
    return ind
            