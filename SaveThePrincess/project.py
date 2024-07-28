import random

class Player:
    def __init__(self,name):
        self.name = name
        self.items = {
            "Rusty Sword":5, #Max 15
            "Diamond Sword":25, #Max 75
            "Spear":15, #Max 45
            "Hammer":20 #Max 60
        }
        self.enemies = {
            "Dragon":75,
            "Sorcerer":50,
            "Goblin":25
        }

    def choose_item(self):
        item = random.choice(list(self.items))
        return item

    def choose_enemy(self):
        enemy = random.choice(list(self.enemies))
        return enemy

    # Fight function
    def fight(self,player_item, player_enemy):
        enemy_hp = self.enemies[player_enemy]
        player_hp = self.items[player_item]
        #turn 1
        print(f"\nYou strike the {player_enemy} with the {player_item}.")
        enemy_hp -= player_hp
        if enemy_hp > 0:
            #turn 2
            print(f"\nThe {player_enemy} is strong! However you are quick and attack them again.")
            enemy_hp -= player_hp
            if enemy_hp > 0:
                #turn 3
                print(f"\nHurry {self.name}, the {player_enemy} is weakened! You hit them one last time.")
                enemy_hp -= player_hp
                if enemy_hp > 0:
                    print(f"\nThe {player_enemy} has had enough!")
                    print(f"It attacks you with a blow to the head.")
                    print(f"{self.name}, you have died.  Poor princess.")
                    return
                else:
                    print(f"\nYou did it, {self.name}!  You defeated the {player_enemy}!")
                    print(f"You run over to the princess and quickly untie her.")
                    print(f"You saved the princess!!")
            else:
                print(f"\nYou did it, {self.name}!  You defeated the {player_enemy}!")
                print(f"You run over to the princess and quickly untie her.")
                print(f"You saved the princess!!")
        else:
            print(f"\nYou did it, {self.name}!  You defeated the {player_enemy}!")
            print(f"You run over to the princess and quickly untie her.")
            print(f"You saved the princess!!")

def line_break():
    print("------------------------------")


def game():
    while True:
        # Introduction
        print("\nSave the Princess!")
        print("\nThe princess is being held hostage.  Enter the castle and try to save her.")
        print("Make the correct choices, defeat the enemy and save the princess!")
        hero = Player(input("What is your name, hero? "))
        line_break()
        print(f"\n{hero.name}, you walk up to the large castle. You hear the princess scream!")
        print("You can either enter the castle quietly through the dungeon or boldly through the castle doors.")
        print("1: Dungeon")
        print("2: Castle Doors")
        entrance = input("Which way do you choose (Enter 1 or 2)? ")

        # Dungeon
        if entrance == "1":
            line_break()
            print("\nYou sneak in through the dungeon. Its dark with a few torches along the wall.")
            print("You grab a torch and head deeper inside.  There's a room to the left and a narrow hallway on the right.")
            while True:
                print(f"{hero.name}, which way should you go?")
                print("1: Left into the room")
                print("2: Right down the narrow hallway")
                first_dungeon = input("Left or right (Enter 1 or 2)? ")
                if first_dungeon == "2":
                    line_break()
                    print("\nYou make a right and head down the narrow hallway.")
                    print("It is getting tighter and tighter!")
                    print(f"You walk right into the wall!  I think you hit a dead end, {hero.name}.  Turn around to go back!")
                else:
                    line_break()
                    print("\nYou turn left into the room.  It is dimly lit, but notice something in the center of the room.")
                    print("Its a treasure chest!")
                    player_item = hero.choose_item()
                    print(f"\n{hero.name} has been awarded the {player_item.upper()}")
                    print("This might be useful!")
                    print("\nAaaaaahhhhhh!!!!")
                    print("That must be the princess. Keep going to save her.")
                    print("The room has two identical doors. Which one do you want to walk through?")
                    door = input("First Door or Second Door (Enter 1 or 2)? ")
                    if door == "1":
                        line_break()
                        print("\nYou step through the door and you feel the ground collapse beneath your feet!")
                        print(f"Oh no {hero.name}!  You have fallen into a pit!!")
                        print("It looks like your adventure is over. Poor princess.")
                    else:
                        line_break()
                        print("\nYou step through the door into an open room. You see the princess tied up in the corner.")
                        player_enemy = hero.choose_enemy()
                        print(f"Before you can run to her, a {player_enemy.upper()} jumps in your path.")
                        print(f"Draw your {player_item}, {hero.name}.  You must defeat the {player_enemy} to save the princess!")
                        hero.fight(player_item, player_enemy)
                    break
        #Castle Doors
        if entrance == "2":
            line_break()
            print("\nYou bravely burst open the castle doors. To your surprise, no one is there to meet you.")
            print("You hear the princess yell. Where is she?")
            print("To the left, is a room but you cannot see inside it.  On the right, is a hallway lined with armored suits.")
            while True:
                print(f"{hero.name}, which way should you go?")
                print("1: Left into the room")
                print("2: Right down the hallway")
                first_dungeon = input("Left or right (Enter 1 or 2)? ")
                if first_dungeon == "2":
                    line_break()
                    print("\nYou make a right and head down the hallway.")
                    print("The armored suits begin to move!")
                    print(f"You remove the helmet from one of the moving suits.  The suit is empty!  You are not dealing with ghosts, turn around to go back {hero.name}!")
                else:
                    line_break()
                    print("\nYou turn left into the room.  Its a large room with marble floors.  You notice something on a pillar in the center of the room.")
                    print("Its a treasure chest!")
                    player_item = hero.choose_item()
                    print(f"\n{hero.name} has been awarded the {player_item.upper()}")
                    print("This might be useful!")
                    print("\nAaaaaahhhhhh!!!!")
                    print("That must be the princess. Keep going to save her.")
                    print("The room has two identical doors. Which one do you want to walk through?")
                    door = input("First Door or Second Door (Enter 1 or 2)? ")
                    if door == "1":
                        line_break()
                        print("\nYou step through the door.  Suddenly a large pendulum with spikes swings at your side!")
                        print(f"Oh no {hero.name}!  You have been fatally struck.")
                        print("It looks like your adventure is over. Poor princess.")
                    else:
                        line_break()
                        print("\nYou step through the door into an open room. You see the princess tied up in the corner.")
                        player_enemy = hero.choose_enemy()
                        print(f"Before you can run to her, a {player_enemy.upper()} jumps in your path.")
                        print(f"Draw your {player_item}, {hero.name}.  You must defeat the {player_enemy} to save the princess!")
                        hero.fight(player_item, player_enemy)   
                    break
        again = input("\nPlay Again? (Enter 1 for Yes or 2 for No)? ")
        if again == "1":
            continue
        else:
            return print("Goodbye!")
    
game()