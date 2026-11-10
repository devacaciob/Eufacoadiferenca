from armazenamento import carregar_dados, salvar_dados

dados = carregar_dados()

print("Dados carregados:")
print(dados)

salvar_dados(dados)

print("Dados salvos com sucesso!")