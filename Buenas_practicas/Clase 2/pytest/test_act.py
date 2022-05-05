from act import *
import pytest

def test_calculadora():
    
    numero1 = 5
    numero2 = 5
    basicas = False
    multi = 25
    division = 1.0


    assert numero1 * numero2 == multi
    assert numero1 / numero2 == division

# ********************************************************************

def test_calculadora2():
    
    numero1 = 5
    numero2 = 5
    basicas = True
    suma = 10
    resta = 0


    assert numero1 + numero2 == suma
    assert numero1 - numero2 == resta    