def run():
    my_set1 = {2,3,4,5,6,7}
    my_set2 = {5,6,7,8,9,10}

    my_set_union = my_set1 | my_set2
    print("Esto es union: ",my_set_union)

    my_set_interseccion = my_set1 & my_set2
    print("Esto es interseccion: ",my_set_interseccion)

    my_set_diferencia1 = my_set1 - my_set2
    print("Esto es diferencia 1: ", my_set_diferencia1)
    my_set_diferencia2 = my_set2 - my_set1
    print("Esto es diferencia 2: ", my_set_diferencia2)

    my_set_dif_simetrica1 = my_set1 ^ my_set2
    print("Esto es diferencia simetrica 1:",my_set_dif_simetrica1)
    my_set_dif_simetrica2 = my_set2 ^ my_set1
    print("Esto es diferencia simetrica 2:",my_set_dif_simetrica2)
if __name__ == "__main__":
    run()
