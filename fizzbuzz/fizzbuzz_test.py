import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz_1(self):
        pass
        # self.assertEqual(fizzbuzz.fizzbuzz(1), [1])

    def test_fizzbuzz_0(self):
        pass
        # self.assertEqual(fizzbuzz.fizzbuzz(0), [])

    def test_fizzbuzz_101(self):
        pass
        # self.assertEqual(fizzbuzz.fizzbuzz(101), [])

    @unittest.skip('')
    def test_fizzbuzz_2(self):
        expected = [1, 2]
        self.assertEqual(fizzbuzz.fizzbuzz(2), expected)

    @unittest.skip('')
    def test_fizzbuzz_3(self):
        expected = [1, 2, 'Fizz']
        self.assertEqual(fizzbuzz.fizzbuzz(3), expected)

    @unittest.skip('')
    def test_fizzbuzz_5(self):
        expected = [1, 2, 'Fizz', 4, 'Buzz']
        self.assertEqual(fizzbuzz.fizzbuzz(5), expected)

    @unittest.skip('')
    def test_fizzbuzz_15(self):
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                    'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        self.assertEqual(fizzbuzz.fizzbuzz(15), expected)

if __name__ == '__main__':
    unittest.main()
