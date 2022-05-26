def greet(name):
    return f"Hey {name}!"

print(greet('Ali'))

def concatenate(word_one, word_two):
    return word_one + word_two

print(concatenate('Ali', ' Heydari'))
print(concatenate(word_two= ' Heydari', word_one= 'Ali'))

def age_in_dog_years(age):
    return age * 7

print(age_in_dog_years(29))

print(greet())
print(greet('Chris', 'aditional argument'))


name = 'Mattan'
def print_different_name():
    name = 'Chris'
    print(name)

print(name)
print_different_name()
print(name)


def uppercase_and_reverse(string):
    return string.upper()[::-1]
print(uppercase_and_reverse('ali'))