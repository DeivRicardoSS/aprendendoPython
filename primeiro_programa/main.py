import os

controle = 1
nome = ""
idade = 0
while(controle != 0):
    os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
    controle = int(input("Pressione: \n1 para cadastrar um aluno \n2 para aplicar notas\n"))
    if controle == 1:
        os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
        print("Digite as informações do aluno nos campos abaixo:")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
    elif controle == 2:
        os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
        print("Insira as notas do aluno")
        n1 = float(input("Teste: "))
        n2 = float(input("Prova: "))
        notaCorte = float(input("Nota de Corte: "))
        media = (n1 + n2)/2
        if media >= notaCorte:
            os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
            print(nome, "foi aprovado")
            print("Média: ",media)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
            print("Insira a nota de Recuperação:")
            rec = float(input("Nota de Recuperação: "))
            media = (media + rec)/2
            if media >= notaCorte:
                os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
                print(nome, "foi aprovado")
                print("Média: ",media)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
                print(nome, "foi reporvado")
                print("Média: ",media)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')#código pra limpar a tela do CMD
        print("entrada inválida!")
    controle = int(input("Fim do programa! Digite:\n 0 para encerrar;\n 1 para voltar ao inicio;"))