

user_input =input("Please enter the string to see if there are only unique chars.\n")

def unique_check(user_input):
    for i in range(0,len(user_input)):

        char_check1 = user_input[i]

        for j in range(0,len(user_input)):
            char_check2 = user_input[j]
            if char_check1 == char_check2 and i != j:
                return False
                break
            else:
                return True

is_unique = unique_check(user_input)

if is_unique == True:
    print("That string is unique!")
else:
    print("That string has repeating characters")