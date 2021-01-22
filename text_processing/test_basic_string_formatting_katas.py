import unittest


class BasicStringFormattingTestCase(unittest.TestCase):
    def test_string_formatting_with_f_string(self):
        two = 'two'
        counting = f'one three'
        self.assertEqual(counting, 'one two three')

    def test_string_formatting_with_expression(self):
        def double(num):
            return num * 2

        expressing_numbers = f'double three equals: {3}'
        # use the double function
        self.assertEqual(expressing_numbers, 'double three equals: 6')

    def test_string_formatting_with_format(self):
        words = 'Once I was _ I was _'.format('afraid', '')

        self.assertEqual(words, 'Once I was afraid I was petrified')

    def test_string_formatting_with_format_dict(self):
        words = "Oooohh! Yes {}, I can boogie But I need a certain {}".format(something='song', who='sir')
        self.assertEqual(words, 'Oooohh! Yes sir, I can boogie But I need a certain song')


if __name__ == '__main__':
    unittest.main()
