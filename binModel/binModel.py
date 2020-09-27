from docplex.mp.model import Model

class BinModel():
    def __init__(self, data):
        self.bins = data['bins']
        self.distances = data['distances']
        self.dwellings = data['dwellings']
        self.locations = data['locations']
        self.max_distance = data['max_distance']

        self.model = Model(name='Lixeiras')

    def solve(self, tolerance = 0):
        self.add_variables()
        self.add_constraints()
        self.add_objectives(tolerance)

        if not self.model.solve():
            return None

        installed_bins = self.generate_installed_bins()
        designated_locations = self.generate_designated_locations()

        return {
            'objectives': self.model.solution.multi_objective_values,
            'installed_bins': installed_bins,
            'designated_locations': designated_locations,
        }

    def add_variables(self):
        self.model.installed = self.model.binary_var_matrix(
            len(self.locations), len(self.bins), 'lixeiras_instaladas'
        )

        self.model.designated = self.model.binary_var_matrix(
            len(self.locations), len(self.dwellings), 'localizacoes_designadas'
        )

    def add_constraints(self):
        # constraint lim_volume
        for i in range(len(self.locations)):
            sum_bins = self.model.sum(
                self.bins[j]['capacity'] * self.model.installed[ (i, j) ] for j in range(len(self.bins))
            )

            sum_dwellings = self.model.sum(
                self.dwellings[j]['volume'] * self.model.designated[ (i, j) ] for j in range(len(self.dwellings))
            )

            self.model.add_constraint(sum_bins >= sum_dwellings, 'lim_volume_%s' % i)

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
                set_distance = self.distances[i][j] * self.model.designated[ (i, j) ]

                self.model.add_constraint(
                    set_distance <= self.max_distance, 'lim_distancia_%s_%s' % (i, j)
                )

        # constraint lim_instalacao
        for i in range(len(self.bins)):
            summation = self.model.sum(
                self.model.installed[ (j, i) ] for j in range(len(self.locations))
            )

            self.model.add_constraint(summation <= 1, 'lim_instalacao_%s' % i)

    def add_objectives(self, tolerance):
        # objective distancia
        distance_objective = self.model.sum(
            self.distances[i][j] * self.model.designated[ (i, j) ] for j in range(len(self.dwellings)) for i in range(len(self.locations))
        )

        self.model.add_kpi(distance_objective, 'distancia')

        # objective lixeiras
        bins_objective = self.model.sum(
            self.model.installed[ (i, j) ] for j in range(len(self.bins)) for i in range(len(self.locations))
        )

        self.model.add_kpi(bins_objective, 'lixeiras')

        # minimize
        self.model.minimize_static_lex([
            distance_objective, bins_objective,
        ], abstols=tolerance)

    def generate_installed_bins(self):
        installed_bins = []

        for i in range(len(self.locations)):
            bins_row = []

            for j in range(len(self.bins)):
                bins_row.append(self.model.solution.get_value(
                    'lixeiras_instaladas_%s_%s' % (i, j)
                ))

            installed_bins.append(bins_row)

        return installed_bins

    def generate_designated_locations(self):
        designated_locations = []

        for i in range(len(self.locations)):
            locations_row = []

            for j in range(len(self.dwellings)):
                locations_row.append(self.model.solution.get_value(
                    'localizacoes_designadas_%s_%s' % (i, j)
                ))

            designated_locations.append(locations_row)

        return designated_locations
