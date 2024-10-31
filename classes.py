import abc


def mostrar_cardapio():
    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=CARDAPIO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
    print('|-----------COMIDAS----------------|-----------BEBIDAS---------------------|')
    print('|1-Hamburguer ........12,00 a 15,00| 7-Refrigerante ........8,00           |')
    print('|2-Pizza .............40,00 a 60,00| 8-Água mineral ........2,00           |')
    print('|3-Coxinha ...........3,00 a 4,00  | 9-Água de coco ........4,00           |')
    print('|4-Bomba .............3,00         | 10-Cerveja ............4,00 a 16,00   |')
    print('|5-Pastel ............3,00 a 4,00  |                                       |')
    print('|6-Salsichão .........3,00         |                                       |')
    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')


def hamburguer():
    print()
    print('1-X_Bacon.........12,00')
    print('2-X_Salada........13,00')
    print('3-X_Delicia.......14,00')
    print('4-X_Calabresa.....15,00')
    print()


def pizza():
    print()
    print('1-Mexicana.........50,00')
    print('2-Frango...........40,00')
    print('3-Calabresa........45,00')
    print('4-Nordestina.......60,00')
    print()


def coxinha():
    print()
    print('1-Frango....................3,00')
    print('2-Frango com Cheddar........4,00')
    print('3-Frango com catupiry.......4,00')
    print('4-Carne.....................3,00')
    print()


def pastel():
    print()
    print('1-Frango....................3,00')
    print('2-Frango de queijo..........5,00')
    print('3-Frango com catupiry.......4,00')
    print('4-Carne.....................3,00')
    print()


def cerveja():
    print()
    print('1-Heineken long neck...........................6,00')
    print('2-Heineken 600ml..............................16,00')
    print('3-Skol lonk neck...............................4,00')
    print('4-Skol 600ml...................................8,00')
    print('5-Budweiser long neck..........................5,00')
    print('6-Crystal 269ml................................2,10')
    print('7-Itaipava 1L..................................9,00')
    print('8-Berrió 350ml.................................3,00')
    print()


def refrigerante():
    print()
    print('1-Coca cola.................8,00')
    print('2-Guaraná...................8,00')
    print('3-Fanta laranja.............8,00')
    print('4-Fanta uva.................8,00')
    print()

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
            print()
            return True, 'Atendente cadastrado com sucesso'
        else:
            print()
            return False, 'CPF já cadastrado'

    def add_administradores(self, cpf):
        if cpf not in self._funcionarios.keys() and cpf not in self._clientes:
            nome = str(input('Nome: '))
            dt_nasc = str(input('Data de nascimento: '))
            salario = float(input('Salário: '))
            senha = str(input('Senha: '))
            self._funcionarios[cpf] = Administradores(nome, cpf, dt_nasc, salario, senha)
            print()
            return True, 'Administrador cadastrado com sucesso'
        else:
            print()
            return False, 'CPF já cadastrado'

    def add_cliente(self, cpf):
        if cpf not in self._clientes.keys() and cpf not in self._funcionarios:
            nome = str(input('Nome: '))
            dt_nasc = str(input('Data de nascimento: '))
            self._clientes[cpf] = Cliente(nome, cpf, dt_nasc)
            print()
            return True, 'Cliente cadastrado com sucesso'
        else:
            print()
            return False, 'CPF já cadastrado'

    def realizar_pedido(self, cpf, cont, id):
        go = 0
        for k in self._funcionarios.keys():
            if isinstance(self._funcionarios[k], Atendente):
                go = 1
        if go == 1:
            self._preco_tot.clear()
            cliente = self._clientes[cpf]
            print()
            print(f'Id do seu pedido: {id}')
            preco = desconto = preco_desconto = 0
            p = Pedido(preco, desconto, preco_desconto, cliente)
            self._pedido[id] = p
            if cpf not in self._pedido:
                self._pedido[cpf] = []
            self._pedido[cpf].append(p)
            msg = f"ID do pedido: {id}"
            self._pedido[id]._historico.add(msg)
            while True:
                print(f'Muito bem {cliente.nome}, Vamos realizar o seu pedido!')
                print()
                mostrar_cardapio()
                print()
                print('11-Calcular preço')
                print('12-Finalizar pedido')
                print()
                opc = int(input(f'Escolha uma opção {cliente.nome}:'))
                print()
                if opc == 1:
                    sinal = 0
                    print(f'HUMMMM! Hambuguer, Ótima escolha {cliente.nome}')
                    hamburguer()
                    try:
                        escolha = int(input('Escolha um tipo de Hambuguer:'))
                        if escolha == 1:
                            print('X_Bacon')
                            valor = 12.00
                            msg = f"Hamburguer X-Bacon R${valor:.2f}"
                        elif escolha == 2:
                            print('X_Salada')
                            valor = 13.00
                            msg = f"Hamburguer X-Salada R${valor:.2f}"
                        elif escolha == 3:
                            print('X_Delicia')
                            valor = 14.00
                            msg = f"Hamburguer X-Delicia R${valor:.2f}"
                        elif escolha == 4:
                            print('X_Calabresa')
                            valor = 15.00
                            msg = f"Hamburguer X-Calabresa R${valor:.2f}"
                        else:
                            print('opção invalida')
                        self._preco_tot.append(valor)
                        print('Pedido realizado!')
                        self._pedido[id]._historico.add(msg)
                    except:
                        print('Error')
                elif opc == 2:
                    sinal = 0
                    print(f'HUMMMM! Pizza, Ótima escolha {cliente.nome}')
                    pizza()
                    try:
                        escolha = int(input('Escolha um tipo de Pizza:'))
                        if escolha == 1:
                            print('Pizza Mexicana:')
                            valor = 50.00
                            msg = f"Pizza Mexicana R${valor:.2f}"
                        elif escolha == 2:
                            print('Pizza de Frango:')
                            valor = 40.00
                            msg = f"Pizza de frango R${valor:.2f}"
                        elif escolha == 3:
                            print('Pizza de Calabresa:')
                            valor = 45.00
                            msg = f"Pizza de Calabreza R${valor:.2f}"
                        elif escolha == 4:
                            print('Pizza Nordestina:')
                            valor = 60.00
                            msg = f"Pizza Nordestina R${valor:.2f}"
                        else:
                            print('opção invalida')
                        self._preco_tot.append(valor)
                        print('Pedido realizado!')
                        self._pedido[id]._historico.add(msg)
                    except:
                        print('ERRO')
                elif opc == 3:
                    sinal = 0
                    print(f'HUMMMM! Coxinha, Ótima escolha {cliente.nome}')
                    coxinha()
                    try:
                        escolha = int(input('Escolha um tipo de Coxinha:'))
                        if escolha == 1:
                            print('Coxinha de Frango:')
                            valor = 3.00
                            msg = f"Coxinha de Frango R${valor:.2f}"
                        elif escolha == 2:
                            print('Coxinha de Frango com Cheddar:')
                            valor = 4.00
                            msg = f"Coxinha de Frango com Cheddar R${valor:.2f}"
                        elif escolha == 3:
                            print('Coxinha de Frango com catupiry:')
                            valor = 4.00
                            msg = f"Coxinha de Frango com catupiry R${valor:.2f}"
                        elif escolha == 4:
                            print('Coxinha de Carne:')
                            valor = 3.00
                            msg = f"Coxinha de Carne R${valor:.2f}"
                        else:
                            print('opção invalida')
                        self._preco_tot.append(valor)
                        print('Pedido realizado!')
                        self._pedido[id]._historico.add(msg)
                    except:
                        print('ERRO')
                elif opc == 4:
                    sinal = 0
                    print(f'HUMMMM! Bomba, Ótima escolha {cliente.nome}')
                    valor = 3.00
                    self._preco_tot.append(valor)
                    msg = f"Bomba R${valor:.2f}"
                    print('Pedido realizado!')
                    self._pedido[id]._historico.add(msg)
                elif opc == 5:
                    sinal = 0
                    print(f'HUMMMM! Pastel, Ótima escolha {cliente.nome}')
                    pastel()
                    try:
                        escolha = int(input('Escolha um tipo de Pastel:'))
                        if escolha == 1:
                            print('Pastel de Frango:')
                            valor = 3.00
                            msg = f"Pastel de Frango R${valor:.2f}"
                        elif escolha == 2:
                            print('Pastel de queijo:')
                            valor = 5.00
                            msg = f"Pastel de queijo R${valor:.2f}"
                        elif escolha == 3:
                            print('Pastel de Frango com catupiry:')
                            valor = 4.00
                            msg = f"Pastel de Frango com catupiry R${valor:.2f}"
                        elif escolha == 4:
                            print('Pastel de Carne:')
                            valor = 3.00
                            msg = f"Pastel de Carne R${valor:.2f}"
                        else:
                            print('opção invalida')
                        self._preco_tot.append(valor)
                        print('Pedido realizado!')
                        self._pedido[id]._historico.add(msg)
                    except:
                        print('ERRO')
                elif opc == 6:
                    sinal = 0
                    print(f'HUMMMM! Salsichão, Ótima escolha {cliente.nome}')
                    valor = 3.00
                    self._preco_tot.append(valor)
                    msg = f"Salsichão R${valor:.2f}"
                    print('Pedido realizado!')
                    self._pedido[id]._historico.add(msg)
                elif opc == 7:
                    sinal = 0
                    print(f'HUMMMM! Refrigerante, Ótima escolha {cliente.nome}')
                    refrigerante()
                    try:
                        escolha = int(input('Escolha um tipo de refrigerante:'))
                        if escolha == 1:
                            print('Coca cola:')
                            valor = 8.00
                            msg = f"Refrigerante Coca cola R${valor:.2f}"
                        elif escolha == 2:
                            print('Guaraná:')
                            valor = 8.00
                            msg = f"Refrigerante Guaraná R${valor:.2f}"
                        elif escolha == 3:
                            print('Fanta laranja:')
                            valor = 8.00
                            msg = f"Refrigerante Fanta laranja R${valor:.2f}"
                        elif escolha == 4:
                            print('Fanta uva:')
                            valor = 8.00
                            msg = f"Refrigerante Fanta uva R${valor:.2f}"
                        else:
                            print('opção invalida')
                        self._preco_tot.append(valor)
                        print('Pedido realizado!')
                        self._pedido[id]._historico.add(msg)
                    except:
                        print('ERRO')
                elif opc == 8:
                    sinal = 0
                    print(f'HUMMMM! Água mineral, Ótima escolha {cliente.nome}')
                    valor = 2.00
                    self._preco_tot.append(valor)
                    msg = f"Água mineral R${valor:.2f}"
                    print('Pedido realizado!')
                    self._pedido[id]._historico.add(msg)
                elif opc == 9:
                    sinal = 0
                    print(f'HUMMMM! Água de coco, Ótima escolha {cliente.nome}')
                    valor = 4.00
                    self._preco_tot.append(valor)
                    msg = f"Água de coco R${valor:.2f}"
                    print('Pedido realizado!')
                    self._pedido[id]._historico.add(msg)
                elif opc == 10:
                    sinal = 0
                    print(f'HUMMMM! Cerveja, Ótima escolha {cliente.nome}')
                    cerveja()
                    try:
                        escolha = int(input('Escolha um tipo de cerveja:'))
                        if escolha == 1:
                            print('Heineken long neck:')
                            valor = 6
                            msg = f"Cerveja Heineken long neck R${valor:.2f}"
                        elif escolha == 2:
                            print('Heineken 600ml:')
                            valor = 16
                            msg = f"Cerveja Heineken 600ml R${valor:.2f}"
                        elif escolha == 3:
                            print('Skol long neck:')
                            valor = 4
                            msg = f"Cerveja Skol long neck R${valor:.2f}"
                        elif escolha == 4:
                            print('Skol 600ml:')
                            valor = 8
                            msg = f"Cerveja Skol 600ml R${valor:.2f}"
                        elif escolha == 5:
                            print('Budweiser long neck:')
                            valor = 5
                            msg = f"Cerveja Budweiser long neck R${valor:.2f}"
                        elif escolha == 6:
                            print('Crystal 269ml:')
                            valor = 2.10
                            msg = f"Cerveja Crystal 269ml R${valor:.2f}"
                        elif escolha == 7:
                            print('Itaipava 1L:')
                            valor = 9
                            msg = f"Cerveja Itaipava 1L R${valor:.2f}"
                        elif escolha == 8:
                            print('Berrió 350ml:')
                            valor = 3
                            msg = f"Cerveja Berrió 350ml R${valor:.2f}"
                        else:
                            print('opção invalida')
                        self._preco_tot.append(valor)
                        print('Pedido realizado!')
                        self._pedido[id]._historico.add(msg)
                    except:
                        print('ERRO')
                elif opc == 11:
                    retorno = self._pedido[id].calcular_preco(self._preco_tot)
                    if retorno <= 20:
                        print(f'Preço: {retorno:.2f}')
                        desct = 0
                        cal_des = 0
                    elif retorno > 20 and retorno <= 50:
                        des = 2/100
                        desct = self._pedido[id].calcular_desconto(des)
                        cal_des = self._pedido[id].calcular_preco_com_desconto()
                        print(f'Preço: {retorno:.2f}')
                        print(f'desconto: {desct:.2f}')
                        print(f'PREÇO FINAL = {cal_des:.2f}')
                    elif retorno > 50 and retorno <= 100:
                        des = 3/100
                        desct = self._pedido[id].calcular_desconto(des)
                        cal_des = self._pedido[id].calcular_preco_com_desconto()
                        print(f'Preço: {retorno:.2f}')
                        print(f'desconto: {desct:.2f}')
                        print(f'PREÇO FINAL = {cal_des:.2f}')
                    elif retorno > 100 and retorno <= 200:
                        des = 4/100
                        desct = self._pedido[id].calcular_desconto(des)
                        cal_des = self._pedido[id].calcular_preco_com_desconto()
                        print(f'Preço: {retorno:.2f}')
                        print(f'desconto: {desct:.2f}')
                        print(f'PREÇO FINAL = {cal_des:.2f}')
                    elif retorno > 200:
                        des = 5/100
                        desct = self._pedido[id].calcular_desconto(des)
                        cal_des = self._pedido[id].calcular_preco_com_desconto()
                        print(f'Preço: {retorno:.2f}')
                        print(f'desconto: {desct:.2f}')
                        print(f'PREÇO FINAL = {cal_des:.2f}')
                    sinal = 1
                elif opc == 12:
                    cpf_aten = str(input('Qual o cpf do atendente que lhe atendeu?'))
                    if cpf_aten in self._funcionarios.keys() and isinstance(self._funcionarios[cpf_aten], Atendente):
                        if sinal == 1:
                            print(f'Seu pedido foi o {cont}º da lista')
                            print(f'Obrigado pela preferência! {cliente.nome}')
                            self._pedido[id].preco = retorno
                            self._pedido[id].desconto = desct
                            self._pedido[id].preco_desconto = cal_des
                            self._cofre += self._pedido[id].calcular_preco_com_desconto()
                            self._funcionarios[cpf_aten]._comissao.append(retorno)
                            break
                        else:
                            print('Recalcule o preço do seu pedido digitando a opcao 11')
                    else:
                        print(f'número de cpf ({cpf_aten}) do atendente não cadastrado')
                else:
                    print('opção inválida! escolha uma opção do cardápio.')
        else:
            print('É preciso ter pelo menos um atendente cadastrado para realizar seu pedido')

    def consultar_pedido(self, id):
        if id not in self._pedido.keys():
            print('Id do pedido não encontrado')
        else:
            self._pedido[id].mostrar_pedido()

    def exibir_pedidos(self):
        cont = 0
        for cpf, cliente in self._clientes.items():
            if cpf in self._pedido:
                for pedido in self._pedido[cpf]:
                    print(f"Pedidos do cliente {cliente.nome}")
                    pedido.mostrar_pedido()
                    print()
                    pedido._historico.mostrar_historico()
                    print()
                    cont += 1
        if cont == 0:
            print('A lanchonete não possui nenhum pedido\n')

    def cofre_lanchonete(self, cpf):
        if cpf not in self._funcionarios.keys() and cpf not in self._clientes.keys():
            print('CPF não cadastrado no sistema')
        else:
            senha = str(input('Informe Senha: '))
            try:
                adm = self._funcionarios[cpf]
                LS = SistemaLogin()
                if LS.login(adm, senha) == True:
                    print(f'Cofre da lanchonete: R${self._cofre:.2f}')
                else:
                    print('Você não é um adm')
            except:
                print('Clientes não tem acesso')

    def exibir_Funcionarios(self):
        cont = 0
        if len(self._funcionarios.keys()) != 0:
            for cpf in self._funcionarios.keys():
                self._funcionarios[cpf].mostrar_funcionario()
                print(f'bonificação: {self._funcionarios[cpf].get_bonificacao():.2f}')
                cont += 1
            print(f'A lanchonete POSSUI {cont:} funcionarios!\n')
        else:
            print('\nA lanchonete não possui nenhum funcionario\n')

    def exibir_clientes(self):
        cont = 0
        if len(self._clientes.keys()) != 0:
            for cpf in self._clientes.keys():
                self._clientes[cpf].mostrar_cliente()
                cont += 1
                if cpf in self._pedido.keys():
                    for order in self._pedido[cpf]:
                        order._historico.mostrar_historico()
                        print()
                else:
                    print(f"Cliente {self._clientes[cpf].nome} não fez nenhum pedido")
            print(f'A lanchonete POSSUI {cont:} clientes cadastrados!\n')
        else:
            print('\nA lanchonete não possui nenhum cliente cadastrado\n')

    def buscar_cpf(self):
        try:
            op = int(input('1 - Buscar funcionarios\n2 - Buscar cliente\nEscolha uma opção\n>>> '))
            if op == 1:
                cpf = str(input('Digite o cpf: '))
                if cpf in self._funcionarios.keys():
                    self._funcionarios[cpf].mostrar_funcionario()
                    print(f'bonificação: {self._funcionarios[cpf].get_bonificacao():.2f}')
                else:
                    print('\nCpf não encontrado\n')
            elif op == 2:
                cpf = str(input('Digite o cpf: '))
                if cpf in self._clientes.keys():
                    self._clientes[cpf].mostrar_cliente()
                    if cpf in self._pedido.keys():
                        for order in self._pedido[cpf]:
                            order._historico.mostrar_historico()
                            print()
                    else:
                        print(f"Cliente {self._clientes[cpf].nome} não fez nenhum pedido")
                else:
                    print('\nCpf não encontrado\n')
            else:
                print('Opção invalida')
        except:
            print('ERRO')


class Pessoa(abc.ABC):
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
    def dt_nasc(self):
        return self._dt_nasc

    @dt_nasc.setter
    def dt_nasc(self, dt_nasc):
        self._dt_nasc = dt_nasc


class Atendente(Pessoa):
    def __init__(self, nome, cpf, dt_nasc, salario):
        super().__init__(nome, cpf, dt_nasc)
        if salario < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = salario
        self._comissao = []

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    def mostrar_funcionario(self):
        print(f'\n= Atendente =\nNome: {self.nome}\nCpf: {self.cpf}\nData de nascimennto: {self.dt_nasc}\nSalario: {self._salario}\n')

    def get_bonificacao(self):
        return self._salario*0.05 + sum(self._comissao) * 0.10


class Cliente(Pessoa):
    def __init__(self, nome, cpf, dt_nasc):
        super().__init__(nome, cpf, dt_nasc)

    def mostrar_cliente(self):
        print(f'\n= Cliente =\nNome: {self.nome}\nCpf: {self.cpf}\nData de nascimennto: {self.dt_nasc}')


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

    def mostrar_pedido(self):
        print(f'CPF = {self.cliente.cpf}')
        print(f'Cliente = {self.cliente.nome}')
        print(f'preço = {self.preco:.2f}')
        print(f'desconto = {self.desconto:.2f}')
        if self.preco_desconto != 0:
            print(f'VALOR FINAL = {self.preco_desconto:.2f}')
        else:
            print(f'VALOR FINAL = {self.preco:.2f}')


class Administradores(Pessoa):
    def __init__(self, nome, cpf, dt_nasc, salario, senha):
        super().__init__(nome, cpf, dt_nasc)
        if salario < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = salario
        self._senha = senha

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    def autenticacao(self, senha):
        return senha == self._senha

    def mostrar_funcionario(self):
        print(f'\n= Administrador =\nNome: {self.nome}\nCpf: {self.cpf}\nData de nascimennto: {self.dt_nasc}\nSalario: {self._salario}')

    def get_bonificacao(self):
        return self._salario*0.20


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
        if len(self._historico) != 0:
            print('= Pedidos =')
            for h in self._historico:
                print(h)
            print()
        else:
            print('\nSem Pedidos...\n')

    def add(self, msg):
        self._historico.append(msg)
