

user_input =input("Please enter the string to see if there are only unique chars.\n")

def unique_check(user_input):
    answer = False
    for i in range(0,len(user_input)):
        test_char = user_input[i]
        for c in user_input:
            if c == test_char:
                answer = False
                break
            else:
                answer = True

    return answer

is_unique = unique_check(user_input)

if is_unique == True:
    print("That string is unique!")
else:
    print("That string has repeating characters")