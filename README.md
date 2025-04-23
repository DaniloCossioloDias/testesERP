# testesERP

python -m unittest discover -s test


..F...
======================================================================
FAIL: test_adicionar_produto_falha (test_estoque.TestEstoque.test_adicionar_produto_falha)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/caminho/para/seu_projeto/test/test_estoque.py", line 17, in test_adicionar_produto_falha
    self.assertEqual(quantidade, 25)  # erro intencional a quantidade (deveria ser 20)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
AssertionError: 20 != 25

----------------------------------------------------------------------
Ran 6 tests in 0.001s


# Interpretação dos Resultados

- **Cada ponto (`.`)**: Representa um teste que passou.
- **`F`**: Indica um teste que falhou.

## Resumo:
- **Total de testes**: 6
- **Passaram**: 5
- **Falharam**: 1 (intencional)

## Detalhes do Teste com Falha:
- **Teste**: `test_adicionar_produto_falha`
- **Motivo**: O teste compara `20` (valor correto) com `25` (valor errado de propósito), causando a falha esperada.