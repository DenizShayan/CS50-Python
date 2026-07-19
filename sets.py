# Create an empty set

s = set()

# Add elements to the set

s.add(1)
s.add(2)
s.add(4)
s.add(3)    

print(s)  # prints the set {1, 2, 3, 4} always in sorted order !!!
          # Output order is not guaranteed.

names = set()

names.add("Harry")
names.add("Ron")
names.add("Hermione")
names.add("Draco")

print(names)    # prints the set of names, order is not guaranteed. {'Draco', 'Harry', 'Ron', 'Hermione'}


numbers = set()

numbers.add(42)
numbers.add(5)
numbers.add(1000)
numbers.add(17)

print(numbers)



test_numbers = set()

test_numbers.add(42)
test_numbers.add(5)
test_numbers.add(1000)
test_numbers.add(17)

print(test_numbers)

test_numbers.add(18)

print(test_numbers)

test_numbers.remove(42)
test_numbers.add(42)

print(test_numbers)


experiment = set()

for value in [42, 5, 1000, 17, 18, 999, -3, 250]:
    experiment.add(value)

print(experiment)

experiment.remove(1000)
print(experiment)

experiment.add(1000)
print(experiment)