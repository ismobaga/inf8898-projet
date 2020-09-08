import random
from utils import *
from collections import defaultdict

class Individu:
    def __init__(self, indices, fitness):
        """

        Args:
            indices ([]): [description]
            fitness (Fitness): [description]
        """
        self.Indices = indices
        self.Fitness = fitness

class Fitness:
    def __init__(self, energie, delais):
        self.energie = energie
        self.delais = delais
    def __lt__(self, other):
        if self.energie != other.energie:
            return self.energie < other.energie
        return self.delais < other.delais
    def val(self):
        return (self.energie, self.delais)

def energy_genetic(reqs):
    """Maximum d'energy d'un ensemble de requetes

    Args:
        reqs ([](a, d, m, e)): Un ensmble de requetes

    Returns:
        [float]: L'energie qui prends pour envoye cet ensemble
    """

    E = defaultdict(lambda : 0)
    # Penalisation sil ya des envoie au meme instant comsomme es deux energie
    for r in reqs:
        E[r[2]] = max(r[3], E[r[2]])

    return sum(E.values())
def get_fitness(p):
    e = 0
    d = 0
    for envoie in p:
        e += energy_genetic(np.array(envoie))
        d += 0# delais(np.array(envoie))
    
    return Fitness(e, d)
def _generer_part_from_index(indexes, entries):
    """Generer une partition en ontion des indices

    Args:
        indexes ([]): Liste d'indice
        entries ([](a, d, m, e)): L'ensemble des demandes

    Returns:
        []: une partion 
    """
    idx = [0] + indexes + [None]

    return [
        entries[idx[j]:idx[j+1]] for j in range((len(idx) - 1)) 
    ]

def _generate_individu( set_size, eniries, getFitness):

    while True:
        indvIdx = []
        idx = list(range(set_size+1))
        # Nombre de sous ensemble
        nbSub = random.sample(idx, 1)[0]
        # generer une combinaison d'indices
        indvIdx.extend(random.sample(idx[1:], nbSub))
        indvIdx.sort()
        p = _generer_part_from_index(indvIdx, eniries)
        return Individu(indvIdx, getFitness(p))


def _init_pop(length, entries, getFitness):
    pop = []
    while len(pop) < length:
        indiv = _generate_individu(len(entries), entries, getFitness)
        pop += [indiv]
    return pop

def _mutate(indiv, entries, getFitness):
    childIndices = indiv.Indices[:]
    childIndices2 = indiv.Indices[:]
    if len(indiv.Indices):
        # seletion un sous ensemble
        subSetIdx = random.randrange(0, len(indiv.Indices))
        # augmenter a taille
        childIndices[subSetIdx] = min(len(entries)-1, childIndices[subSetIdx] + 1)
        childIndices = list(set(childIndices))
        p = _generer_part_from_index(childIndices, entries)
        fitness1 = getFitness(p)
        i1 = Individu(childIndices, fitness1)

        # diminuer la taille
        childIndices2[subSetIdx] = max(1, childIndices2[subSetIdx] -1)
        childIndices2 = list(set(childIndices2))
        p = _generer_part_from_index(childIndices2, entries)
        fitness2 = getFitness(p)
        i2 = Individu(childIndices2, fitness2)
        return i1 if fitness1 < fitness2 else i2
    
    subSetIdx = random.randrange(1, len(entries))
    indices = [subSetIdx]
    p = _generer_part_from_index(indices, entries)
    fitness = getFitness(p)
    i3 = Individu(indices, fitness)
    return i3

def _fit(popsize, new_child, generate_pop, its=100):
    def bestFit(p):
        i = 0 #Mini satisfaite

        for j, indv in enumerate(p):
            if indv.Fitness < p[i].Fitness:
                i = j
        return i, p[i]

    pop = generate_pop(popsize)
    _, best = bestFit(pop)
    for i in range(its):
        for j in range(popsize):
            child = new_child(pop[j])
            pop[j] = child
            if  child.Fitness < best.Fitness:
                best = child
        yield best

def genetic(entries, maxIter=100, getFitness=get_fitness):
    random.seed()

    def fnMutate(parent):
        return _mutate(parent, entries, getFitness)

    def fnGenerateParent(popsize=1):
        if popsize == 1 :
            return _generate_individu(len(entries), entries, getFitness)
        return _init_pop(popsize, entries, getFitness)


    for individu in _fit(10, fnMutate, fnGenerateParent, maxIter):
        pass
    return individu.Fitness.val()

entries =[
           [0, 3, 1, 4],
           [0, 2, 1, 1],
           [1, 4, 1, 3],
           [1, 3, 2, 4], 
           [2, 4, 3, 5],
           [2, 2, 2, 3]
]
# popss = _init_pop(10, entries, get_fitness)

# r = genetic(entries)
# print(r)

