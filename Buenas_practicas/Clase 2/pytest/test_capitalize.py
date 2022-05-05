from capitalize import *
import pytest


def test_capital_case():
    assert capital_case('alex') == 'Alex'

def test_raise_exception_capitalize():
    with pytest.raises(TypeError):    
        capital_case(9)