#Emilio & Kacper
#This program runs a slot machine

#Init
import random

sy = ["☆","☆","☆","♡","♡","♢","7", "7"] #Added more symbols to lower the chance of rolling a 7

#Func
def spins():
    cd = 0
    #Welcomes player
    print("\033[1m===== Welcome To The 3-Slot Machine =====\033[0m")
    print("")
    print("Slot Symbols: ☆, ♡, ♢, 7")
    print("")
    print(f"You have {cd} credits. Each spin costs 10 credits. ")
    print("")
    while True:
        menu = input("[S]pin, [D]eposit Credits, [T]est or [E]xit And Cash Out: ")
        print("")
        if menu == "S":
            #The definition of the roll
            if cd < 10:
                print("Not enough credits to spin. Deposit more credits.")
                print("")
                continue
            cd = cd - 10
            roll = [random.choice(sy), random.choice(sy), random.choice(sy)]
            print("Spin result:", roll)
            if roll[0] == roll[1] == roll[2]:
                #Win or don't
                if roll[0] == "7":
                    print("\033[1mJACKPOT! 7 - 7 - 7\033[0m")
                    print("+310 Credits")
                    cd = cd + 1010
                    print("")
                    print("Credits: ", cd)
                else:
                    print("Small Win!")
                    print("+60 Credits")
                    cd = cd + 310
                    print("")
                    print("Credits: ", cd)
            else:
                print("No win this time.")
                print("")
                print("Credits: ", cd)
        #Credit system
        if menu == "D":
            print("                                                                       ")
            cred = int(input("How Many Credits Would You Like To Deposit(20, 50, or 100)? "))
            cd = cd + cred
            print("Credits: ", cd)
            print("")
            #leaves system
        if menu == "E":
            print("")
            print("\033[1m===== Thank You For Playing =====\033[0m")
            print("Final Credits:", cd)
            break
        if menu == "T":
            print("Running 1,000-spin simulation...")
            total_spent = 0
            total_won = 0
            for i in range(1000):
                total_spent += 10
                roll = [random.choice(sy), random.choice(sy), random.choice(sy)]
                if roll[0] == roll[1] == roll[2]:
                    if roll[0] == "7":
                        total_won += 310
                    else:
                        total_won += 60
                net_profit = total_spent - total_won
            print("===== Simulation Results =====")
            print(f"Total Credits Spent: {total_spent}")
            print(f"Total Credits Won: {total_won}")
            print(f"Net Profit for Casino: {net_profit}")
            print("")

#Runs Program
spins()
