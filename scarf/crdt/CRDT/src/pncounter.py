import sys
sys.path.append('../../../')

from crdt.CRDT.src.gcounter import GCounter


class PNCounter:
    def __init__(self):
        self.P = GCounter()
        self.N = GCounter()

    def add_new_node(self, key):
        self.P.add_new_node(key)
        self.N.add_new_node(key)

    def inc(self, key):
        self.P.inc(key)

    def dec(self, key):
        self.N.inc(key)

    def query(self):
        return self.P.query() - self.N.query()

    def compare(self, gc2):
        return self.P.compare(gc2.P) and self.N.compare(gc2.N)

    def merge(self, gc2):
        self.P.merge(gc2.P)
        self.N.merge(gc2.N)
        # self.display()

    def display(self, name):
        print("{}.P: ".format(name), end="")
        self.P.display()
        print("{}.N: ".format(name), end="")
        self.N.display()

    def toDict(self):
        return self.__dict__
    
    def loadFromDict(dict_input):
        pncounter = PNCounter()
        pncounter.__dict__ = dict_input
        return pncounter