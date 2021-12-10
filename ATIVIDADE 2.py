horas = input('Que horas sao? ')
horas = int(horas)
manha_1 = 0
manha_limite = 11

tarde = 12
tarde_limite = 17

noite = 18
noite_limite = 23
if horas < 0 or horas > 23:
    print('O horario deve estar entre 0 e 23 horas')
if horas >= manha_1 and horas <= manha_limite:
    print('Bom dia senhor')
if horas >= tarde and horas <= tarde_limite:
    print('Boa tarde')
if horas >= noite and horas <= noite_limite:
    print('Boa noite')


