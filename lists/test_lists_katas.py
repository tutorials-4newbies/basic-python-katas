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

    def test_removing_a_specific_value_from_list(self):
        mothers = ['Sara', 'Rivka', 'Rachel', 'Lea']
        mothers.do_something('Rivka')
        self.assertListEqual(mothers, ['Sara', 'Rachel', 'Lea'], 'the lists were supposed to be equal')

    def test_simple_list_slicing(self):
        pass

    def test_list_slicing_from_the_middle(self):
        pass

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
