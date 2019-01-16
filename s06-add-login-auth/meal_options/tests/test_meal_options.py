import unittest

import meal_options


class Meal_optionsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = meal_options.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to meal-options', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
