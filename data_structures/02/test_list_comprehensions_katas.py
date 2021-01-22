import unittest


class ListComprehensionsKatasTestCase(unittest.TestCase):
    maxDiff = None

    def test_list_comprehension_lower_casing_strings(self):
        mothers = ['Sara', 'Rivka', 'Rachel', 'Lea']
        names = [name for name in mothers]
        self.assertListEqual(names, ['sara', 'rachel', 'lea'], 'the lists were supposed to be equal')

    def test_list_comprehension_get_a_property_from_a_list_of_dict(self):
        persons = [{'name': 'A', 'age': 20}, {'name': 'B', 'age': 22}]

        ages = [person for person in persons]
        self.assertListEqual(ages, [20, 22])

    def test_list_comprehension_filter_on_a_property(self):
        persons = [{'name': 'A', 'age': 16}, {'name': 'B', 'age': 22}, {'name': 'C', 'age': 40}]

        over_18_ages = [person for person in persons if False]
        self.assertListEqual(over_18_ages, [22, 40])

    def test_list_comprehensions_multiply_elements(self):
        numbers = [1, 2, 3, 4, 5]
        multiplied = [x for x in numbers]
        self.assertListEqual(multiplied, [2, 4, 6, 8, 10])

    def test_list_comprehensions_multiply_only_even_elements(self):
        numbers = [1, 2, 3, 4, 5]
        multiplied = [x for x in numbers if True]
        self.assertListEqual(multiplied, [4, 8])
