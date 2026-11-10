
# ==================================================
# IMPORTAÇÃO DAS CLASSES E FUNÇÕES
# ==================================================

# Importa as classes que representam as entidades.
from Entidades.aluno import Aluno
from Entidades.curso import Curso
from Entidades.inscricao import Inscricao

# Importa as funções de armazenamento JSON.
from armazenamento import carregar_dados, salvar_dados


# ==================================================
# 1. CADASTRO DE ALUNOS
# ==================================================

def cadastrar_aluno(id_aluno, nome, email):

    # Carrega os dados existentes no JSON.
    dados = carregar_dados()

    # Verifica se o aluno já está cadastrado.
    for aluno in dados["alunos"]:
        if aluno["id_aluno"] == id_aluno:
            print("Aluno já cadastrado.")
            return False

    # Cria um objeto da classe Aluno.
    novo_aluno = Aluno(id_aluno, nome, email)

    # Adiciona os dados do aluno à lista.
    dados["alunos"].append(novo_aluno.__dict__)

    # Salva os dados atualizados.
    salvar_dados(dados)

    print("Aluno cadastrado com sucesso!")
    return True


# ==================================================
# 2. CADASTRO DE CURSOS
# ==================================================

def cadastrar_curso(id_curso, nome, descricao, carga_horaria, vagas):

    # Carrega os dados existentes no JSON.
    dados = carregar_dados()

    # Verifica se o curso já está cadastrado.
    for curso in dados["cursos"]:
        if curso["id_curso"] == id_curso:
            print("Curso já cadastrado.")
            return False

    # Cria um objeto da classe Curso.
    novo_curso = Curso(id_curso, nome, descricao, carga_horaria, vagas)

    # Adiciona os dados do curso à lista.
    dados["cursos"].append(novo_curso.__dict__)

    # Salva os dados atualizados.
    salvar_dados(dados)

    print("Curso cadastrado com sucesso!")
    return True


# ==================================================
# 3. INSCRIÇÃO DE ALUNOS EM CURSOS
# ==================================================

def inscrever_aluno(id_inscricao, id_aluno, id_curso):

    # Carrega os dados existentes no JSON.
    dados = carregar_dados()

    # Verifica se o aluno existe.
    aluno_encontrado = False

    for aluno in dados["alunos"]:
        if aluno["id_aluno"] == id_aluno:
            aluno_encontrado = True
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")
        return False

    # Verifica se o curso existe.
    curso_encontrado = None

    for curso in dados["cursos"]:
        if curso["id_curso"] == id_curso:
            curso_encontrado = curso
            break

    if curso_encontrado is None:
        print("Curso não encontrado.")
        return False

    # Verifica se o ID da inscrição já está sendo utilizado.
    for inscricao in dados["inscricoes"]:
        if inscricao["id_inscricao"] == id_inscricao:
            print("ID de inscrição já utilizado.")
            return False

    # Verifica se o aluno já está inscrito no mesmo curso.
    for inscricao in dados["inscricoes"]:
        if (inscricao["id_aluno"] == id_aluno and
                inscricao["id_curso"] == id_curso):
            print("Aluno já inscrito neste curso.")
            return False

    # Verifica se existem vagas disponíveis.
    if curso_encontrado["vagas"] <= 0:
        print("Não existem vagas disponíveis.")
        return False

    # Cria um objeto da classe Inscricao.
    nova_inscricao = Inscricao(id_inscricao, id_aluno, id_curso)

    # Adiciona a inscrição à lista.
    dados["inscricoes"].append(nova_inscricao.__dict__)

    # Diminui uma vaga disponível no curso.
    curso_encontrado["vagas"] -= 1

    # Salva as alterações no JSON.
    salvar_dados(dados)

    print("Inscrição realizada com sucesso!")
    return True


# ==================================================
# 4. CONSULTA DE ALUNOS
# ==================================================

def consultar_aluno(id_aluno):

    # Carrega os dados existentes no JSON.
    dados = carregar_dados()

    # Procura o aluno pelo ID informado.
    for aluno in dados["alunos"]:
        if aluno["id_aluno"] == id_aluno:

            # Exibe as informações do aluno.
            print("\n--- DADOS DO ALUNO ---")
            print(f"ID: {aluno['id_aluno']}")
            print(f"Nome: {aluno['nome']}")
            print(f"E-mail: {aluno['email']}")

            return aluno

    # Informa caso o aluno não seja encontrado.
    print("Aluno não encontrado.")
    return None


# ==================================================
# 5. CONSULTA DE CURSOS
# ==================================================

def consultar_curso(id_curso):

    # Carrega os dados existentes no JSON.
    dados = carregar_dados()

    # Procura o curso pelo ID informado.
    for curso in dados["cursos"]:
        if curso["id_curso"] == id_curso:

            # Exibe as informações do curso.
            print("\n--- DADOS DO CURSO ---")
            print(f"ID: {curso['id_curso']}")
            print(f"Nome: {curso['nome']}")
            print(f"Descrição: {curso['descricao']}")
            print(f"Carga horária: {curso['carga_horaria']} horas")
            print(f"Vagas disponíveis: {curso['vagas']}")

            return curso

    # Informa caso o curso não seja encontrado.
    print("Curso não encontrado.")
    return None
