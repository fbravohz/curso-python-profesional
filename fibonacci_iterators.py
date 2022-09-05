import time


class FiboIter():

    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.n1 + self.n2 <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                #Tecnica swapping en python hace lo mismo que el codigo anterior
                self.n1, self.n2 = self.n2, self.aux    
                self.counter += 1
                return self.aux
        else:
            raise StopIteration


def run():
    user_entry = input("Ingresa un entero y llegare al numero mas cercano, usa none para infinito:")
    if user_entry.lower() != 'none':
        try:
            casted_user_entry = int(user_entry)
        except ValueError:
            print("Valor incorrecto, ingresa un numero, o 'none'")
            exit()
        else:
            fibonacci = FiboIter(casted_user_entry)
    else:
        fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == "__main__":
    run()
