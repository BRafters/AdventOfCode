import unittest
from handle_content import *
from mapping import Mapper

class TestBackpackParsing(unittest.TestCase):
    def test_file_operation(self):
        data = unload_data_from_file("resources/test_data.txt")
        self.assertNotEqual(data, "", "Reading text from file")
        print(data)

    def test_grab_set(self):
        list_of_expected_results = ['p', 'L', 'P', 'v', 't', 's']
        datas = list_backpacks(unload_data_from_file("resources/test_data.txt"))
        for i in range(len(datas)):
            self.assertEqual(list(search_for_duplicates(datas[i]))[0], list_of_expected_results[i])

    def test_mapping_value(self):
        list_of_expected_results = ['p', 'L', 'P', 'v', 't', 's']
        map = Mapper()

        for result in list_of_expected_results:
            map.inc_total_priorities(result)

        self.assertEqual(157, map.get_priority_total())

    def test_empty_mapping_value(self):
        list_of_expected_results = ['p', 'L', 'P', ' ', 't', 's']
        map = Mapper()

        for result in list_of_expected_results:
            map.inc_total_priorities(result)

        self.assertEqual(135, map.get_priority_total())

    def test_groups_of_elves(self):
        print("Testing even groups")
        datas = make_groups_of_three(unload_data_from_file("resources/test_data.txt"))
        self.assertEqual(len(datas), 2)

        for data in datas:
            self.assertEqual(len(data), 3)

    def test_for_common_items(self):
        print("Test for common items")
        backpacks = list_backpacks(unload_data_from_file("resources/test_data.txt"))
        datas = make_groups_of_three(backpacks)

        # Here we will have two groups. We will test these groups
        common_items = find_common_items(datas)

        print(common_items)
        self.assertEqual(common_items[0][0], 'r')
        self.assertEqual(common_items[1][0], 'Z')

    # Negative Tests
    def test_uneven_groups_of_elves(self):
        print("Testing uneven groups")
        datas = make_groups_of_three(unload_data_from_file("resources/test_data.txt"))
        print(datas)
        
if __name__ == '__main__':
    unittest.main()
