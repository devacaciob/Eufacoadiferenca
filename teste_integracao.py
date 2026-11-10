
# ==================================================
# TESTE DE INTEGRACAO DA PLATAFORMA
# ==================================================

from armazenamento import carregar_dados, salvar_dados

from gerenciador import (
    cadastrar_aluno,
    cadastrar_curso,
    inscrever_aluno,
    consultar_aluno,
    consultar_curso
)


# Guarda os dados originais para restaurá-los depois.
dados_originais = carregar_dados()

try:

    # Cria uma base temporária para os testes.
    salvar_dados({
        "alunos": [],
        "cursos": [],
        "inscricoes": []
    })

    print("\n========== TESTE DE INTEGRACAO ==========")

    # --------------------------------------------------
    # TESTE 01 - CADASTRO DE ALUNO
    # --------------------------------------------------

    print("\n[TESTE 01] Cadastro válido de aluno")

    cadastrar_aluno(
        9001,
        "João Silva",
        "joao@email.com"
    )

    # --------------------------------------------------
    # TESTE 02 - ALUNO DUPLICADO
    # --------------------------------------------------

    print("\n[TESTE 02] Tentativa de aluno duplicado")

    cadastrar_aluno(
        9001,
        "João Silva",
        "joao@email.com"
    )

    # --------------------------------------------------
    # TESTE 03 - CADASTRO DE CURSO
    # --------------------------------------------------

    print("\n[TESTE 03] Cadastro válido de curso")

    cadastrar_curso(
        9001,
        "Python Orientado a Objetos",
        "Curso de programação orientada a objetos",
        40,
        20
    )

    # --------------------------------------------------
    # TESTE 04 - INSCRICAO VALIDA
    # --------------------------------------------------

    print("\n[TESTE 04] Inscrição válida")

    inscrever_aluno(9001, 9001, 9001)

    # --------------------------------------------------
    # TESTE 05 - INSCRICAO DUPLICADA
    # --------------------------------------------------

    print("\n[TESTE 05] Tentativa de inscrição duplicada")

    inscrever_aluno(9002, 9001, 9001)

    # --------------------------------------------------
    # TESTE 06 - CONSULTA DE ALUNO
    # --------------------------------------------------

    print("\n[TESTE 06] Consulta de aluno")

    consultar_aluno(9001)

    # --------------------------------------------------
    # TESTE 07 - CONSULTA DE CURSO
    # --------------------------------------------------

    print("\n[TESTE 07] Consulta de curso")

    consultar_curso(9001)

    # --------------------------------------------------
    # TESTE 08 - CONSULTA INVALIDA
    # --------------------------------------------------

    print("\n[TESTE 08] Consulta de aluno inexistente")

    consultar_aluno(9999)

    
    # --------------------------------------------------
    # TESTE 09 - ID DE INSCRICAO DUPLICADO
    # --------------------------------------------------

    print("\n[TESTE 09] Tentativa de utilizar ID de inscrição repetido")

    # Cadastra outro aluno e outro curso.
    cadastrar_aluno(
        9002,
        "Maria Oliveira",
        "maria@email.com"
    )

    cadastrar_curso(
        9002,
        "Java Básico",
        "Introdução à linguagem Java",
        30,
        5
    )

    # Tenta utilizar o ID 9001, que já pertence a outra inscrição.
    inscrever_aluno(9001, 9002, 9002)


    # --------------------------------------------------
    # TESTE 10 - CURSO SEM VAGAS
    # --------------------------------------------------

    print("\n[TESTE 10] Tentativa de inscrição em curso lotado")

    # Cadastra um curso sem vagas disponíveis.
    cadastrar_curso(
        9003,
        "Python Avançado",
        "Curso avançado de Python",
        60,
        0
    )

    # Tenta inscrever Maria em um curso sem vagas.
    inscrever_aluno(9003, 9002, 9003)


finally:

    # Restaura os dados originais do projeto.
    salvar_dados(dados_originais)

    print("\n========== TESTES FINALIZADOS ==========")
    print("Dados originais restaurados com sucesso!")
