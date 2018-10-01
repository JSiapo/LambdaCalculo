"""
Convert function to lambda calc
"""

from ArgsAndApp import generate_argument_application
from Beta_Reduction import beta_convert

# expression for example is f(x+y+z)=2*(x+3)
expression = []
values_argument = []
expresion_input = input('Ingrese expresion: ')

#creamos la lista expresion del string que se capturó ignorando Los espacios en blanco
for i in expresion_input:
    if i != ' ':
        expression.append(i)

# listas creadas de argumento y aplicacion
(argument, application) = generate_argument_application(expression)

# functions

# Ver expresion original
def original_expression():
    for i in expression:
        print(i, end='')

#Ver expresion lambda
def view_expression():
    print('(λ', end='')
    for i in argument:
        print(i, end='')
    print('.',end='')
    for i in application:
        print(i, end=' ')
    print(')', end='')

#Vemos los valores ingresados de los argumentos
def values_arguments():
    for i in argument:
        values_argument.append( input('{} -> '.format(i)))
    print('Los elementos son: {}'.format(values_argument))

def view_beta_reduction(argument, application, values_argument,size_arguments):
    str_f=''
    for _ in range(0, size_arguments):
        str_f=str_f+'\n->β '
        (argument, application, values_argument) = beta_convert(argument, application, values_argument)
        str_f=str_f+'('+view_expression_beta(argument, application, values_argument)+')'
    return str_f

def view_expression_beta(argument, application, values_argument):
    str_f=''
    if len(argument) != 0:
        for _ in values_argument:
            str_f=str_f+'('
        str_f=str_f+'('
        for it in argument:
            str_f=str_f+'λ'+it
        str_f=str_f+'.'
    for it in application:
        str_f=str_f+it+' '
    if len(argument) != 0:
        str_f=str_f+')'
        for it in values_argument:
            str_f=str_f+it+')'
    return str_f

print('\n---------------------------------------\nConvert function to lambda '
      'calc\n---------------------------------------\n')

print('Function')
original_expression()
print('\n\nExpression LambdaC')
view_expression()
print('\n')
values_arguments()
print(view_beta_reduction(argument, application, values_argument,len(argument)))
