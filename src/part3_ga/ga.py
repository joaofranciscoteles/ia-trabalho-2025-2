import random

class GA:
    
    def __init__(self,pop_size,cx_rate,mut_rate,fitness_fn,create_ind,crossover,mutate,max_iters=1000,seed=42):

        random.seed(seed)

        self.pop = [create_ind() for _ in range (pop_size)]

        self.cx_rate=cx_rate
        self.mut_rate=mut_rate

        self.fitness_fn = fitness_fn  
        self.create_ind = create_ind  
        self.crossover = crossover    
        self.mutate = mutate          
        
        self.max_iters = max_iters  

    def select(self):

        a = random.choice(self.pop)
        b = random.choice(self.pop)

        return a if self.fitness_fn(a) > self.fitness_fn(b) else b
    
    def step(self):
        new = []

        while len(new) < len(self.pop):

            p1 = self.select()
            p2 = self.select()

            c1,c2=p1[:],p2[:]

            if random.random() < self.cx_rate:
                c1,c2=self.crossover(c1,c2)
            if random.random() < self.mut_rate:
                c1 =self.mutate(c1)
            if random.random() < self.mut_rate:
                c2 = self.mutate(c2)
            
            new.append(c1)
            new.append(c2)
        self.pop = new[:len(self.pop)]

    def run(self):

        best = max(self.pop, key=self.fitness_fn)
        history = []  # lista para salvar o melhor fitness de cada geração

        for _ in range(self.max_iters):
            self.step()
        
        # melhor da geração atual
            cand = max(self.pop, key=self.fitness_fn)
            history.append(self.fitness_fn(cand))  # registra fitness da geração

            if self.fitness_fn(cand) > self.fitness_fn(best):
                 best = cand

        return best, self.fitness_fn(best), history

