n = input('Digite algo: ')
print('O Tipo Primitivo desse valor é', type(n))
print('É Somente Espaços?', n.isspace())
print('É Numérico?', n.isnumeric())
print('É Alfabético?', n.isalpha())
print('É Alfanumérico?', n.isalnum())
print('Esta em MAIÚSCULAS?', n.isupper())
print('Esta em minusculas?', n.islower())
print('Esta Capitalizada?', n.istitle())
# Capitalizada, Se a primeira letra estiver em MAIÚSCULA e o resto em minusculas.
# Saída de variáveis