def verif_primo(numero: int) -> bool:
    for i in range(2,numero):
        if numero > 1 and numero % i == 0 :
            return False
    return True


def run():
    print(verif_primo(int(input("Ingrese el numero: "))))


if __name__ == "__main__":
    run()
    