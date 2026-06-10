cadastros_alunos = {}
cont = 0

def menu ():
    try:
        
        print ("----menu---")
        print ("1- Cadastrar alunos")
        print ("2- lançar notas")
        print ("3- consultar")
        print ("4- relatorio geral")
        print ("5- salvar dados")
        print ("6- sair\n")

        op = int(input("Escolha a opção desejada: "))

        if op == 1:
            cadastro()
        elif op == 2:
            Lnotas (cont)

    except ValueError:
        print("Erro! Digite apenas números. Tente novamente.")

def cadastro ():
    try:

        while cont:

            nome = input("digite o nome do aluno: ")
            idade = int(input("digite a idade do aluno: "))
            turma = input("digite a turma desse aluno: ")
            cadastros_alunos[nome] = {"idade": idade},{"turma": turma}

            op = input("Deseja cadastrar outro aluno? (s/n): ").lower()
            cont = cont + 1

            if op == "n":
                print ("cadastro realizado!")
                print(cadastros_alunos)
                print(f"quantidades de alunos cadastrados: {cont}")
                break
                
    except ValueError:
        print("Valor inválido. Tente novamente.")
    finally:
        menu ()

def Lnotas (cont):
    try:

        while cont:
            print(f"insira a nota do aluno(a): {cont}")
            not1 = float(input("digite a 1º nota: "))
            not2 = float(input("digite a 2º nota: "))
            not3 = float(input("digite a 3º nota: "))
            not4 = float(input("digite a 4º nota: "))

    except:
        print("kfas")

menu ()