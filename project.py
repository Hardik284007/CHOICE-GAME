print("Welcome To The Choice Game!")
name = input("What is your name? ")
print("How old are you, " + name + "?")
age = input()
health = 10

if int(age) < 18:
    print("Sorry, you are not old enough to play this game.")

else:
    print("Great! You are old enough to play the game.")
    print("Let's play!")
    print("You are starting with " + str(health) + " health.")

    print("Where you want to go? left/right")
    direction = input().strip().lower()

    if direction == "left":
        print("You fall of a cliff and died! Game Over!")
        health -= 10

    elif direction == "right":
        print("You came across a pond. Do you want to swim across or go around? (swim/around)")
        swim = input().strip().lower()

        if swim == "swim":
            print("You were bit by a snake and lost 5 health.")
            health -= 5
            print("You went through the pond and found a house. You knocked the door and a man welcomed you with a RPG & trying to escape from him you died. Game Over!")
            health -= 5

        elif swim == "around":
            print("You went around the pond and found a house. You knocked the door and a man welcomed you with a RPG & trying to escape from him you lost 5 health.")
            health -= 5

            print("You found a mysterious mushroom at the entrance of a jungle. Do you want to eat it? (yes/no)")
            eat = input().strip().lower()

            if eat == "yes":
                print("You ate the mushroom and gained 5 health. You entered the jungle, but a wild animal attacked you and you lost 5 health but you managed to escape and found your way back home. You won the game!")
                health += 5
                print("Your final health is: " + str(health))

            elif eat == "no":
                print("You didn't eat the mushroom. You entered the jungle, but a wild animal attacked you and you died. Game Over!")

        else:
            print("Invalid choice! You stood there confused and a wild animal attacked you. Game Over!")

    else:
        print("Invalid choice! You stood there confused and a wild animal attacked you. Game Over!")