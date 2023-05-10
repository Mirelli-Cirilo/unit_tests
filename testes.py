from app import converte_f_para_c, converte_c_para_f
from unittest import TestCase

class TestConverteFparaC(TestCase):
    def test_converte_retorna_0_quando_receber_32(self):
        assert converte_f_para_c(32) == 0
    def test_converte_retorna_menos40_quando_receber_menos40(self):
        assert converte_f_para_c(-40) == -40

    def test_converte_retorna__menos17_77_recebe_0(self):
        self.assertAlmostEqual(converte_f_para_c(0), -17.77, places=1)    

class TestConverteCparaF(TestCase):
    def test_converte_retorna__40_quando_receber__40(self):
        self.assertEqual(converte_c_para_f(-40), -40)