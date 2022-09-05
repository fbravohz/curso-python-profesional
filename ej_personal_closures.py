#Entiendo que los closures son una alternativa a pasar parametros para alimentar una funcion interna
#Para ello definamos puntos clave:
#1. La funcion interna retorna el resultado requerido
#2. la funcion interna es retornada por medio de la funcion externa,
#       Algo como func_externa(<argumentos>) -> func_interna():
#       es decir si una variable1 = func_externa(<argumentos>)
#       variable1 contendra un obj tipo func_interna()
#       que al llamar variable1 seria como si llamaramos desde afuera func_interna()
#       pero con los argumentos que ya guardamos para func_externa() al declara variable1
def make_multiplier(x):
    def multiplier(n):
        return x*n
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

#Esta linea nos arroja este resultado <class 'function'>
print(type(times10))

print(times10(3))
print(times4(5))
print(times10(times4(2)))
