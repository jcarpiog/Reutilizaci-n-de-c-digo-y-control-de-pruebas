import mymath
import unittest
class TestAdd(unittest.TestCase):
    """
     Pruebe la función agregar de la biblioteca mymath
    """
    def test_add_integers(self):
        """
        Pruebe que la suma de dos enteros devuelva el total correcto
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)
    def test_add_floats(self):
        """
        Pruebe que la suma de dos flotadores devuelva el resultado correcto
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)
    def test_add_strings(self):
        """
        Probar la suma de dos cadenas devuelve las dos cadenas como una
        cadena concatenada
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')
if __name__ == '__main__':
    unittest.main()