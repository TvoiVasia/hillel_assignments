from plates_list import plates_list

number_of_unique_elements = len(set(plates_list))

user_number = input("Please, enter number: ").upper()

def first_func():
    if len(user_number) == 8:
        return user_number[0:2], user_number[2], user_number[3],user_number[4], user_number[5], user_number[6:8]
    elif len(user_number) != 8:
        return False

print(first_func())

print("Number of unique elements in the list: ", number_of_unique_elements)

if user_number in plates_list:
   print("Your number detected")

elif user_number not in plates_list:
    print("Your number is not detected")

def suma():
    sum_of_elements = sum(map(int, user_number[2:6]))
    return sum_of_elements

print("Sum of all numbers in the entered number: ", suma())

