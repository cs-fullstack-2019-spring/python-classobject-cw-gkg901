def main():
    # ex1()
    # ex2()
    ex3()
    # ex4()

class Dog:
    def __init__(self,name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender


    def printAll(self):
        print(self.name,self.breed,self.color,self.gender)



class Person:
    def __init__(self,name = "",weight = 0,height = 0):
        self.name = name
        self.weight = weight
        self.height = height


    # FUNCTION ALSO CHANGES WEIGHT AND HEIGHT
    def bmiCalc(self,weight=0,height=0):
        self.weight = weight
        self.height = height

        print((weight / (height * height)) *  703)


    def printAll(self):
        print(f'{self.name},{self.weight},{self.height}')



class Product:
    def __init__(self,name="",price=0,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity


    def changeProduct(self,name="",price=0,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity


    def printAll(self):
        print(f'{self.name},{self.price},{self.quantity}')





# Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.

def ex1():

    dog1 = Dog("Fido","poodle","brown","male")
    dog1.printAll()

# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
def ex2():

    userInput =""
    while (userInput != "="):
        userInput = input("enter something")




# In your main file create three Person objects.
# Change the weight and height of each one.
# Afterwards, print the BMI (body mass index) of each Person.
# If you don’t know how to calculate BMI, look at the code I provided for you.
def ex3():

    fighter1 = Person("Blanka",280,62)
    fighter2 = Person("Akuma",248,73)
    fighter3 = Person("Balrog",312,76)

    fighter1.printAll()
    fighter2.printAll()
    fighter3.printAll()


    fighter1 = Person("Blanka",303,60)
    fighter2 = Person("Akuma",260,72)
    fighter3 = Person("Balrog",326,77)


    fighter1.printAll()
    fighter2.printAll()
    fighter3.printAll()

    fighter2.printAll()
    fighter2.bmiCalc(250,73)
    fighter2.printAll()


#
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have changeProduct:
#
# a) If changeProduct has one parameter, it can change the name of the product.
#
#     b) If changeProduct has two parameters it can change the name and price of the product.
#
#     c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
#
#     Create an object of Product in your problem4 function and print all of it's attributes.
def ex4():

    item1 = Product("OxyClean",49,10000)

    item1.printAll()
    item1.changeProduct("Flexseal")
    item1.changeProduct("Flexseal",37)
    item1.changeProduct("Flexseal",37,30000)
    item1.printAll()








if __name__ == '__main__':
    main()