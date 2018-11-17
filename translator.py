#giraffe language
#vowels -> g
#------------

#dog -> dgg
#cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #checks to see if letter is in string, to determine if vowel
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
#above function uses for loop to run through each element in phrase variable (in this case its a letter)
#each loop through phrase variable checks to see if the letter is a vowel (first if loop)
#if its a vowel the translation variable adds a 'G' to its string
#additional if/else loop at this point to distinguish capital/lower case and preserve
#final else returns the original letter parsed if it was not a vowel

print(translate(input("Enter a phrase: ")))
#prints the translate function with the user input as the phraase variable defined in the function
