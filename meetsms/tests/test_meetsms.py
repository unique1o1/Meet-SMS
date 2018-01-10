import unittest

from meetsms import meetsms


class Tests(unittest.TestCase):

    def test_unit_test(self):
        got = meetsms.unit_test("hello")
        expected = "hello"
        self.assertEqual(got, expected)


if __name__ == '__main__':
    unittest.main()
