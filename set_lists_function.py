def all_functions(container):
    if type(container)==set:
        container.add(4)
        container.remove(3)
        print(container)
    elif type(container)==list:
        container.append(5)
        container.remove(6)
        print(container)
def main():
    my_list=[1,2,4,6]
    my_set={1,2,6,3}
    all_functions(my_list)
    all_functions(my_set)
main()