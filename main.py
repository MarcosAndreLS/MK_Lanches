from classes import Lanchonete
from classes import Autenticavel
from classes import Administradores
import random

Autenticavel.register(Administradores)

cont = 0
#Desconto.register(Pedido)
lan = Lanchonete()


def menu():
    try:
        op = int(input('-----------MENU-----------\n1 - cadastrar administrador\n2 - cadastrar Atendente\n3 - cadastrar cliente\n4 - realizar um pedido\n5 - consultar um pedido\n6 - mostrar cofre da lanchonete\n7 - listar funcionarios\n8 - listar clientes\n0 - sair\n--------------------------\n'))
        return op
    except:
        print('Opção digitado não é um inteiro')


while True:
    op = menu()

    if op == 2:
        cpf = str(input('CPF:'))
        print(lan.add_atendente(cpf)[1])
    elif op == 3:
        cpf = str(input('CPF: '))
        print(lan.add_cliente(cpf)[1])
    elif op == 4:
        num = random.sample(range(1, 100 + 1), 1)
        id = num[0]
        cpf = str(input('CPF: '))
        if cpf not in lan._clientes.keys():
            print('Cliente não cadastrado')
        else:
            cont += 1
            lan.realizar_pedido(cpf, cont, id)
    elif op == 5:
        try:
            IdP = int(input('Id do pedido:'))
            lan._pedido[IdP]._historico.mostrar_historico()
            lan.consultar_pedido(IdP)
        except:
            print('Error')
    elif op == 6:
        cpf = str(input('CPF: '))
        lan.cofre_lanchonete(cpf)
    elif op == 1:
        cpf = str(input('CPF: '))
        print(lan.add_administradores(cpf)[1])
    elif op == 7:
        lan.exibir_Funcionarios()
    elif op == 8:
        lan.exibir_clientes()
    elif op == 0:
        print('\nSaindo da execução...\n')
        break
    else:
        print('Opcao invalida')
