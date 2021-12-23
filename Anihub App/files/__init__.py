import PySimpleGUI as sg
import os
from os import remove
from PySimpleGUI.PySimpleGUI import Window, theme


def getUsername():
    """
    -> Função para pegar o nome de usuário do computador.
    """
    return os.getlogin()


def exist(name):
    """
    -> Função para verificar a existência de um arquivo no mesmo local localizado o programa.
    :param name: Nome do arquivo para fazer a verificão.
    """
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create(name, error='ERRO: Não foi possível criar o arquivo.'):
    """
    -> Função para criar um arquivo no mesmo local localizado o programa.
    :param name: Nome do arquivo para fazer a criação.
    :param error: (Opcional) O que mostrar caso a função dê erro.
    """
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print(f'\033[31m{error}\033[m')


def read(name, error='ERRO: Não foi possível ler o arquivo.'):
    """
    -> Função para ler um arquivo no mesmo local localizado o programa.
    :param name: Nome do arquivo para fazer a leitura.
    :param error: (Opcional) O que mostrar caso a função dê erro.
    """
    try:
        a = open(name, 'rt')
    except:
        print(f'\033[31m{error}\033[m')
    else:
        return a.read()
    finally:
        a.close()


def write(name, write='', error='ERRO: Não foi possível editar o arquivo.'):
    """
    -> Função para escrever algo em um arquivo no mesmo local localizado o programa.
    :param name: Nome do arquivo a qual será usado para fazer a escrita.
    :param write: Valor que será digitado no arquivo.
    :param error: (Opcional) O que mostral caso a função dê erro.
    """
    try:
        a = open(name, 'at')
    except:
        print(f'\033[31m{error}\033[m')
    else:
        a.write(write)


def delete(name):
    """
    -> Função para deletar um arquivo no mesmo local localizado o programa.
    :param name: Nome do arquivo a qual será deletado.
    """
    remove(name)