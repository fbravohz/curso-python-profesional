def test_var_args(single_arg, *args):
    print(f"primer argumento normal: {single_arg}")
    print(args)
    for arg in args:
        print(arg)

test_var_args(3.5, "anunaki","kawasaki",3,5.632)


def saludame(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1} = {2}".format(key, value, "NANI???"))

saludame(nombre="manco",apellido="kapak",perro="juan gabriel")        