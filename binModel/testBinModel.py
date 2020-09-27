import json, unittest
from binModel import BinModel

class TestBinModel(unittest.TestCase):
    def test_tolerance_0(self):
        input_file = open('./input.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(0)

        input_file.close()

        self.assertEqual(result['objectives'], [ 50, 4 ])
        self.assertEqual(result['installed_bins'][0][0], 1.0)
        self.assertEqual(result['installed_bins'][2][2], 1.0)
        self.assertEqual(result['installed_bins'][3][3], 1.0)
        self.assertEqual(result['installed_bins'][6][9], 1.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)
        self.assertEqual(result['designated_locations'][3][3], 1.0)
        self.assertEqual(result['designated_locations'][6][1], 1.0)

    def test_tolerance_20(self):
        input_file = open('./input.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(20)

        input_file.close()

        self.assertEqual(result['objectives'], [ 70, 3 ])
        self.assertEqual(result['installed_bins'][0][0], 1.0)
        self.assertEqual(result['installed_bins'][2][2], 1.0)
        self.assertEqual(result['installed_bins'][6][9], 1.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)
        self.assertEqual(result['designated_locations'][6][1], 1.0)
        self.assertEqual(result['designated_locations'][6][3], 1.0)

    def test_tolerance_60(self):
        input_file = open('./input.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(60)

        input_file.close()

        self.assertEqual(result['objectives'], [ 110, 2 ])
        self.assertEqual(result['installed_bins'][1][5], 1.0)
        self.assertEqual(result['installed_bins'][6][3], 1.0)
        self.assertEqual(result['designated_locations'][1][0], 1.0)
        self.assertEqual(result['designated_locations'][1][2], 1.0)
        self.assertEqual(result['designated_locations'][6][1], 1.0)
        self.assertEqual(result['designated_locations'][6][3], 1.0)
