# Write your test here
from challenge02 import *


def test_1():
    
  

    actual=first_repeated('ASAC is a department at LTUC. ASAC teaches programming in LTUC.')
    expect='ASAC'
    assert actual == expect


def test_2():
    
  

    actual=first_repeated('I am learning programming at ASAC.')
    expect='No Repetition'
    assert actual == expect


def test_3():
    
  

    actual=first_repeated('')
    expect='No Repetition'
    assert actual == expect