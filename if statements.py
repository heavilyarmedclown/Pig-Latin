is_male = False #boolean variable
is_tall = True
if is_male and is_tall:
    print("You are a tall boy!")
elif is_male and not(is_tall):
    print("You are a short boy!")
elif not(is_male) and is_tall:
    print("You are a tall girl!")
else:
    print("You're a girl! You are short")