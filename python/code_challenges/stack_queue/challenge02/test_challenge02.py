# Write your test here
from challenge02 import validate_Parentheses

def test_validate_Parentheses_1():
    actual=validate_Parentheses("()[]{}")
    expect=True
    assert actual==expect

def test_validate_Parentheses_2():
    actual=validate_Parentheses("[({}]")
    expect=False
    assert actual==expect

def test_validate_Parentheses_3():
    actual=validate_Parentheses("[(hello)()]")
    expect=True
    assert actual==expect