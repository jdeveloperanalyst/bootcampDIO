from datetime import datetime


def registra_log(func):
    
    def logs(*args, **kwargs):
        mensagem = ''
        if func.__name__ == 'deposito':
            result = func(*args, **kwargs)
            linha = '=' * 10
            print(f'{linha} DEPOSITO {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {linha}')
            print('Deposito realizado no valor de R$ reais.')
            
        return result
    
    return logs



@registra_log
def deposito(valor=[float]):
    return f'{valor:.2f}'
    
op = deposito(5)
print(op)
