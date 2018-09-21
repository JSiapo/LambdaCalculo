from InfixToPrefix import infix_to_prefix


def generate_argument_application(expression):
    position_equals = 0
    position_par = 0
    for element in expression:
        if element == '=':
            break
        else:
            position_equals = position_equals + 1

    for element in expression:
        if element == '(':
            break
        else:
            position_par = position_par + 1

    argument = []
    for element in range(position_par, position_equals):
        if 123 > ord(expression[element]) > 96:
            argument.append(expression[element])

    application = []
    for element in range(position_equals + 1, len(expression)):
        application.append(expression[element])

    application = infix_to_prefix(convert_list_string(application))

    return argument, application

def convert_list_string(expresion):
    cadena=''
    for i in expresion:
        cadena += i
    return cadena
