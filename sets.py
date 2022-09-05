def remove_duplicates_w_sets(some_list):
    set_without_duplicates = set(some_list)
    return set_without_duplicates

def remove_duplicates_w_for(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates_w_for(random_list))
    print(remove_duplicates_w_sets(random_list))


if __name__ == "__main__":
    run()