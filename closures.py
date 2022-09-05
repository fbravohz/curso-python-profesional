from __future__ import division


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas de texto"
        return string * n
    return repeater    


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola "))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi "))


def make_division_by(n: int):
    def division(x: int):
        return x / n
    return division


def run2():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()
    run2()
