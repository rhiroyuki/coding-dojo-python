import unittest
import jokenpo

class JoKenPoTest(unittest.TestCase):

    def test_tesoura_tesoura(self):
        self.assertEqual(jokenpo.jokenpo('Tesoura', 'Tesoura'), 'Empate')

    def test_pedra_pedra(self):
        self.assertEqual(jokenpo.jokenpo('Pedra', 'Pedra'), 'Empate')

    def test_papel_papel(self):
        self.assertEqual(jokenpo.jokenpo('Papel', 'Papel'), 'Empate')

    def test_papel_pedra(self):
        self.assertEqual(jokenpo.jokenpo('Papel', 'Pedra'), 'Jogador 1 ganhou!')

    def test_pedra_papel(self):
        self.assertEqual(jokenpo.jokenpo('Pedra', 'Papel'), 'Jogador 2 ganhou!')

    def test_papel_tesoura(self):
        esperado = 'Jogador 2 ganhou!'
        self.assertEqual(jokenpo.jokenpo('Papel', 'Tesoura'), esperado)

    def test_pedra_tesoura(self):
        esperado = 'Jogador 1 ganhou!'
        self.assertEqual(jokenpo.jokenpo('Pedra', 'Tesoura'), esperado)

    def test_pedra_papel(self):
        esperado = 'Jogador 2 ganhou!'
        self.assertEqual(jokenpo.jokenpo('Pedra', 'Papel'), esperado)
