class Player:
    def __init__(self):
        self.name = input("Informe o nome do jogador: ")
        print("Olá,", self.name, "!\nBem-vindo(a) ao DIA NORMAL...")


        self.level = 1
        self.hp = 100
        jobsMessage = '''
        Classes Disponíveis (escolha de acordo com a letra dos parênteses):
            -Pro(g)ramador(a)
            -(M)édico(a)
            -(P)rofessor(a)
        '''
        print(jobsMessage)
        self.job = input("Informe a classe do personagem: ")
        while(self.job.lower() != 'g' and self.job.lower() != 'm' and self.job.lower() != 'p'):
            self.job = input("Opção Inválida!\nInforme a classe do personagem: ")

        if(self.job == 'g'):
            self.job = 'Programador(a)'
            self.weapon = 'Garrafa de Café'
        elif(self.job == 'm'):
            self.job = 'Médico(a)'
            self.weapon = 'Bisturi'
        else:
            self.job = 'Professor(a)'
            self.weapon = 'Apagador'
