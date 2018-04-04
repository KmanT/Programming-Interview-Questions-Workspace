def permutation_check(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        char_dict = {}
        for i in range(0,len(word1)):

            char_dict[word1[i]] += 1    #Adds a char to the dictionary

            for j in range(0,len(word1)):


