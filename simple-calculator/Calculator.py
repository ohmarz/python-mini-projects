import time


time.sleep(0.3)
print("-----"*25)
time.sleep(0.5)
print("CALCULATOR🧮".center(50))
time.sleep(1)

class Calculator():
    def __init__(self, num1, num2):
        # pass in function arguments
         self.num1 = num1
         self.num2 = num2


    def addition(self):
        print("-----"*25)
        time.sleep(0.5)
        print("ADDITION➕")
        result = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {result}")
        return result

    def subtraction(self):
        print("-----"*25)
        time.sleep(0.5)
        print("SUBTRACTION➖")
        result = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {result}")
        return result

    def multiplication(self):
        print("-----"*25)
        time.sleep(0.5)
        print("MULTIPLICATION✖️")
        result = self.num1 * self.num2
        print(f"{self.num1} * {self.num2} = {result}")
        return result

    def division(self):
        print("-----"*25)
        time.sleep(0.5)
        print("DIVISION➗")
        try:
         result = self.num1 / self.num2
         print(f"{self.num1} / {self.num2} = {result}")
         return result
        except ZeroDivisionError:
            print("*****" * 25)
            print("Cannot divide by ZERO⚠️")
            print("*****" * 25)
            return 0

while True:
    time.sleep(0.5)
    choice = input("Do you want to perform a calculation🧮?(y/n): ").lower()
    if choice == "y":
        try:
            print("-----" * 25)
            print("Enter the numbers to calculate:")
            time.sleep(0.3)
            num1 = int(input("Enter the first number🔢: "))
            num2 = int(input("Enter the second number🔢: "))
            # add the two parameters
            calculator = Calculator(num1, num2)

            operations = ["A:addition➕", "B:subtraction➖", "C:multiplication✖️", "D:division➗"]
            print()
            print("OPERATIONS:")
            time.sleep(0.3)
            for operation in operations:
                print(operation)

            while True:
                print()
                operation = input("Enter the operation to perform: ").upper()

                match operation:
                    case "A":
                        calculator.addition()
                    case "B":
                        calculator.subtraction()
                    case "C":
                        calculator.multiplication()
                    case "D":
                        calculator.division()
                    case _:
                        time.sleep(0.5)
                        print("*****" * 25)
                        print("INVALID OPERATION⚠️")
                        print("*****" * 25)
                        continue  # skips the following code and go back to enter operation

                another_operation = input("Do you want to perform another operation?(y/n): ").lower()
                if another_operation != "y":
                    break

        except ValueError:
            time.sleep(0.5)
            print("*****" * 25)
            print("Please enter a NUMERIC values🔢")
            print("*****" * 25)

    else:
        time.sleep(0.5)
        print("See you next time!👋👋")
        print("-----" * 25)
        break
