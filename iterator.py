from xml.dom.minidom import Element


class EvenNumbers:
    """Clase que implementa un iterador de todos los numeros pares, o los numeros
    pares hasta un maximo
    """
    def __init__(self, max=None):
        self.max = max
        self.__iter__()

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


def run():
    numbers = EvenNumbers()
    while True:
        try:
            #element = numbers.__next__()
            element = next(numbers)
            print(element)
        except StopIteration:
            break

if __name__ == "__main__":
    run()
