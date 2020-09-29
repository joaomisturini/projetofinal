import json, unittest
from bin_model import BinModel

class TestBinModel(unittest.TestCase):
    def test_set1_tolerance_0(self):
        input_file = open('./testes/teste1.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(0)

        input_file.close()

        self.assertEqual(result['objectives'], [ 50, 4 ])
        self.assertEqual(result['installed_bins'][0], 1.0)
        self.assertEqual(result['installed_bins'][2], 1.0)
        self.assertEqual(result['installed_bins'][3], 1.0)
        self.assertEqual(result['installed_bins'][6], 1.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)
        self.assertEqual(result['designated_locations'][3][3], 1.0)
        self.assertEqual(result['designated_locations'][6][1], 1.0)

    def test_set1_tolerance_20(self):
        input_file = open('./testes/teste1.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(20)

        input_file.close()

        self.assertEqual(result['objectives'], [ 70, 3 ])
        self.assertEqual(result['installed_bins'][0], 1.0)
        self.assertEqual(result['installed_bins'][2], 1.0)
        self.assertEqual(result['installed_bins'][3], 1.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][2][1], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)
        self.assertEqual(result['designated_locations'][3][3], 1.0)

    def test_set1_tolerance_60(self):
        input_file = open('./testes/teste1.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(60)

        input_file.close()

        self.assertEqual(result['objectives'], [ 110, 2 ])
        self.assertEqual(result['installed_bins'][0], 1.0)
        self.assertEqual(result['installed_bins'][6], 1.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][0][2], 1.0)
        self.assertEqual(result['designated_locations'][6][1], 1.0)
        self.assertEqual(result['designated_locations'][6][3], 1.0)

    def test_set2_tolerance_0(self):
        input_file = open('./testes/teste2.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(0)

        input_file.close()

        self.assertEqual(result['objectives'], [ 60, 5 ])
        self.assertEqual(result['installed_bins'][0], 1.0)
        self.assertEqual(result['installed_bins'][2], 1.0)
        self.assertEqual(result['installed_bins'][3], 1.0)
        self.assertEqual(result['installed_bins'][4], 2.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)
        self.assertEqual(result['designated_locations'][3][3], 1.0)
        self.assertEqual(result['designated_locations'][4][1], 1.0)

    def test_set2_tolerance_10(self):
        input_file = open('./testes/teste2.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(10)

        input_file.close()

        self.assertEqual(result['objectives'], [ 70, 4 ])
        self.assertEqual(result['installed_bins'][0], 1.0)
        self.assertEqual(result['installed_bins'][2], 2.0)
        self.assertEqual(result['installed_bins'][3], 1.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][2][1], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)
        self.assertEqual(result['designated_locations'][3][3], 1.0)

    def test_set2_tolerance_60(self):
        input_file = open('./testes/teste2.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(60)

        input_file.close()

        self.assertEqual(result['objectives'], [ 120, 3 ])
        self.assertEqual(result['installed_bins'][0], 1.0)
        self.assertEqual(result['installed_bins'][2], 2.0)
        self.assertEqual(result['designated_locations'][0][0], 1.0)
        self.assertEqual(result['designated_locations'][0][3], 1.0)
        self.assertEqual(result['designated_locations'][2][1], 1.0)
        self.assertEqual(result['designated_locations'][2][2], 1.0)

    def test_set2_tolerance_210(self):
        input_file = open('./testes/teste2.json')

        bin_model = BinModel(json.loads(input_file.read()))
        result = bin_model.solve(210)

        input_file.close()

        self.assertEqual(result['objectives'], [ 270, 2 ])
        self.assertEqual(result['installed_bins'][4], 2.0)
        self.assertEqual(result['designated_locations'][4][0], 1.0)
        self.assertEqual(result['designated_locations'][4][1], 1.0)
        self.assertEqual(result['designated_locations'][4][2], 1.0)
        self.assertEqual(result['designated_locations'][4][3], 1.0)
