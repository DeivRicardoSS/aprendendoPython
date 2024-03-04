import os
from random import randint
print("carregando funções")
historico = []
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcularCpf(string):
    n1 = int(string[:1])
    n2 = int(string[1:2])
    n3 = int(string[2:3])
    n4 = int(string[3:4])
    n5 = int(string[4:5])
    n6 = int(string[5:6])
    n7 = int(string[6:7])
    n8 = int(string[7:8])
    n9 = int(string[8:9])

    soma1 = n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2
    n10 = 11 - (soma1%11)
    if n10 > 9:
        n10 = 0
    
    soma2 = n1*11 + n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + n10*2
    n11 = 11 - (soma2%11)
    if n11 > 9:
        n10 = 0

    saida = f"{n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{n10}{n11}"
    
    print(f"O seu cpf completo é:\n{saida}")

def calcularCnpj(string):
    n1 = int(string[:1])
    n2 = int(string[1:2])
    n3 = int(string[2:3])
    n4 = int(string[3:4])
    n5 = int(string[4:5])
    n6 = int(string[5:6])
    n7 = int(string[6:7])
    n8 = int(string[7:8])
    n9 = int(string[8:9])
    n10 = int(string[9:10])
    n11 = int(string[10:11])
    n12 = int(string[11:12])

    soma1 = n1*5 + n2*4 + n3*3 + n4*2 + n5*9 + n6*8 + n7*7 + n8*6 + n9*5 + n10*4 + n11*3 + n12*2
    n13 = 11 - (soma1%11)
    if n13 > 9:
        n13 = 0
    
    soma2 = n1*6 + n2*5 + n3*4 + n4*3 + n5*2 + n6*9 + n7*8 + n8*7 + n9*6 + n10*5 + n11*4 + n12*3 + n13*2
    n14 = 11 - (soma2%11)
    if n14 > 9:
        n14 = 0

    saida = f"{n1}{n2}.{n3}{n4}{n5}.{n6}{n7}{n8}/{n9}{n10}{n11}{n12}-{n13}{n14}"
    
    print(f"O seu cnpj completo é:\n{saida}")

def calcularCpfSecret(string):
    n4 = int(string[:1])
    n5 = int(string[1:2])
    n6 = int(string[2:3])
    n7 = int(string[3:4])
    n8 = int(string[4:5])
    n9 = int(string[5:6])
    n10 = int(string[6:7])
    n11 = int(string[7:8])

    soma1 = 0
    soma2 = 0

    tentativas = 0
    max_tentativas = 90000

    while tentativas <= max_tentativas:
        n1 = randint(0,9)
        n2 = randint(0,9)
        n3 = randint(0,9)
        soma1 = 11-((n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2)%11)
        if soma1 > 9:
            soma1 = 0
        
        soma2 = 11-((n1*11 + n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + n10*2)%11)
        if soma2 > 9:
            soma2 = 0
        
        if soma2 == n11 and soma1 == n10:
            saida = f"{n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{soma1}{soma2}"
            if len(historico) == 0:
                historico.append(saida)
            else:
                ind = 0
                for x in historico:
                    
                    if x != saida:
                        ind += 1
                        if ind == len(historico):
                            historico.append(saida)
                    else:
                        ind = 0
            tentativas += 1
            return historico
            
            
        
        
        

        
    

    

controle = 0
while controle == 0:
    limpar()
    controle = int(input("Digite:\n1 para calcular CPF\n2 para calcular CNPJ\n"))
    if controle == 1:
        limpar()
        print("Calculador de dígitos verificadores de cpf:")
        cpf = input("Digite os 9 digitos do seu cpf: \n Obs: Apenas numeros\n")
        limpar()
        if len(cpf) == 9:
            calcularCpf(cpf)
        else:
            print("entrada inválida")
    elif controle == 2:
        limpar()
        print("Calculador de dígitos verificadores de cnpj:")
        cnpj = input("Digite os 12 digitos do seu cpf: \n Obs: Apenas numeros\n")
        limpar()
        if len(cnpj) == 12:
            calcularCnpj(cnpj)
        else:
            print("entrada inválida")
    elif controle == 3:
        limpar()
        print("Calcular 3 primeiros dígitos do cpf\nDigite o cpf ignorando os 3 primeiros dígitos")
        cpf = input("XXX")
        if len(cpf) == 8:
            for x in range(100):
                calcularCpfSecret(cpf)
                if x == 99:
                    print("CPF ", x ,": ",calcularCpfSecret(cpf))
                    historico = []
                
            
        else:
            print("entrada inválida")

    controle = int(input("Digite: 0 ==> Reiniciar Programa || 1 ==> encerrar\n"))
    if controle != 0:
        print("Fim do Programa!\n© Deivs")

