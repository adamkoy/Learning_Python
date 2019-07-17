

class Calculator:

    def add(self):
        return self.num1 + self.num2

    def subtraction(self):
            return self.num1- self.num2

    def multipy(self):
            return self.num1 * self.num2

    def divide(self):
            return self.num1 / self.num2



MyCalculator = Calculator()
MyCalculator.num1 = int(input("Please type a number"))
MyCalculator.num2 = int(input("Please enter second number"))
MyCalculator.random_function = input("please select an operator").strip().lower()

if MyCalculator.random_function == 'add':
    print(MyCalculator.add())
elif MyCalculator.random_function == 'subtract':
    print(MyCalculator.subtraction())
elif MyCalculator.random_function == "multiply":
    print(MyCalculator.multipy())

elif MyCalculator.random_function == "divide":
    print(MyCalculator.divide())
else:
    print("Sorry, input not recognized. Better luck next time")


# subtr = Calculator()
# print(subtr.subtraction())
#
# multi1 = Calculator()
# print(multi1.multipy(23,5))
#
# divide1 = Calculator()
# print(divide1.divide(100,5))
