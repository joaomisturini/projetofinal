import json, unittest
from locationModel import LocationModel

class TestLocationModel(unittest.TestCase):
    def test_solution(self):
        input_file = open('./input.json')

        location_model = LocationModel(json.loads(input_file.read()))
        result = location_model.solve()

        input_file.close()

        self.assertEqual(result['objectives'], [ 160 ])
        self.assertEqual(result['designated_locations'][0][2], 1.0)
        self.assertEqual(result['designated_locations'][0][3], 1.0)
        self.assertEqual(result['designated_locations'][2][0], 1.0)
        self.assertEqual(result['designated_locations'][3][1], 1.0)
