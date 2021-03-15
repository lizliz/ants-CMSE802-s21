import pytest 
from ants import anthill

def test_init_ant():
    ant = anthill.Ant()
    assert ant.hasfood == False
