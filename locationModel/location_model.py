from docplex.mp.model import Model

class LocationModel():
    def __init__(self, data):
        self.distances = data['distances']
        self.dwellings_count = data['dwellings_count']
        self.locations = data['locations']

        self.model = Model(name='Localizacoes')

    def solve(self):
        self.add_variables()
        self.add_constraints()
        self.add_objective()

        if not self.model.solve():
            return None

        designated_locations = self.generate_designated_locations()

        return {
            'objectives': self.model.solution.multi_objective_values,
            'designated_locations': designated_locations,
        }

    def add_variables(self):
        self.model.designated = self.model.binary_var_matrix(
            len(self.locations), self.dwellings_count, 'localizacoes_designadas'
        )

    def add_constraints(self):
        # constraint lim_localizacao
        for i in range(self.dwellings_count):
            summation = self.model.sum(
                self.model.designated[ (j, i) ] * self.locations[j]['installed'] for j in range(len(self.locations))
            )

            self.model.add_constraint(summation == 1, 'lim_localizacao_%s' % i)

    def add_objective(self):
        distance_objective = self.model.sum(
            self.distances[i][j] * self.model.designated[ (i, j) ] for j in range(self.dwellings_count) for i in range(len(self.locations))
        )

        self.model.add_kpi(distance_objective, 'distancia')

        self.model.minimize(distance_objective)

    def generate_designated_locations(self):
        designated_locations = []

        for i in range(len(self.locations)):
            locations_row = []

            for j in range(self.dwellings_count):
                locations_row.append(self.model.solution.get_value(
                    'localizacoes_designadas_%s_%s' % (i, j)
                ))

            designated_locations.append(locations_row)

        return designated_locations
