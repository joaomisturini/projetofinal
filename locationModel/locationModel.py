from docplex.mp.model import Model

class LocationModel():
    def __init__(self, data):
        self.distances = data['distances']
        self.dwellingsCount = data['dwellingsCount']
        self.locations = data['locations']

        self.model = Model(name='Localizacoes')

    def solve(self):
        self.addVariables()
        self.addConstraints()
        self.addObjective()

        if not self.model.solve():
            return None

        designatedLocations = self.generateDesignatedLocations()

        return {
            'objectives': self.model.solution.multi_objective_values,
            'designatedLocations': designatedLocations,
        }

    def addVariables(self):
        self.model.designated = self.model.binary_var_matrix(
            len(self.locations), self.dwellingsCount, 'localizacoes_designadas'
        )

    def addConstraints(self):
        # constraint lim_localizacao
        for i in range(self.dwellingsCount):
            summation = self.model.sum(
                self.model.designated[ (j, i) ] * self.locations[j]['installed'] for j in range(len(self.locations))
            )

            self.model.add_constraint(summation == 1, 'lim_localizacao_%s' % i)

    def addObjective(self):
        distanceObjective = self.model.sum(
            self.distances[i][j] * self.model.designated[ (i, j) ] for j in range(self.dwellingsCount) for i in range(len(self.locations))
        )

        self.model.add_kpi(distanceObjective, 'distancia')

        self.model.minimize(distanceObjective)

    def generateDesignatedLocations(self):
        designatedLocations = []

        for i in range(len(self.locations)):
            locationsRow = []

            for j in range(self.dwellingsCount):
                locationsRow.append(self.model.solution.get_value(
                    'localizacoes_designadas_%s_%s' % (i, j)
                ))

            designatedLocations.append(locationsRow)

        return designatedLocations
