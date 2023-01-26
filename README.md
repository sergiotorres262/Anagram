# Anagram Checker

This program checks if two given strings are anagrams of each other.

## How it works

The program takes two strings as input and converts them to lowercase. It then creates two dictionaries, one for each string, with the characters of the string as keys and their frequency as values. The program then compares the two dictionaries and if they are equal, it prints "True", indicating that the strings are anagrams of each other. If the dictionaries are not equal, the program prints "False", indicating that the strings are not anagrams.

## Usage

 Run the program by executing the command  ./anagram.py in the terminal.
 The program will prompt you to enter the two strings you want to check for anagrams.
 The program will then determine if the two strings are anagrams and print the result.
 
Note: If the two strings have different lengths, the program will automatically print "False" as they cannot be anagrams.

## Example

  Input:
  cadena1 = "escalonamiento"
  cadena2 = "ocasionalmente"

### Output:

{'e': 2, 's': 1, 'c': 1, 'a': 2, 'l': 1, 'o': 2, 'n': 2, 'm': 1, 'i': 1, 't': 1}

{'o': 2, 'c': 1, 'a': 2, 's': 1, 'i': 1, 'n': 2, 'l': 1, 'm': 1, 'e': 2, 't': 1}

True
