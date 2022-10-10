class FizzBuzz:

    def __init__(self, num_fizz, word_fizz, num_buzz, word_buzz):
        if type(num_fizz) == int and num_fizz > 0:
            self.__num_fizz = num_fizz
        else:
            raise TypeError('num_fizz must be int and greater than zero')
        self.word_fizz = word_fizz
        if type(num_buzz) == int and num_buzz > 0:
            self.__num_buzz = num_buzz
        else:
            raise TypeError('num_buzz must be int and greater than zero')
        self.word_buzz = word_buzz
        self.index = 1
    
    def call_next(self):
        ret = self.index
        if self.__should_call_fizz() and self.__should_call_buzz():
            ret = self.word_fizz + self.word_buzz
        elif self.__should_call_fizz():
            ret = self.word_fizz
        elif self.__should_call_buzz():
            ret = self.word_buzz
        self.index += 1
        return ret
    
    def __should_call_fizz(self):
        return self.index % self.__num_fizz == 0 and self.word_fizz
    
    def __should_call_buzz(self):
        return self.index % self.__num_buzz == 0 and self.word_buzz

    def set_num_fizz(self, num_fizz):
        if type(num_fizz) == int and num_fizz > 0:
            self.__num_fizz = num_fizz
        else:
            raise TypeError('num_fizz must be int and greater than zero')
    
    def set_num_buzz(self, num_buzz):
        if type(num_buzz) == int and num_buzz > 0:
            self.__num_buzz = num_buzz
        else:
            raise TypeError('num_buzz must be int and greater than zero')
    
    def get_num_fizz(self):
        return self.__num_fizz
    
    def get_num_buzz(self):
        return self.__num_buzz

if __name__ == '__main__':
    fizz_buzz = FizzBuzz(3, 'Fizz', 5, 'Buzz')
    for _ in range(30):
        print(fizz_buzz.call_next())