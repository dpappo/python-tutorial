def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)


# python has a built in input function, which can be assigned to a variable
print("type in your name and hit enter")
name = input()

say_hi(name)
