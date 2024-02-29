# 1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
def count_vowels(word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count
    
# 2. Iterate through the following list of animals and print each one in all caps.
#   animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
def print_caps(list):
    for animal in list:
        print(animal.upper())

# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
def number3():
    for i in range(0, 21):
        print("Integer " + str(i) + " is " + ("Even" if i%2==0 else "odd"))

# 4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum_of_integers(a, b):
    return a + b

# print(count_vowels("Hello"))
# print(count_vowels("Elepante"))
# print(count_vowels("Evil"))
# print_caps(['tiger', 'elephant', 'monkey', 'zebra', 'panther'])
# number3()