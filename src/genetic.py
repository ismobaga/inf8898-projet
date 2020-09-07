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
    def __gt__(self, other):
        if self.energie != other.energie:
            return self.energie > other.energie
        return self.delais > other.delais
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
    

    return np.max(reqs[:,3])

def _generer_part_from_index(indexes, entries):
    """Generer une partition en ontion des indices

    Args:
        indexes ([]): Liste d'indice
        entries ([](a, d, m, e)): L'ensemble des demandes

    Returns:
        []: une partion 
    """
    idx = [0] + indexes + [None]

    print("index", idx)
    return [
        entries[idx[j]:idx[j+1]] for j in range((len(idx) - 1)) 
    ]

def _generate_parent(length, set_size, eniries):

    while True:
        indvIdx = []
        idx = list(range(set_size+1))
        # Nombre de sous ensemble
        nbSub = random.sample(idx, 1)[0]
        # generer une combinaison d'indices
        indvIdx.extend(random.sample(idx[1:], nbSub))
        indvIdx.sort()
        p = _generer_part_from_index(indvIdx, eniries)
        yield p 

    return None
    
    
    # while len(indv) < nbSub:
    #     sampleSize = min(length - len(genes), len(geneSet))
    #     indv.extend(random.sample(geneSet, sampleSize))
    # fitness = get_fitness(genes)
    # return Chromosome(genes, fitness)


def _init_pop(length, entries, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

def genetic(entries):
    p = _init_pop(10, len(entries))



entries =[
           [0, 3, 1, 4],
           [0, 2, 1, 1],
           [1, 4, 1, 3],
           [1, 3, 2, 4], 
           [2, 4, 3, 5],
           [2, 2, 2, 3]
]

for r in _generate_parent(5, 3, entries):
    print(r)