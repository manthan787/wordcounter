from collections import defaultdict
from abc import ABCMeta, abstractmethod


class Tokenizer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def tokenize(self, text):
        pass


class SimpleTokenizer(object):

    def tokenize(self, text):
        return text.split()


class Wordcounter(object):

    def __init__(self, text, tokenizer=SimpleTokenizer()):
        self.text = text
        self.tokenizer = tokenizer

    def count(self):
        return len(self.tokenizer.tokenize(self.text))


if __name__ == '__main__':
    # Tests
    assert Wordcounter("").count() == 0
    assert Wordcounter("hello world").count() == 2
    assert Wordcounter("  ").count() == 0
    assert Wordcounter("  \n ").count() == 0
