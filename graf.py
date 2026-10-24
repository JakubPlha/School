class Graph:
    def __init__(self, orientovany=False):
        self.uzly = []
        self.hrany = []
        self.orientovany = orientovany

    def add_node(self, uzel):
        if uzel not in self.uzly:
            self.uzly.append(uzel)

    def add_edge(self, a, b, vaha=None):
        if a not in self.uzly:
            self.add_node(a)
        if b not in self.uzly:
            self.add_node(b)

        self.hrany.append((a, b, vaha))

    def analyze(self):
        print("Počet uzlů:", len(self.uzly))
        print("Počet hran:", len(self.hrany))
        print("Orientovaný:", self.orientovany)

        ohodnoceny = False
        for hrana in self.hrany:
            if hrana[2] is not None:
                ohodnoceny = True
                break

        smycky = False
        for hrana in self.hrany:
            if hrana[0] == hrana[1]:
                smycky = True
                break

        print("Ohodnocený:", ohodnoceny)
        print("Obsahuje smyčky:", smycky)

        if len(self.uzly) < 3:
            planarni = True
        elif len(self.hrany) <= 3 * len(self.uzly) - 6:
            planarni = True
        else:
            planarni = False

        print("Planární (orientační kontrola):", planarni)

        barvy = {}

        for uzel in self.uzly:
            pouzite = set()

            for a, b, vaha in self.hrany:
                if a == uzel and b in barvy:
                    pouzite.add(barvy[b])
                if b == uzel and a in barvy:
                    pouzite.add(barvy[a])

            barva = 0
            while barva in pouzite:
                barva += 1

            barvy[uzel] = barva

        if barvy:
            chromatic = max(barvy.values()) + 1
        else:
            chromatic = 0

        print("Chromatické číslo (odhad):", chromatic)


g = Graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")

g.add_edge("A", "B", 5)
g.add_edge("B", "C", 3)
g.add_edge("C", "A", 2)
g.add_edge("A", "A", 1)

g.analyze()
