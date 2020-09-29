import json, unittest
from location_model import LocationModel

class TestLocationModel(unittest.TestCase):
    def test_set1_solution(self):
        input_file = open('./testes/teste1.json')

        location_model = LocationModel(json.loads(input_file.read()))
        result = location_model.solve()

        input_file.close()

        self.assertEqual(result['objectives'], [ 160 ])
        self.assertEqual(result['designated_locations'][0][2], 1.0)
        self.assertEqual(result['designated_locations'][0][3], 1.0)
        self.assertEqual(result['designated_locations'][2][0], 1.0)
        self.assertEqual(result['designated_locations'][3][1], 1.0)

    def test_set2_solution(self):
        input_file = open('./testes/teste2.json')

        location_model = LocationModel(json.loads(input_file.read()))
        result = location_model.solve()

        input_file.close()

        self.assertEqual(result['objectives'], [ 175 ])
        self.assertEqual(result['designated_locations'][0][2], 1.0)
        self.assertEqual(result['designated_locations'][0][3], 1.0)
        self.assertEqual(result['designated_locations'][2][0], 1.0)
        self.assertEqual(result['designated_locations'][3][1], 1.0)
