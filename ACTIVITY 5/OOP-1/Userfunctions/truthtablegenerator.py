def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0:
        return "You need to enter an integer"
    else:
        total_combinations = 2 ** number_of_variables
        combinations_list = []
        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:].zfill(number_of_variables)
            combinations_list.append(tuple(int(val) for val in bin_equivalent))
        return combinations_list


def evaluate_propositional_logic(c_list):
    expression = input("Enter the propositional logic expression: ")

    if len(c_list[0]) == 2:
        print("A B f")
        for A, B in c_list:
            print(A, B, eval(expression))
    elif len(c_list[0]) == 3:
        print("A B C f")
        for A, B, C in c_list:
            print(A, B, C, eval(expression))


evaluate_propositional_logic(generate_truthtable(3))

