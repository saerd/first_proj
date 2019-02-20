# this will be the main file
# author: Saer Debel

import os

x = 2
print(x)

names = ["saer", 3]


for i in names:
    print(i)

if x == 2:
    x += 1

print(x)

#num_words = int(input("Enter a number: "))

def print_words(num_words):
    list_variable = []

    for _ in range(num_words):
        list_variable.append(input(""))

    space = " "
    print(space.join(list_variable), end=' ')


print_words(3)

print(names[0:2])









