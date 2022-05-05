from operaciones import *
import unittest 

class TestCalculoMedia(unittest.TestCase):
    def test_1(self):
        resultado = calculo_media([5,5,5,5])
        self.assertEqual(resultado,5)

    def test_2(self):
        resultado = calculo_media([10,10,10])
        self.assertEqual(resultado,10)

if __name__ == '__main__':
    unittest.main()          



# .assertEqual(a, b): Verifica la igualdad de ambos valores.
# .assertTrue(x): Verifica que el valor es True.
# .assertFalse(x): Verifica que el valor es False.
# .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
# .assert.IsNone(x): Verifica que el valor es None.
# .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
# .assertIsInstance(a, b): Verifica que a es una instancia de b.
# .assertRaises(x): Verifica que se lanza una excepción.