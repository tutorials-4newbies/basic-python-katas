import unittest


class ListKatasTestCase(unittest.TestCase):
    maxDiff = None

    def test_adding_to_list(self):
        fathers = ['Avraham', 'Yizhak']
        missing_father = 'Yaacov'
        fathers.do_something(missing_father)
        self.assertListEqual(fathers, ['Avraham', 'Yizhak', 'Yaacov'], 'the lists were supposed to be equal')

    def test_removing_from_list(self):
        mothers = ['Sara', 'Rivka', 'Rachel', 'Lea']
        mothers.do_something()
        self.assertListEqual(mothers, ['Sara', 'Rivka', 'Rachel'], 'the lists were supposed to be equal')

    def test_list_concatenating(self):
        trees = ['oak', 'lemon']
        more_trees = ['olive', 'cedar']

        trees.do_something(more_trees)

        self.assertListEqual(trees, ['oak', 'lemon', 'olive', 'cedar'])

    def test_removing_a_specific_value_from_list(self):
        mothers = ['Sara', 'Rivka', 'Rachel', 'Lea']
        mothers.do_something('Rivka')
        self.assertListEqual(mothers, ['Sara', 'Rachel', 'Lea'], 'the lists were supposed to be equal')

    def test_simple_list_slicing(self):
        europe = ['France', 'Germany', 'Italy', 'Spain', 'Britain', 'Ireland', 'Portugal']

        first_two_countries = europe[0:0]
        self.assertListEqual(first_two_countries, ['France', 'Germany'])

    def test_list_slicing_from_the_middle(self):
        europe = ['France', 'Germany', 'Italy', 'Spain', 'Britain', 'Ireland', 'Portugal']

        islands = europe[0:0]
        self.assertListEqual(islands, ['Britain', 'Ireland'])

    def test_list_steps(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        thirds = nums[0:0:0]
        self.assertListEqual(thirds, [3, 6, 9])
