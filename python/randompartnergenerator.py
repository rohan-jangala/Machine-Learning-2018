import random

people = ['Michiko', 'Calder', 'Luke', 'Rohan', 'Adam', 'Will', 'Aryaman', 'Siresh', 'Amoug']

length = len(people)

for i in range(int(length/2) - 1):
    a = people.pop(random.randrange(0, len(people)))
    a += ', ' + people.pop(random.randrange(0, len(people)))

    print(a)
last = ''

for j in people:
    last += j + ', '

print(last)


# rand = random.randrange(len(people))
# a = people[rand]
# people.pop(rand)
# #
# rand = random.randrange(len(people))
# a += ', ' + people[rand]
# people.pop(rand)
# #
# rand = random.randrange(len(people))
# b = people[rand]
# people.pop(rand)
# #
# rand = random.randrange(len(people))
# b += ', ' + people[rand]
# people.pop(rand)
# #
# rand = random.randrange(len(people))
# c = people[rand]
# people.pop(rand)
# #
# rand = random.randrange(len(people))
# c += ', ' + people[rand]
# people.pop(rand)
# #
# print(a)
# print(b)
# print(c)
# print(people)
