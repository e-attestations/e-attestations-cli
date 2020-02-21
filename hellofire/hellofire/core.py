#!/usr/bin/env python
# Copyright Vincent DAGOURY - 2020. BSD 3-Clause license, see LICENSE file.

"""
The core module of hellofire
"""

import fire

class Greeter(object):
    """
A simple cli using Fire !
    
Commands:
    hello : greet in English
    salut : greet in French

Options:
    --verbose : the verbose mode (duh)
    """

    def __init__(self, verbose=False):
        self._verbose = verbose

    def hello(self, name="World"):
        """A simple Hello world example"""
        if (self._verbose == 1):
            print("Saying hello %s" % name)
        return "Hello %s!" % name

    def salut(self, name="World"):
        """A simple Salut world example"""
        if (self._verbose == 1):
            print("Saying salut %s" % name)
        return "Salut %s!" % name

def hellofire():
    fire.Fire(Greeter)

if __name__ == '__main__':
    hellofire()
