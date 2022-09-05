def mayusculas(func: callable):
    def envoltura(texto: str):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"


print(mensaje("Cesar"))