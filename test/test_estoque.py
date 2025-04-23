import unittest
from estoque import Estoque

class TestEstoque(unittest.TestCase):
    
    def setUp(self):
        self.estoque = Estoque()

    # Teste correto: Adiciona produto e verifica se a quantidade foi aumentada corretamente
    def test_adicionar_produto(self):
        quantidade = self.estoque.adicionar_produto("Produto A", 10)
        self.assertEqual(quantidade, 10)  # Esperamos que a quantidade seja 10

    # Teste incorreto: Verifica se o produto foi adicionado, mas com um valor errado para testar a falha
    def test_adicionar_produto_falha(self):
        quantidade = self.estoque.adicionar_produto("Produto B", 20)
        self.assertEqual(quantidade, 25)  # Aqui estamos intencionalmente errando a quantidade (deveria ser 20)

    # Teste: Verifica se adicionar mais do mesmo produto aumenta a quantidade corretamente
    def test_adicionar_mais_produto(self):
        self.estoque.adicionar_produto("Produto A", 10)
        quantidade = self.estoque.adicionar_produto("Produto A", 5)
        self.assertEqual(quantidade, 15)  # Esperamos que a quantidade seja 15 após adicionar 5 unidades

    # Teste correto: Remove produto do estoque
    def test_remover_produto(self):
        self.estoque.adicionar_produto("Produto A", 10)
        quantidade = self.estoque.remover_produto("Produto A", 5)
        self.assertEqual(quantidade, 5)  # Esperamos que a quantidade seja 5 após remover 5 unidades

    # Teste incorreto: Tentar remover mais produto do que existe no estoque
    def test_remover_produto_falha(self):
        self.estoque.adicionar_produto("Produto B", 10)
        with self.assertRaises(ValueError):  # Esperamos um erro devido a quantidade insuficiente
            self.estoque.remover_produto("Produto B", 15)
    
    # Teste incorreto: Remover um produto que não existe
    def test_remover_produto_inexistente(self):
        with self.assertRaises(ValueError):  # Esperamos um erro pois o produto não existe
            self.estoque.remover_produto("Produto C", 5)
