

user_input =input("Please enter the string to see if there are only unique chars.\n")

def unique_check(user_input):
    answer = False
    for i in range(0,len(user_input)):
        test_char = user_input[i]
        for j in range(0,len(user_input)):
            other_char = user_input[j]

            if other_char == test_char and i == j:
                continue
            elif other_char == test_char and i != j:
                answer = False
                return answer
            else:
                answer = True

    return answer

is_unique = unique_check(user_input)

if is_unique == True:
    print("That string is unique!")
else:
    print("That string has repeating characters")