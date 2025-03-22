import datetime
# from datetime import date -> importa somente a função date do módulo datetime

data = datetime.date(2025, 6, 22)
# data = date(2025, 3, 22) -> retilaria o módulo da qual foi importada, e aplicaria diretamente a função importada
print(data)

hoje = datetime.date.today()
print(hoje)

data_completa = datetime.datetime(2025, 6, 22, 22, 10, 20)
data_completa2 = datetime.datetime(2025, 6, 22)
data_completa3 = datetime.datetime.today()
print(data_completa)
print(data_completa2)
print(data_completa3)

hora = datetime.time(10, 15, 24)
print(hora)

nova_data = data_completa + datetime.timedelta(weeks=1)
print(data_completa)
print(nova_data)

data_formatada = data.strftime('%d/%m/%Y')
print(data_formatada)
print(type(data_formatada))

data_str = '2025-10-31 10:20'
mascara = '%Y-%m-%d %H:%M'
data_formatada2 = datetime.datetime.strptime(data_str, mascara) # funciona somente para mesmo layout, altera somete as posições
print(data_formatada2)

import pytz # importa os fuso horários

horaTZOslo = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
horaTZSaoPaulo = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print(horaTZOslo)
print(horaTZSaoPaulo)

TZdatetimeOslo = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2), 'BRT')) # forma de pegar horário com timezone com datetime
print(TZdatetimeOslo)
