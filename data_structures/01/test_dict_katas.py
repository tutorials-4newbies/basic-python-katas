import unittest


class DictKatasTestCase(unittest.TestCase):
    def test_dict_get(self):
        first_person = {
            "age": 1000,
            "name": "Hava"
        }
        age = first_person['']
        self.assertEqual(age, 1000)

    def test_dict_default_get(self):
        second_person = {
            "age": 999,
            "name": "Adam"
        }

        birthday = second_person.do_something('', 42)
        self.assertEqual(birthday, 42)

    def test_nested_dicts(self):
        family_tree = {
            "my_children": {
                "Robert": 19,
                "Fiona": 23
            },
            "my_parents": [
                "Dad Name", "Mom Name 2"
            ]
        }

        robert_age = family_tree['']
        self.assertEqual(robert_age, 19)

        mom_name = family_tree['']
        self.assertEqual(mom_name, "Mom Name 2")

    def test_dict_insert(self):
        songs = {
            "blur": "song2"
        }
        songs['']
        self.assertDictEqual(songs, {"bluer": "song2", "The Clash": "London Calling"})

    def test_dict_merge(self):
        spice_records = {
            "Spice": 1996,
            "SpiceWorld": 1997

        }
        comeback_records = {"Forever": 2000}

        spice_records.do_something(comeback_records)
        self.assertDictEqual(spice_records, {
             "Spice": 1996,
             "SpiceWorld": 1997,
             "Forever": 2000
        })

    def test_nested_dict_insert(self):
        family_tree = {
            "my_children": {
                "Robert": 19,
                "Fiona": 23
            },
            "my_parents": [
                "Dad Name", "Mom Name 2"
            ]
        }

        family_tree['']

        self.assertDictEqual(family_tree['my_children'], {"Robert": 19, "Fiona": 23, "Danna": 30})

    def test_dict_iteration_keys(self):
        best_places_rating = {
            "Jerusalem": 5,
            "NewYork": 10
        }
        places = []

        # For loop here
        self.assertListEqual(places, ['Jerusalem', 'NewYork'])

    def test_dict_iteration_values(self):
        sore_losers = {
            "Trump": 2020,
            "Hoover": 1932
        }

        losing_dates = []

        # for loop here

        self.assertListEqual(losing_dates, [2020, 1932])


if __name__ == '__main__':
    unittest.main()
