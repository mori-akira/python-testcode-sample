from fizz_buzz import FizzBuzz
from fizz_buzz import Config
import unittest
import unittest.mock

class TestFizzBuzz(unittest.TestCase):

    def test_constructor(self):
        # indexのテスト
        self.assertEqual(FizzBuzz().index, 1)

    @unittest.mock.patch('fizz_buzz.Config.get_config')
    def test_call_next(self, mock_get_config):
        # 1~30で通常のFizzBuzz
        mock_get_config.return_value = {
            'num_fizz': 3,
            'word_fizz': 'Fizz',
            'num_buzz': 5,
            'word_buzz': 'Buzz',
        }
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 2)
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 4)
        self.assertEqual(fizz_buzz.call_next(), 'Buzz')
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 7)
        self.assertEqual(fizz_buzz.call_next(), 8)
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 'Buzz')
        self.assertEqual(fizz_buzz.call_next(), 11)
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 13)
        self.assertEqual(fizz_buzz.call_next(), 14)
        self.assertEqual(fizz_buzz.call_next(), 'FizzBuzz')
        self.assertEqual(fizz_buzz.call_next(), 16)
        self.assertEqual(fizz_buzz.call_next(), 17)
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 19)
        self.assertEqual(fizz_buzz.call_next(), 'Buzz')
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 22)
        self.assertEqual(fizz_buzz.call_next(), 23)
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 'Buzz')
        self.assertEqual(fizz_buzz.call_next(), 26)
        self.assertEqual(fizz_buzz.call_next(), 'Fizz')
        self.assertEqual(fizz_buzz.call_next(), 28)
        self.assertEqual(fizz_buzz.call_next(), 29)
        self.assertEqual(fizz_buzz.call_next(), 'FizzBuzz')

        # 2~6でword_fizz未指定
        mock_get_config.return_value = {
            'num_fizz': 2,
            'word_fizz': None,
            'num_buzz': 3,
            'word_buzz': 'hoge',
        }
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 2)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 4)
        self.assertEqual(fizz_buzz.call_next(), 5)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')

        # 2~6でword_buzz未指定
        mock_get_config.return_value = {
            'num_fizz': 2,
            'word_fizz': 'hoge',
            'num_buzz': 3,
            'word_buzz': None,
        }
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 3)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 5)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')

        # 2~6でword_fizz、word_buzz未指定
        mock_get_config.return_value = {
            'num_fizz': 2,
            'word_fizz': None,
            'num_buzz': 3,
            'word_buzz': None,
        }
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 2)
        self.assertEqual(fizz_buzz.call_next(), 3)
        self.assertEqual(fizz_buzz.call_next(), 4)
        self.assertEqual(fizz_buzz.call_next(), 5)
        self.assertEqual(fizz_buzz.call_next(), 6)

        # 1~4でnumに1指定
        mock_get_config.return_value = {
            'num_fizz': 1,
            'word_fizz': 'hoge',
            'num_buzz': 4,
            'word_buzz': 'fuga',
        }
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 'hogefuga')

if __name__ == '__main__':
    unittest.main()
