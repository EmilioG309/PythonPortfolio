#Calc
#A program that prompts users to enter two numbers, an operator, and prints the result of the operation

#Init
#Func
#Collect Input
def main():
    print("Welcome to EG15 Calculator!")
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    op = input("Please enter an operator(+, -, *, /): ")

#Defining Operations
    if op == "+":
        print(calc_sum(num1,num2))
    if op == "-":
        print(calc_sub(num1,num2))
    if op == "/":
        print(calc_div(num1,num2))
    if op == "*":
        print(calc_mult(num1,num2))

#Perform Addition
def calc_sum(x,y):
    sum = x + y
    return(sum)

#Perform Subtraction
def calc_sub(x,y):
    sub = x - y
    return(sub)

#Perform Division
def calc_div(x,y):
    div = x / y
    return(div)

#Perform Multiplication
def calc_mult(x,y):
    mult = x * y
    return(mult)

#Main
main()
