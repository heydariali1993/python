the_count = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, 1/2, ["Oh no", "Another list!"]]

for number in the_count:
    print("this is count", number)
for stock in stocks:
    print("Stock ticker:", stock)
for i in random_things:
    print("Here's a random thing:", i)

people = []
people.append("Mattan")
people.append("Ali")
people.append("Mahsa")

print(people)

people.remove("Mattan")
print(people)

for person in people:
    print("Person is:", person)

for number in range(1, 11):
    print(number, "squared is", number * number)

animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("thins is a:", type(random_things))

another_list = random_things[-1]
print(another_list)

random_things[-1][0]