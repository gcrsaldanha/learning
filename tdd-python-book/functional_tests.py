import unittest
from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.Firefox()

# Ao acessar a aplicação o usuário vê o título "Lista de Tarefas"
browser.get('http://localhost:8000')
assert "Lista de Tarefas" in browser.title
