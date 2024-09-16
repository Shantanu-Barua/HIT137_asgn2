global_variable = 100
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'} #Fixed mixed quotes in dictionary keys. Now, all keys are correctly quoted.

def process_numbers():
    global global_variable 
    local_variable = 5 #local_vabiable → local_variable: Corrected spelling.
    numbers = [1, 2, 3, 4, 5]
    
    while local_variable > 0: # locel_variable → local_variable: Corrected spelling.
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1  # Decrease local_variable to avoid an infinite loop
    return numbers

my_set = {1, 2, 3, 4, 5}  # Fixed the set declaration my_set = {1, 2, 3, 4, 5} from {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # Fixed by removing the redundant "numbers = my_set" argument since it's not needed.

def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable
    

modify_dict()  # The modification of my_dict doesn’t require any

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    # i += 1 # i += 1 was unnecessary and corrected

if my_set is not None and my_dict['ke14'] == 10: # Changed m1_dict to my_dict
    print("Condition met!")

if 5 not in my_dict: # Changed m1_dict to my_dict
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict) # Changed m1_dict to my_dict
print(my_set)

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 