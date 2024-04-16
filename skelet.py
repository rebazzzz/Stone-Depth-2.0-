#import
import random, time, combat

#variabel
skelet_hp = 100
player_hp = 120
pickaxe = 25
yxa = 30
magisktlubba = 35
arsenal = ["Pickaxe 🪓", "Yxa 🔨", "Magisktlubba 🍭✨"]

#funktion för spelare attack mot enemy
def spelare_attack():
    """Spelaren attackerar enemy genom att välja vapen i sin arsenal"""
    global skelet_hp    
    attack = input("Skriv 1 för Pickaxe, 2 för yxan och 3 för den magiska klubban:\n")

    if attack == "1":
        skelet_hp -= pickaxe
        if skelet_hp <= 0:
            print(f"Skelettet är död!")
        else:
            print(f"⚔️ 🦴 💥: Skelettet har nu {skelet_hp} hp efter din attack.")
    elif attack == "2":
        skelet_hp -= yxa
        if skelet_hp <= 0:
            print(f"Skelettet är död:")
        else:
            print(f"⚔️ 🦴 💥💥: Skelettet har nu {skelet_hp} hp efter din attack.")
    elif attack == "3":
        skelet_hp -= magisktlubba
        if skelet_hp <= 0:
            print(f"Skelettet är död!")
        else:
            print(f"⚔️ 🦴 💥💥💥: Skelettet har nu {skelet_hp} hp efter din attack.")
            #⚔️🦴💥
    else:
        combat.fel_combat_input()

#funktion för enemy attack mot spelaren
def skelet_attack():
    """Enemy attackerar spelaren med random damage"""
    global player_hp
    damage = random.randint(20, 30)
    player_hp -= damage
    if player_hp < 0:
        print(f"Du har nu 0 hp efter skelettets attack.")
    else:
        print(f"⚔️ 💥💥💥: Du har nu {player_hp} hp efter skelettets attack.")

#spelguide innan man börjar spela
def combat_guide():
    print (f"Du har dessa vapen i din arsenal: {arsenal}.")
    time.sleep(2)
    print(f"Din pickaxe gör 25 damage, yxan gör 30 och den magiska klubban gör 35!")
    time.sleep(2)
    print(f"Vilket vapen vill du attackera skelettet med?")
    time.sleep(2)

#loop för combat mellan spelaren och enemy tils en dör
def skelet_combatloop():
    """Loop för combat mellan spelaren och enemy"""
    while player_hp > 0 or skelet_hp > 0:
        spelare_attack()
        time.sleep(0.5)
        if skelet_hp <= 0:
            print("Raslande benen faller och en nyckel ligger på marken!")
            break

        skelet_attack()
        time.sleep(0.5)
        if player_hp <= 0:
            print("GAME OVER")
            break

