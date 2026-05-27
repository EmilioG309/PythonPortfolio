# Initial Conditions
import random
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake

# The Simulation Loop
while tortoise_pos < finish_line and hare_pos < finish_line:
    # Tortoise always moves a short distance between 1 - 3 meters at random
    tortoise_move = random.randint(1,3)
    tortoise_pos = tortoise_pos + tortoise_move
    # Hare has a 30% chance of falling a sleep for a turn
    asleep_chance = random.randint(1,100)
    if asleep_chance <= 30:
        is_hare_asleep = True
        print("Hare Is Asleep")
    else:
        is_hare_asleep = False
    # If Hare is awake, it will move 1 - 10 meters at random
    if is_hare_asleep == False:
        hare_move = random.randint(1,10)
        hare_pos = hare_move + hare_pos
    # Print the positions of the Hare and Tortoise after each round
    print(f"Tortoise: {tortoise_pos} | Hare: {hare_pos}")

    # Determine the winner
if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins!")
else:
    print("🐇 The Hare wins!")
