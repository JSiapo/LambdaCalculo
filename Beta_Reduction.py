def beta_convert(argument, application, values):
    m = [i for i, x in enumerate(application) if x == argument[0]]
    for index in m:
        application[index] = values[0]
    argument.pop(0)
    values.pop(0)
    return argument, application, values
