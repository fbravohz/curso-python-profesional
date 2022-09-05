from datetime import datetime


def execution_time(func):
    def wrapper(*args):
        inital_time = datetime.now() 
        if args.__sizeof__ != 0:
            print("Los argumentos con '*args' se reciben como arreglos y se accede a ellos sin '*': ",
            f"args[0] = {args[0]}, args[1] = {args[1]}.")
            print("ahora imprimimos *args, y nos separa el arreglo en espacios: ",*args,
            " pero en realidad las funciones al recibirlo lo entienden como func(x = 7, y = 6)")
            print("Este es args sin '*' sin acceder a los indices del arreglo: ", args,
            " ves que lo imprime como tupla?"," Pero si lo enviamos asi: func(args)",
            " seria enviar como func(x = (7,6), y = ?)")
        print(func(*args))
        final_time = datetime.now()
        time_elapsed = final_time - inital_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos.")
    return wrapper


#Aqui utilizamos la decoracion al estilo closures, sin el @
def suma(a: int,b: int):
    return a + b
suma = execution_time(suma)
suma(7,6)


#Aqui utilizamos la decoracion con el @
@execution_time
def multiplicacion(a: int, b: int):
    return a * b
multiplicacion(12, 15)


# #Aqui utilizamos la decoracion con el @
# @execution_time
# def random_func():
#     for _ in range(1,100000000):
#         pass
# random_func()


# #Aqui utilizamos la decoracion al estilo closures, sin el @
# def ciclo():
#     for _ in range(1,1000000):
#         pass
# ciclo = execution_time(ciclo)
# ciclo()
