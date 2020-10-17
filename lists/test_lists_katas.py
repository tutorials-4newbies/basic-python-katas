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

    def test_list_comprehension_get_a_property_from_a_list_of_dict(self):
        persons = [{'name': 'A', 'age': 20}, {'name': 'B', 'age': 22}]

        ages = [person for person in persons]
        self.assertListEqual(ages, [20, 22])

    def test_list_comprehension_filter_on_a_property(self):
        persons = [{'name': 'A', 'age': 16}, {'name': 'B', 'age': 22}, {'name': 'C', 'age': 40}]

        over_18_ages = [person for person in persons]
        self.assertListEqual(over_18_ages, [22, 40])

    def test_list_comprehensions_multiply_a_property(self):
        numbers = [1, 2, 3, 4, 5]
        multiplied = [x for x in numbers]
        self.assertListEqual(multiplied, [2, 4, 6, 8, 10])
