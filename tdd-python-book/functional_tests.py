from unittest import TestCase, main
from selenium import webdriver


class TestPaginaInicial(TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_usuario_visualiza_o_titulo_da_pagina(self):
        # Ao acessar a aplicação o usuário vê o título "Lista de Tarefas"
        self.browser.get('http://localhost:8000')
        # assert 'Lista de Tarefas' in self.browser.title, '"Lista de Tarefas" não encontrada no título'
        # Outra opção:
        self.assertIn('Lista de Tarefas', self.browser.title)


if __name__ == '__main__':
    main()
