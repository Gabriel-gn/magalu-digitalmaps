import datetime

def horario_no_intervalo(inicio, fim, atual):
    """

    :param inicio: - horario de inicio str
    :param fim: - horario final str
    :param atual: - horario atual
    :return: True caso esteja no range, False caso não esteja
    """
    if inicio <= fim:
        return inicio <= atual <= fim
    else:
        return inicio <= atual or atual <= fim