from collections.abc import Iterable


class Reporter(Iterable):
    def __init__(self):
        self.__key = None
        self.__key_name = None
        self.__rel = None
        self.__rel_name = None

    def set_key(self, key, name):
        self.__key = iter(key)
        self.__key_name = name

    def add_relation(self, func, name):
        self.__rel = func
        self.__rel_name = name

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__key:
            raise StopIteration
        result = dict()
        key = next(self.__key)
        result[self.__key_name] = key
        if self.__rel:
            result[self.__rel_name] = self.__rel(key)
        return result
