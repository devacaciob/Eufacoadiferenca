
# ==================================================
# PLATAFORMA DE CURSOS ONLINE
# Programa principal do sistema
# ==================================================

# Importa todas as funções do gerenciador.
from gerenciador import (
    cadastrar_aluno,
    cadastrar_curso,
    inscrever_aluno,
    consultar_aluno,
    consultar_curso
)


# ==================================================
# 1. CADASTRO DE ALUNOS
# ==================================================

print("\n========== CADASTRO DE ALUNOS ==========")

# Teste válido: cadastra um aluno.
cadastrar_aluno(1001, "Carlos", "carlos@email.com")

# Teste inválido: tenta cadastrar o mesmo aluno novamente.
cadastrar_aluno(1001, "Carlos", "carlos@email.com")


# ==================================================
# 2. CADASTRO DE CURSOS
# ==================================================

print("\n========== CADASTRO DE CURSOS ==========")

# Teste válido: cadastra um curso.
cadastrar_curso(
    101,
    "Python Básico",
    "Introdução à programação com Python",
    40,
    30
)


# ==================================================
# 3. INSCRIÇÃO DE ALUNOS
# ==================================================

print("\n========== INSCRIÇÃO EM CURSOS ==========")

# Teste válido: inscrição de Carlos.
inscrever_aluno(1, 1001, 101)

# Teste inválido: ID de inscrição já utilizado.
inscrever_aluno(1, 1001, 101)

# Teste inválido: aluno já inscrito no curso.
inscrever_aluno(2, 1001, 101)


# ==================================================
# 4. CONSULTA DE INFORMAÇÕES
# ==================================================

print("\n========== CONSULTAS ==========")

# Consulta válida: exibe os dados do aluno.
consultar_aluno(1001)

# Consulta válida: exibe os dados do curso.
consultar_curso(101)

# Consulta inválida: tenta consultar um aluno inexistente.
consultar_aluno(9999)


# ==================================================
# FIM DA DEMONSTRAÇÃO
# ==================================================

print("\n========== FIM DA DEMONSTRAÇÃO ==========")
