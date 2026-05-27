#Images
#Tutorial On How To Open Images Using Python
#2/24/26

#Initialize
import webbrowser

url = ["https://tinyurl.com/2k2nk36y",#Dachshund
       "https://tinyurl.com/48u2j5du" #French Bulldog
       "https://tinyurl.com/2s36zkpe" #Corgi
       "https://tinyurl.com/9etj3azp" #Golden Retriever
       ]

description = ["A Dachshund is a small, long‑bodied dog with short legs and a bold, curious personality. They’re affectionate, love to explore, and often act much bigger than they look.",
               "A French Bulldog is a small, muscular little dog with a sweet temper. They’re affectionate and love attention.They often thrive in cozy environments."
               "A Corgi is a small herding dog with a long body, short legs, and a cheerful personality. They’re very energetic, affectionate, and love the attention."
               "A Golden Retriever is a large friendly dog known for its intelligence and happyness. They’re often very loyal and patient. They thrive on affection and love being part of their owner's lives."
               ]


#Functions
def dog_breed():
    print("Welcome, Let's Help You Find Your Perfect Dog Match!")
    speed = input("Which do you prefer(Fast or Slow)? ")
    if speed == "Fast":
        like = input("What do you like more (Smaller or Bigger)? ")
        if like == "Smaller":
                webbrowser.open(url[0])
                print(description[0])
        else:
            webbrowser.open(url[2])
            print(description[2])


    if speed == "Slow":
        perfer = input("What do you like more (Fast or Slow)? ")
        if perfer == "Fast":
                webbrowser.open(url[3])
                print(description[3])
        else:
            webbrowser.open(url[1])
            print(description[1])



#Main
dog_breed()

#Sources of Information

#Picture of Dachshund
#Website Name: The New York Times
#URL: https://www.nytimes.com/2024/03/28/world/europe/dachshund-dog-breeding-ban-germany.html
#Author Name: Derrick Bryson Taylor
#Article Name: Germany’s Beloved Dachshund Could Be Threatened Under Breeding Bill
#Date: March 28, 2024

#Picture of French Bulldog
#Website Name: Pet MD
#URL: https://www.petmd.com/dog/breeds/french-bulldog
#Author Name: Melissa Boldan, DVM
#Article Name: French Bulldog
#Date: Mar. 13, 2023

#Picture of Corgi
#Website Name: Boston Herald
#URL: https://www.bostonherald.com/2025/08/24/little-legs-big-dreams-more-than-100-teams-compete-in-lithuanias-international-corgi-race/
#Author Name: Associated Press
#Article Name: Little legs, big dreams: More than 100 teams compete in Lithuania’s international Corgi race
#Date: August 24, 2025 at 5:51 AM

#Picture of Golden Retriever
#Website Name: The New York Times
#URL: https://www.nytimes.com/2023/07/19/travel/scotland-golden-retrievers.html
#Author Name: Judith Newman
#Article Name: Why Did 488 Golden Retrievers Gather in Scotland?
#Date: July 19, 2023
