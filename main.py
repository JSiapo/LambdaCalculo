"""
Convert function to lambda calc
"""

from ArgsAndApp import generate_argument_application

# functions

def original_expression():
    for i in expression:
        print(i, end='')

def view_expression():
    print('(λ', end='')
    for i in argument:
        print(i, end='')
    print('.',end='')
    for i in application:
        print(i, end=' ')
    print(')', end='')


def values_arguments():
    for i in argument:
        values_argument.append( input('{} -> '.format(i)))
    print('Los elementos son: {}'.format(values_argument))


# expression for example is f(x+y+z)=2*(x+3)
expression = []
values_argument = []
expresion_input = input('Ingrese expresion: ')

for i in expresion_input:
    if i != ' ':
        expression.append(i)

print('\n---------------------------------------\nConvert function to lambda '
      'calc\n---------------------------------------\n')

(argument, application) = generate_argument_application(expression)

print('Function')
original_expression()
print('\n\nExpression LambdaC')
view_expression()
print('\n')
values_arguments()
print('\n')
