#Purpose: To help my user identity specific Division 1 NCAA teams based on a variety of different standards

#Init
import pandas as pd
data = pd.read_csv('D1.csv')
uni = data['University'].tolist()
team = data['Team nickname'].tolist()
city = data['City'].tolist()
state = data['State'].tolist()
enrollment = data['Enrollment'].tolist()
conf = data['Current conference'].tolist()
filtered = []

#Functions
def name(college): #User can search by school's name
    college = college.strip().upper()
    for i in range(len(uni)):
        if college in uni[i].upper():
            filtered.append(i)
    if len(filtered) == 0: #If nothing is found using the user's input
        print ("\033[1m No Data Found\033[0m")
    else:
        print(filtered) #Print Results
        print(data.loc[filtered])
    filtered.clear()
def mascot(character): #User can search by school's mascot/nickname
    for i in range(len(uni)):
        if character in team[i]:
            filtered.append(i)
    if len(filtered) == 0:
        print ("\033[1m No Data Found\033[0m")
    else: #If nothing is found using the user's input
        print(filtered) #Print Results
        print(data.loc[filtered])
    filtered.clear()
def location(place): #User can search by school's location, both the city or state
    for i in range(len(uni)):
        if place in city[i] or place in state[i]:
            filtered.append(i)
    if len(filtered) == 0: #If nothing is found using the user's input
        print ("\033[1m No Data Found\033[0m")
    else:
        print(filtered) #Print Results
        print(data.loc[filtered])
    filtered.clear()
def population(size): #User can find the school based on its size
    if size == "Tiny": #Tiny schools have less than 15000 enrolled
        for i in range(len(enrollment)):
            if enrollment[i] < 15000:
                filtered.append(i)
        print(filtered)
        print(data.loc[filtered]) #Print the schools that have a population matching the size
        filtered.clear()
    if size == "Small": #Small schools have between 15000 and 25000 enrolled
        for i in range(len(enrollment)):
            if 15000 <= enrollment[i] < 25000:
                filtered.append(i)
        print(filtered)
        print(data.loc[filtered]) #Print the schools that have a population matching the size
        filtered.clear()
    if size == "Medium": #Medium schools have between 25000 and 40000 enrolled
        for i in range(len(enrollment)):
            if 25000 <= enrollment[i] < 40000:
                filtered.append(i)
        print(filtered)
        print(data.loc[filtered]) #Print the schools that have a population matching the size
        filtered.clear()
    if size == "Large": #Large schools have more than 40000 enrolled
        for i in range(len(enrollment)):
            if 40000 <= enrollment[i]:
                filtered.append(i)
        print(filtered)
        print(data.loc[filtered]) #Print the schools that have a population matching the size
        filtered.clear()
def organize(conference): #User can find the schools that are in the same conference
    conference = conference.lower()
    for i in range(len(data)):
        if conference in conf[i].lower():
            filtered.append(i)
    if len(filtered) == 0: #If nothing is found using the user's input
        print ("\033[1m No Data Found\033[0m")
    else:
        print(filtered) #Print Results
        print(data.loc[filtered])
    filtered.clear()
def menu():
    print("Welcome To College Sports Locator, Where We Help Locate D1 NCAA Teams. Let's Get Started!")
    print("")
    while True:
        print("------------------------------------------------------------------------------------------------------------------")
        choice = input("Search By [N]ame, [M]ascot, [L]ocation, [S]ize, [C]onference, or [E]xit Program. Please Type The Letter: ").strip().lower()
        if choice == "n":
            print("")
            call = input("What's The Name Of The School? ").strip()
            print("")
            name(call)
            print("")
        elif choice == "m":
            print("")
            ask = input("What's The Mascot? ").title()
            print("")
            mascot(ask)
            print("")
        elif choice == "l":
            print("")
            where = input("Where Is The School? ").title()
            print("")
            location(where)
            print("")
        elif choice == "s":
            print("")
            students = input("How Big Is The School? ([T]iny, [S]mall, [M]edium, or [L]arge) Please Type The Letter: ").strip().lower()
            if students == "t":
                print("")
                population("Tiny")
                print("")
            if students == "s":
                print("")
                population("Small")
                print("")
            if students == "m":
                print("")
                population("Medium")
                print("")
            if students == "l":
                print("")
                population("Large")
                print("")
        elif choice == "c":
            print("")
            print("Conferences: ACC, American, Big 12, Big Ten, C-USA, FBS Independent, Independent, MAC, Mountain West, Pac-12, SEC, Sun Belt")
            print("")
            which = input("What Conference Is The School In? ").title()
            print("")
            organize(which)
            print("")
        elif choice == "e":
            break
        else:
            print("Sorry, Could Not Process ")
            print("")

#Main
menu()

#Sources
#NCAA Division 1 Teams Dataset
#Website Name: CFB Data Warehouse
#URL: https://docs.google.com/spreadsheets/d/1Ibwy8Nk--_1xKUVzDAeerNfwZc0Ya3rluul4I9Zcwao/edit?gid=0#gid=0
#Dataset Source: http://www.cfbdatawarehouse.com/index.php
#Dataset Shared By code.org
