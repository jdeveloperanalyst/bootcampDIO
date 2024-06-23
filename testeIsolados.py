from datetime import datetime


def registra_log(func):
    hour_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def logs(*args, **kwargs):
        mensagem = ''
        if func.__name__ == 'deposito':
            valor = func(*args, **kwargs)
            mensagem = f'Deposito realizado no valor de R${valor} reais.'
            modalidade = 'MODALIDADE'
            linha = '=' * 15
            print('MODALIDADE')
            print(linha, modalidade, linha)
            print(f'DEPOSITO\t{hour_now}')
            
        return mensagem
    
    return logs



@registra_log
def deposito(valor=[float]):
    return f'{valor:.2f}'
    
op = deposito(5)
print(op)
