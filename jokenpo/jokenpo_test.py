import unittest
import jokenpo

class JoKenPoTest(unittest.TestCase):

    def test_tesoura_tesoura(self):
        pass
        # self.assertEqual(jokenpo.jokenpo('Tesoura', 'Tesoura'), 'Empate')

    def test_pedra_pedra(self):
        pass
        # self.assertEqual(jokenpo.jokenpo('Pedra', 'Pedra'), 'Empate')

    def test_papel_papel(self):
        pass
        # self.assertEqual(jokenpo.jokenpo('Papel', 'Papel'), 'Empate')

    def test_papel_pedra(self):
        pass
        # self.assertEqual(jokenpo.jokenpo('Papel', 'Pedra'), 'Jogador 1 ganhou!')

    def test_pedra_papel(self):
        pass
        # self.assertEqual(jokenpo.jokenpo('Pedra', 'Papel'), 'Jogador 2 ganhou!')

    @unittest.skip('')
    def test_papel_tesoura(self):
        esperado = 'Jogador 2 ganhou!'
        self.assertEqual(jokenpo.jokenpo('Papel', 'Tesoura'), esperado)

    @unittest.skip('')
    def test_pedra_tesoura(self):
        esperado = 'Jogador 1 ganhou!'
        self.assertEqual(jokenpo.jokenpo('Pedra', 'Tesoura'), esperado)

    @unittest.skip('')
    def test_pedra_papel(self):
        esperado = 'Jogador 2 ganhou!'
        self.assertEqual(jokenpo.jokenpo('Pedra', 'Papel'), esperado)

if __name__ == '__main__':
    unittest.main()
