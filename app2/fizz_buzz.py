class FizzBuzz:
    def __init__(self):
        self.index = 1
    
    def call_next(self):
        config = Config.get_config()
        num_fizz = config['num_fizz']
        word_fizz = config['word_fizz']
        num_buzz = config['num_buzz']
        word_buzz = config['word_buzz']
        ret = self.index
        if self.__should_call_fizz(num_fizz, word_fizz) and self.__should_call_buzz(num_buzz, word_buzz):
            ret = word_fizz + word_buzz
        elif self.__should_call_fizz(num_fizz, word_fizz):
            ret = word_fizz
        elif self.__should_call_buzz(num_buzz, word_buzz):
            ret = word_buzz
        self.index += 1
        return ret
    
    def __should_call_fizz(self, num_fizz, word_fizz):
        return self.index % num_fizz == 0 and word_fizz
    
    def __should_call_buzz(self, num_buzz, word_buzz):
        return self.index % num_buzz == 0 and word_buzz

class Config:
    def get_config():
        return {
            'num_fizz': 3,
            'word_fizz': 'Fizz',
            'num_buzz': 5,
            'word_buzz': 'Buzz',
        }

if __name__ == '__main__':
    fizz_buzz = FizzBuzz(3, 'Fizz', 5, 'Buzz')
    for _ in range(30):
        print(fizz_buzz.call_next())