import unittest
from notas.conceito import nota_para_conceito


class TestConceito(unittest.TestCase):
    def test_dez_e_a(self):
        self.assertEqual(nota_para_conceito(10.0), "A")

    def test_nove_e_a(self):
        self.assertEqual(nota_para_conceito(9.0), "A")

    def test_8_9_e_b(self):
        self.assertEqual(nota_para_conceito(8.9), "B")

    def test_sete_e_c(self):
        self.assertEqual(nota_para_conceito(7.0), "C")

    def test_seis_e_d(self):
        self.assertEqual(nota_para_conceito(6.0), "D")

    def test_5_9_e_e(self):
        self.assertEqual(nota_para_conceito(5.9), "E")

    def test_3_9_e_f(self):
        self.assertEqual(nota_para_conceito(3.9), "F")

    def test_nota_acima_de_dez_da_erro(self):
        with self.assertRaises(ValueError):
            nota_para_conceito(10.5)


if __name__ == "__main__":
    unittest.main()
