

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
    def val(self):geneSet
        return (self.energie, self.delais)


def _generate_parent(length, geneSet, get_fitness):
    indv = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _init_pop(length, entries, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

def genetic(entries):
    p = _init_pop(10, len(entries))

            