import unittest

from notas.situacao import situacao


class TestSituacao(unittest.TestCase):

    def test_media_alta_e_frequencia_boa(self):
        self.assertEqual(situacao(8.0, 90), "aprovado")

    def test_media_6_e_frequencia_75_aprova(self):
        self.assertEqual(situacao(6.0, 75), "aprovado")

    def test_media_5_9_vai_para_exame(self):
        self.assertEqual(situacao(5.9, 100), "exame")

    def test_media_4_vai_para_exame(self):
        self.assertEqual(situacao(4.0, 80), "exame")

    def test_media_3_9_reprova(self):
        self.assertEqual(situacao(3.9, 80), "reprovado")

    def test_frequencia_74_reprova_mesmo_com_media_alta(self):
        self.assertEqual(situacao(9.0, 74), "reprovado")


if __name__ == "__main__":
    unittest.main()
