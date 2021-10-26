import random


def prompt_user_before_fight():
    name_user = input("Hello Warrior. Please enter your name :")
    print("Why hello there, " + name_user)
    ready_to_fight = input("Are you ready to fight, " + name_user + "? Yes/No")

    if (ready_to_fight == "Yes") or (ready_to_fight == "yes"):
        print("Let's do this !")
    elif (ready_to_fight == "No") or (ready_to_fight == "no"):
        print("Maybe next time...")
    else:
        print("Uhm...What ?")
        prompt_user_before_fight()


def explain_rules():
    print("A huge troll just popped out of no where ! You have to beat him as soon as possible or he'll probably end "
          "up killing you :(")
    print("You have two choices. You can either hit the troll with your sword or drink a potion")
    print("Beware though ! You only have 3 potions in your bag. One potion restores 15 lifepoints so use them wisely")


def game_over():
    print("Oh no ! Your health points have reached 0. You are dead")
    print("GAME OVER!")
    try_again = input("Would you like to try again ? Yes/No")
    if (try_again == "Yes") or (try_again == "yes"):
        print("Let's do this !")
    elif (try_again == "No") or (try_again == "no"):
        print("Maybe next time...")
    else:
        print("Uhm...What ?")
        prompt_user_before_fight()


def yay():
    print("Yay ! You beat the troll and won ! ")
    other_fight = input("Would you like to go for another fight ? Yes/No")
    if (other_fight == "Yes") or (other_fight == "yes"):
        print("Let's do this !")
        print("Run this script again to go for another fight :) ")
    elif (other_fight == "No") or (other_fight == "no"):
        print("Maybe next time...")
    else:
        print("Uhm...What ?")
        prompt_user_before_fight()


def fight():
    life_user = 50
    life_foe = 50
    user_potions = 3
    skip_turn = False

    while True:
        # User turn
        if skip_turn:
            print("You skip your turn")
            skip_turn = False
        else:
            user_action = ""
            while user_action not in ["1", "2"]:
                user_action = input("Would you like to attack (1) or drink a potion (2) ?")

            if user_action == "1":
                player_damage = random.randint(1, 15)
                life_foe -= player_damage
                print("You've inflicted {} points of damage to foe".format(player_damage))
            elif user_action == "2" and user_potions > 0:
                potion_health = random.randint(15, 30)
                life_user += potion_health
                user_potions -= 1
                # User skips turn when they use a potion
                skip_turn = True
                print("You've recovered {} health points".format(potion_health))
            else:
                print("You don't have any potions left...")
                continue

        if life_foe <= 0:
            yay()
            break

        # Foe attack
        foe_attack = random.randint(0, 15)
        life_user -= foe_attack
        print("Foe has inflicted you {} points of damage".format(foe_attack))
        print("-" * 100)

        if life_user <= 0:
            game_over()
            break

        print("You have {} health points left".format(life_user))
        print("That big troll has {} health points left".format(life_foe))
        print("-" * 100)
        print("End of turn")


def main():
    prompt_user_before_fight()
    explain_rules()
    fight()


if __name__ == "__main__":
    main()