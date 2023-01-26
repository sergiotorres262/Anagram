#!/usr/bin/env python3
print("Enter the first word")
cadena1 = input()
print("Enter the second word")
cadena2 = input()
dicc1 = {}
dicc2 = {}

def isAnagram(cadena1,cadena2, dicc1, dicc2):
    cadena1.strip()
    cadena2.strip()
    ayCadena1 = [char for char in cadena1.lower()]
    ayCadena2 = [char for char in cadena2.lower()]
    for i in range(len(cadena1)):
        dicc1[ayCadena1[i]] = dicc1.get(ayCadena1[i], 0) + 1
    
    for i in range(len(cadena2)):
        dicc2[ayCadena2[i]] = dicc2.get(ayCadena2[i], 0) + 1

    if dicc1 == dicc2:
        print(True)
    else:
        print(False)



if(len(cadena1) != len(cadena2)):
    print(False)
else:
    isAnagram(cadena1, cadena2, dicc1, dicc2)