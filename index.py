# Assignment 3A
# Redo the programs on assignment2 but now with functions


def getNameInput():
    global name
    name = input("Enter your name: ")

def getAgeInput():
    global age 
    age = input("Enter your age: ")

def getAddressInput():
    global address
    address = input("Enter your address: ")

def printAll():
    print("Hi, my name is " + name + ". I am "+ age +" years old and I live in " + address +".")

getNameInput()
getAgeInput()
getAddressInput()
printAll()