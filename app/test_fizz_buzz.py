from fizz_buzz import FizzBuzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_constructor(self):
        # num_fizzのテスト
        # 正常
        self.assertEqual(FizzBuzz(1, None, 1, None).get_num_fizz(), 1)
        # None指定
        with self.assertRaises(TypeError):
            FizzBuzz(None, None, 1, None)
        # 文字列指定
        with self.assertRaises(TypeError):
            FizzBuzz('tmp', None, 1, None)
        # 実数指定
        with self.assertRaises(TypeError):
            FizzBuzz(1.1, None, 1, None)
        # 0以下
        with self.assertRaises(TypeError):
            FizzBuzz(0, None, 1, None)

        # word_fizzのテスト
        # 正常
        self.assertEqual(FizzBuzz(1, 'tmp', 1, None).word_fizz, 'tmp')
        self.assertEqual(FizzBuzz(1, None, 1, None).word_fizz, None)

        # num_buzzのテスト
        # 正常
        self.assertEqual(FizzBuzz(1, None, 1, None).get_num_buzz(), 1)
        # None指定
        with self.assertRaises(TypeError):
            FizzBuzz(1, None, None, None)
        # 文字列指定
        with self.assertRaises(TypeError):
            FizzBuzz(1, None, 'tmp', None)
        # 実数指定
        with self.assertRaises(TypeError):
            FizzBuzz(1, None, 1.1, None)
        # 0以下
        with self.assertRaises(TypeError):
            FizzBuzz(1, None, 0, None)

        # word_buzzのテスト
        # 正常
        self.assertEqual(FizzBuzz(1, None, 1, 'tmp').word_buzz, 'tmp')
        self.assertEqual(FizzBuzz(1, None, 1, None).word_buzz, None)

        # indexのテスト
        self.assertEqual(FizzBuzz(1, None, 1, None).index, 1)

    def test_call_next(self):
        # 1~30で通常のFizzBuzz
        fizz_buzz = FizzBuzz(3, 'Fizz', 5, 'Buzz')
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
        fizz_buzz = FizzBuzz(2, None, 3, 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 2)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 4)
        self.assertEqual(fizz_buzz.call_next(), 5)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')

        # 2~6でword_buzz未指定
        fizz_buzz = FizzBuzz(2, 'hoge', 3, None)
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 3)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 5)
        self.assertEqual(fizz_buzz.call_next(), 'hoge')

        # 2~6でword_fizz、word_buzz未指定
        fizz_buzz = FizzBuzz(2, None, 3, None)
        self.assertEqual(fizz_buzz.call_next(), 1)
        self.assertEqual(fizz_buzz.call_next(), 2)
        self.assertEqual(fizz_buzz.call_next(), 3)
        self.assertEqual(fizz_buzz.call_next(), 4)
        self.assertEqual(fizz_buzz.call_next(), 5)
        self.assertEqual(fizz_buzz.call_next(), 6)

        # 1~4でnumに1指定
        fizz_buzz = FizzBuzz(1, 'hoge', 4, 'fuga')
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 'hoge')
        self.assertEqual(fizz_buzz.call_next(), 'hogefuga')

if __name__ == '__main__':
    unittest.main()
