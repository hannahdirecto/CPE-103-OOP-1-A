#Propositional Logic evaluator fro discrete math for 2-3 variables
print ("Propositional logic evaluator for discrete math")
variables = int(input("How many variable? "))
total_combinations = 2** variables


combinations_list = []

#generate the combinations
for i in range (total_combinations):
    bin_equivalent = bin(i)[2:]
    while len (bin_equivalent)<variables:
        bin_equivalent = "0" + bin_equivalent
    combinations_list.append(tuple(int(val)for val in bin_equivalent))

#main program
expression = input ("Enter the propositional logic expression: ")

if variables == 2:
    print ("A B f")
    for A,B in combinations_list:
        evaluated_expression = eval (expression)
        print (A,B, evaluated_expression)
elif variables == 3:
    print ("A B C f")
    for A,B,C in combinations_list:
        evaluated_expression = eval (expression)
        print (A,B,C, evaluated_expression)
