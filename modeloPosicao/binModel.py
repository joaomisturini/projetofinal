from docplex.mp.model import Model

class BinModel():
    def __init__(self, data):
        self.bins = data['bins']
        self.distances = data['distances']
        self.dwellings = data['dwellings']
        self.locations = data['locations']
        self.maxDistance = data['maxDistance']

        self.model = Model(name='Lixeiras')

    def solve(self, tolerance = 0):
        self.addVariables()
        self.addConstraints()
        self.addObjectives(tolerance)

        if not self.model.solve():
            return None

        installedBins = self.generateInstalledBins()
        designatedLocations = self.generateDesignatedLocations()

        return {
            'objectives': self.model.solution.multi_objective_values,
            'installedBins': installedBins,
            'designatedLocations': designatedLocations,
        }

    def addVariables(self):
        self.model.installed = self.model.binary_var_matrix(
            len(self.locations), len(self.bins), 'lixeiras_instaladas'
        )

        self.model.designated = self.model.binary_var_matrix(
            len(self.locations), len(self.dwellings), 'localizacoes_designadas'
        )

    def addConstraints(self):
        # constraint lim_volume
        for i in range(len(self.locations)):
            sumBins = self.model.sum(
                self.bins[j]['capacity'] * self.model.installed[ (i, j) ] for j in range(len(self.bins))
            )

            sumDwellings = self.model.sum(
                self.dwellings[j]['volume'] * self.model.designated[ (i, j) ] for j in range(len(self.dwellings))
            )

            self.model.add_constraint(sumBins >= sumDwellings, 'lim_volume_%s' % i)

        # constraint lim_espaco
        for i in range(len(self.locations)):
            summation = self.model.sum(
                self.bins[j]['size'] * self.model.installed[ (i, j) ] for j in range(len(self.bins))
            )

            self.model.add_constraint(summation <= self.locations[i]['space'], 'lim_espaco_%s' % i)

        # constraint lim_localizacao
        for i in range(len(self.dwellings)):
            summation = self.model.sum(
                self.model.designated[ (j, i) ] for j in range(len(self.locations))
            )

            self.model.add_constraint(summation == 1, 'lim_localizacao_%s' % i)

        # constraint lim_lixeiras
        for i in range(len(self.locations)):
            for j in range(len(self.dwellings)):
                summation = self.model.sum(
                    self.model.installed[ (i, k) ] for k in range(len(self.bins))
                )

                self.model.add_constraint(
                    summation >= self.model.designated[ (i, j) ], 'lim_lixeiras_%s_%s' % (i, j)
                )

        # constraint lim_distancia
        for i in range(len(self.locations)):
            for j in range(len(self.dwellings)):
                setDistance = self.distances[i][j] * self.model.designated[ (i, j) ]

                self.model.add_constraint(
                    setDistance <= self.maxDistance, 'lim_distancia_%s_%s' % (i, j)
                )

        # constraint lim_instalacao
        for i in range(len(self.bins)):
            summation = self.model.sum(
                self.model.installed[ (j, i) ] for j in range(len(self.locations))
            )

            self.model.add_constraint(summation <= 1, 'lim_instalacao_%s' % i)

    def addObjectives(self, tolerance):
        # objective distancia
        distanceObjective = self.model.sum(
            self.distances[i][j] * self.model.designated[ (i, j) ] for j in range(len(self.dwellings)) for i in range(len(self.locations))
        )

        self.model.add_kpi(distanceObjective, 'distancia')

        # objective lixeiras
        binsObjective = self.model.sum(
            self.model.installed[ (i, j) ] for j in range(len(self.bins)) for i in range(len(self.locations))
        )

        self.model.add_kpi(binsObjective, 'lixeiras')

        # minimize
        self.model.minimize_static_lex([
            distanceObjective, binsObjective,
        ], abstols=tolerance)

    def generateInstalledBins(self):
        installedBins = []

        for i in range(len(self.locations)):
            binsRow = []

            for j in range(len(self.bins)):
                binsRow.append(self.model.solution.get_value(
                    'lixeiras_instaladas_%s_%s' % (i, j)
                ))

            installedBins.append(binsRow)

        return installedBins

    def generateDesignatedLocations(self):
        designatedLocations = []

        for i in range(len(self.locations)):
            locationsRow = []

            for j in range(len(self.dwellings)):
                locationsRow.append(self.model.solution.get_value(
                    'localizacoes_designadas_%s_%s' % (i, j)
                ))

            designatedLocations.append(locationsRow)

        return designatedLocations
