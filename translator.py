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

print(translate(input("Enter a phrase: ")))