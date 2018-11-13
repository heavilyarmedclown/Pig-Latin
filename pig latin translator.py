pyg = 'ay' 

original = raw_input('Enter a word:') 
#ask for user input
if len(original) > 0 and original.isalpha(): #test for input and only letters
  word = original.lower() #returns var as lowercase string
  first = word[0] #isolates first letter
  new_word = word[1:len(new_word)] + first + pyg #translation
  print new_word
else:
  print 'empty' #no user input or incorrect variables
