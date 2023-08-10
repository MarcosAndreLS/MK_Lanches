import abc


def mostrar_cardapio():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=CARDAPIO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('-----------COMIDAS----------------|-----------BEBIDAS-------------|')
    print('1-Hamburguer ........12,00 a 15,00| 7-Refrigerante ........8,00   |')
    print('2-Pizza .............40,00 a 60,00| 8-Água mineral ........2,00   |')
    print('3-Coxinha ...........3,00 a 4,00  | 9-Água de coco ........4,00   |')
    print('4-Bomba .............3,00         | 10-Cerveja ............8,00   |')
    print('5-Pastel ............3,00 a 4,00  |                               |')
    print('6-Salsichão .........3,00         |                               |')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


def hamburguer():
    print('1-X_Bacon.........12,00')
    print('2-X_Salada........13,00')
    print('3-X_Delicia.......14,00')
    print('4-X_Calabresa.....15,00')
    print('5-Sair')


def pizza():
    print('1-Mexicana.........50,00')
    print('2-Frango...........40,00')
    print('3-Calabresa........45,00')
    print('4-Nordestina.......60,00')
    print('5-Sair')


def coxinha():
    print('1-Frango....................3,00')
    print('2-Frango com Cheddar........4,00')
    print('3-Frango com catupiry.......4,00')
    print('4-Carne.....................3,00')
    print('5-Sair')


def pastel():
    print('1-Frango....................3,00')
    print('2-Frango com Cheddar........4,00')
    print('3-Frango com catupiry.......4,00')
    print('4-Carne.....................3,00')
    print('5-Sair')


def refrigerante():
    print('1-Coca cola.................8,00')
    print('2-Guaraná...................8,00')
    print('3-Fanta laranja.............8,00')
    print('4-Fanta uva.................8,00')
    print('5-Sair')


class Lanchonete:
    def __init__(self):
        self._clientes = {}
        self._funcionarios = {}
        self._pedido = {}
        self._preco_tot = []
        self._cofre = 0

    @property
    def cofre(self):
        return self._cofre

    @cofre.setter
    def cofre(self, cofre):
        self._cofre = cofre

    def add_atendente(self, cpf):
        if cpf not in self._funcionarios.keys() and cpf not in self._clientes:
            nome = str(input('Nome: '))
            dt_nasc = str(input('Data de nascimento: '))
            salario = float(input('Salário: '))
            self._funcionarios[cpf] = Atendente(nome, cpf, dt_nasc, salario)
            return True, 'Atendente cadastrado com sucesso'
        else:
            return False, 'CPF já cadastrado'

    def add_administradores(self, cpf):
        if cpf not in self._funcionarios.keys() and cpf not in self._clientes:
            nome = str(input('Nome: '))
            dt_nasc = str(input('Data de nascimento: '))
            salario = float(input('Salário: '))
            senha = str(input('Senha: '))
            self._funcionarios[cpf] = Administradores(nome, cpf, dt_nasc, salario, senha)
            return True, 'Administrador cadastrado com sucesso'
        else:
            return False, 'CPF já cadastrado'

    def add_cliente(self, cpf):
        if cpf not in self._clientes.keys() and cpf not in self._funcionarios:
            nome = str(input('Nome: '))
            dt_nasc = str(input('Data de nascimento: '))
            self._clientes[cpf] = Cliente(nome, cpf, dt_nasc)
            return True, 'Cliente cadastrado com sucesso'
        else:
            return False, 'CPF já cadastrado'

    def realizar_pedido(self, cpf, cont, id):
        self._preco_tot.clear()
        cliente = self._clientes[cpf]
        print(f'Id do seu pedido: {id}')
        while True:
            # cliente = dc_cliente[cpf]
            print(f'Muito bem {cliente.nome}, Vamos realizar o seu pedido!')
            mostrar_cardapio()
            print('11-Calcular preço')
            print('12-Finalizar pedido')
            print('')
            opc = int(input(f'Escolha um lanche {cliente.nome}:'))
            if opc == 1:
                sinal = 0
                print(f'HUMMMM! Hambuguer, Ótima escolha {cliente.nome}')
                hamburguer()
                escolha = int(input('Escolha um tipo de Hambuguer:'))
                if escolha == 1:
                    print('X_Bacon')
                    preco = desconto = preco_desconto = 0
                    valor = 12.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    msg = "Hamburguer X-Bacon R$12.00"
                    print('Pedido realizado!')
                elif escolha == 2:
                    print('X_Salada')
                    preco = desconto = preco_desconto = 0
                    valor = 13.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                    msg = "Hamburguer X-Salada R$13.00"
                elif escolha == 3:
                    print('X_Delicia')
                    preco = desconto = preco_desconto = 0
                    valor = 14.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    msg = "Hamburguer X-Bacon R$14.00"
                    print('Pedido realizado!')
                elif escolha == 4:
                    print('X_Calabresa')
                    preco = desconto = preco_desconto = 0
                    valor = 15.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                    msg = "Hamburguer X-Bacon R$15.00"
                self._pedido[id]._historico.add(msg)
            elif opc == 2:
                sinal = 0
                print(f'HUMMMM! Pizza, Ótima escolha {cliente.nome}')
                pizza()
                escolha = int(input('Escolha um tipo de Pizza:'))
                if escolha == 1:
                    print('Pizza Mexicana:')
                    preco = desconto = preco_desconto = 0
                    valor = 50.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 2:
                    print('Pizza de Frango:')
                    preco = desconto = preco_desconto = 0
                    valor = 40.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 3:
                    print('Pizza de Calabresa:')
                    preco = desconto = preco_desconto = 0
                    valor = 45.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 4:
                    print('Pizza Nordestina:')
                    preco = desconto = preco_desconto = 0
                    valor = 60.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
            elif opc == 3:
                sinal = 0
                print(f'HUMMMM! Coxinha, Ótima escolha {cliente.nome}')
                coxinha()
                escolha = int(input('Escolha um tipo de Coxinha:'))
                if escolha == 1:
                    print('Coxinha de Frango:')
                    preco = desconto = preco_desconto = 0
                    valor = 3.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 2:
                    print('Coxinha de Frango com Cheddar:')
                    preco = desconto = preco_desconto = 0
                    valor = 4.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 3:
                    print('Coxinha de Frango com catupiry:')
                    preco = desconto = preco_desconto = 0
                    valor = 4.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 4:
                    print('Coxinha de Carne:')
                    preco = desconto = preco_desconto = 0
                    valor = 3.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
            elif opc == 4:
                sinal = 0
                print(f'HUMMMM! Bomba, Ótima escolha {cliente.nome}')
                preco = desconto = preco_desconto = 0
                valor = 3.00
                p = Pedido(preco, desconto, preco_desconto, cliente)
                self._pedido[id] = p
                self._preco_tot.append(valor)
                print('Pedido realizado!')
            elif opc == 5:
                sinal = 0
                print(f'HUMMMM! Pastel, Ótima escolha {cliente.nome}')
                pastel()
                escolha = int(input('Escolha um tipo de Pastel:'))
                if escolha == 1:
                    print('Pastel de Frango:')
                    preco = desconto = preco_desconto = 0
                    valor = 3.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 2:
                    print('Pastel de Frango com Cheddar:')
                    preco = desconto = preco_desconto = 0
                    valor = 4.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 3:
                    print('Pastel de Frango com catupiry:')
                    preco = desconto = preco_desconto = 0
                    valor = 4.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 4:
                    print('Pastel de Carne:')
                    preco = desconto = preco_desconto = 0
                    valor = 3.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
            elif opc == 6:
                sinal = 0
                print(f'HUMMMM! Salsichão, Ótima escolha {cliente.nome}')
                preco = desconto = preco_desconto = 0
                valor = 3.00
                p = Pedido(preco, desconto, preco_desconto, cliente)
                self._pedido[id] = p
                self._preco_tot.append(valor)
                print('Pedido realizado!')
            elif opc == 7:
                sinal = 0
                print(f'HUMMMM! Refrigerante, Ótima escolha {cliente.nome}')
                refrigerante()
                escolha = int(input('Escolha um tipo de Pastel:'))
                if escolha == 1:
                    print('Coca cola:')
                    preco = desconto = preco_desconto = 0
                    valor = 8.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 2:
                    print('Guaraná:')
                    preco = desconto = preco_desconto = 0
                    valor = 8.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 3:
                    print('Fanta laranja:')
                    preco = desconto = preco_desconto = 0
                    valor = 8.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
                elif escolha == 4:
                    print('Fanta uva:')
                    preco = desconto = preco_desconto = 0
                    valor = 8.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    self._pedido[id] = p
                    self._preco_tot.append(valor)
                    print('Pedido realizado!')
            elif opc == 8:
                sinal = 0
                print(f'HUMMMM! Água mineral, Ótima escolha {cliente.nome}')
                preco = desconto = preco_desconto = 0
                valor = 2.00
                p = Pedido(preco, desconto, preco_desconto, cliente)
                self._pedido[id] = p
                self._preco_tot.append(valor)
                print('Pedido realizado!')
            elif opc == 9:
                sinal = 0
                print(f'HUMMMM! Água de coco, Ótima escolha {cliente.nome}')
                preco = desconto = preco_desconto = 0
                valor = 4.00
                p = Pedido(preco, desconto, preco_desconto, cliente)
                self._pedido[id] = p
                self._preco_tot.append(valor)
                print('Pedido realizado!')
            elif opc == 10:
                sinal = 0
                print(f'HUMMMM! Cerveja, Ótima escolha {cliente.nome}')
                preco = desconto = preco_desconto = 0
                valor = 8.00
                p = Pedido(preco, desconto, preco_desconto, cliente)
                self._pedido[id] = p
                self._preco_tot.append(valor)
                print('Pedido realizado!')
            elif opc == 11:
                retorno = self._pedido[id].calcular_preco(self._preco_tot)
                if retorno <= 20:
                    print('Preço:', retorno)
                    desct = 0
                    cal_des = 0
                elif retorno > 20 and retorno <= 50:
                    des = 2/100
                    desct = self._pedido[id].calcular_desconto(des)
                    cal_des = self._pedido[id].calcular_preco_com_desconto()
                    print('Preço:', retorno)
                    print('desconto:', desct)
                    print('PREÇO FINAL = ', cal_des)
                elif retorno > 50 and retorno <= 100:
                    des = 3/100
                    desct = self._pedido[id].calcular_desconto(des)
                    cal_des = self._pedido[id].calcular_preco_com_desconto()
                    print('Preço:', retorno)
                    print('desconto:', desct)
                    print('PREÇO FINAL = ', cal_des)
                elif retorno > 100 and retorno <= 200:
                    des = 4/100
                    desct = self._pedido[id].calcular_desconto(des)
                    cal_des = self._pedido[id].calcular_preco_com_desconto()
                    print('Preço:', retorno)
                    print('desconto:', desct)
                    print('PREÇO FINAL = ', cal_des)
                elif retorno > 200:
                    des = 5/100
                    desct = self._pedido[id].calcular_desconto(des)
                    cal_des = self._pedido[id].calcular_preco_com_desconto()
                    print('Preço:', retorno)
                    print('desconto:', desct)
                    print('PREÇO FINAL = ', cal_des)
                sinal = 1
            elif opc == 12:
                if sinal == 1:
                    print(f'Seu pedido foi o {cont}º da lista')
                    print(f'Obrigado pela preferência! {cliente.nome}')
                    p = Pedido(retorno, desct, cal_des, cliente)
                    self._pedido[id] = p
                    self._cofre += self._pedido[id].calcular_preco_com_desconto()
                    break
                else:
                    print('Recalcule o preço do seu pedido digitando a opcao 11')
            else:
                print('opção inválida! escolha uma opção do cardápio.')

    def consultar_pedido(self, id):
        if id not in self._pedido.keys():
            print('Id do pedido não encontrado')
        else:
            #pedido_cliente = self._pedido[id]
            print(f'CPF = {self._pedido[id].cliente.cpf}')
            print(f'Cliente = {self._pedido[id].cliente.nome}')
            print(f'preço = {self._pedido[id].preco}')
            print(f'desconto = {self._pedido[id].desconto}')
            if self._pedido[id].preco_desconto != 0:
                print(f'VALOR FINAL = {self._pedido[id].preco_desconto}')
            else:
                print(f'VALOR FINAL = {self._pedido[id].preco}')

    def cofre_lanchonete(self, cpf):
        if cpf not in self._funcionarios.keys():
            print('Administrador não cadastrado')
        else:
            senha = str(input('Informe Senha: '))
            adm = self._funcionarios[cpf]
            LS = SistemaLogin()
            if LS.login(adm, senha) == True:
                print(f'Cofre da lanchonete {self._cofre}')
            else:
                print('Você não é um adm')

    def exibir_Funcionarios(self):
        cont = 0
        if len(self._funcionarios.keys()) != 0:
            for cpf in self._funcionarios.keys():
                self._funcionarios[cpf].mostrar_funcionario()
                cont += 1
            print(f'A lonchonete POSSUI {cont:} funcionarios!\n')
        else:
            print('\nA lanchonete não possui nenhum funcionario\n')


class Pessoa:
    def __init__(self, nome, cpf, dt_nasc):
        self._nome = nome
        self._cpf = cpf
        self._dt_nasc = dt_nasc

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def datanascimento(self):
        return self._dt_nasc

    @datanascimento.setter
    def datanascimento(self, p_dtnasc):
        self._dt_nasc = p_dtnasc


class Atendente(Pessoa):
    def __init__(self, nome, cpf, dt_nasc, salario):
        super().__init__(nome, cpf, dt_nasc)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if (self._salario < 0):
            print('salario não pode ser negativo')
        else:
            self._salario = valor

    def mostrar_funcionario(self):
        print(f'\n= Atendente =\nNome: {self._nome}\nCpf: {self._cpf}\nData de nascimennto: {self._dt_nasc}\nSalario: {self._salario}')


class Cliente(Pessoa):
    def __init__(self, nome, cpf, dt_nasc):
        super().__init__(nome, cpf, dt_nasc)


class Pedido:
    def __init__(self, preco, desconto, preco_desconto, cliente):
        self._preco = preco
        self._desconto = desconto
        self._preco_desconto = preco_desconto
        self._cliente = cliente
        self._historico = Historico()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, desconto):
        self._desconto = desconto

    @property
    def preco_desconto(self):
        return self._preco_desconto

    @preco_desconto.setter
    def preco_desconto(self, preco_desconto):
        self._preco_desconto = preco_desconto

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    def calcular_preco(self, preco_tot):
        val = sum(preco_tot)
        self._preco = val
        return self._preco

    def calcular_desconto(self, des):
        self._desconto = self._preco * des
        return self._desconto

    def calcular_preco_com_desconto(self):
        self._preco_desconto = self._preco - self._desconto
        return self._preco_desconto


class Desconto(abc.ABC):
    @abc.abstractmethod
    def calcular_desconto(self):
        pass


class Administradores(Pessoa):
    def __init__(self, nome, cpf, dt_nasc, salario, senha):
        super().__init__(nome, cpf, dt_nasc)
        self._salario = salario
        self._senha = senha

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def autenticacao(self, senha):
        return senha == self._senha

    def mostrar_funcionario(self):
        print(f'\n= Administradores =\nNome: {self._nome}\nCpf: {self._cpf}\nData de nascimennto: {self._dt_nasc}\nSalario: {self._salario}')


class Autenticavel(abc.ABC):
    """
    Interface responsável pela autenticação no sistema dos administradores da lanchonete, pois alguns dados 
    só deverão ser acessados por esses administradores.
    """

    @abc.abstractmethod
    def autenticacao(self, senha):
        """
        Método responsavel pela autenticação
        :param senha: senha de entrada
        :return: boleano, true para permitir login e false para não permitir
        """
        pass


class SistemaLogin():

    def login(self, obj, senha):
        #So irá entrar caso o obj seja instancia de Autenticavel
        if isinstance(obj, Autenticavel):
            if obj.autenticacao(senha):
                print('Login realizado com sucesso!')
                return True
            else:
                print('Senha incorreta!')
                return False
        else:
            print('Objeto não é autenticavel!')
            return False


class Historico:
    def __init__(self):
        self._historico = []

    def mostrar_historico(self):
        print(len(self._historico))
        if len(self._historico) != 0:
            print('= Pedidos =')
            for h in self._historico:
                print(h)
            print()
        else:
            print('\nSem Pedidos...\n')

    def add(self, msg):
        print(len(self._historico))
        self._historico.append(msg)
        print(self._historico[0])
        print(len(self._historico))
