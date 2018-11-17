friends = ["jim", "karen", "kevin"]


for name in friends:
    print(name)

for index in range(10):
    print(index)
    #prints every number in the range of 0-10 excluding 10

for index in range(3, 10):
    print(index)
    #prints every number in the range of 3-10 excluding 10

for index in range(len(friends)):
    print(friends[index])
    #prints every friend in friends using a range which is the length of friends array

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")