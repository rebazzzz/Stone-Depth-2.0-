#import
import random, time, combat

#variabel
boss_hp = 135
player_hp = 125
pickaxe = 25
yxa = 30
magisktlubba = 35
arsenal = ["Pickaxe 🪓", "Yxa 🔨", "Magisktlubba 🍭✨"]

#funktion för spelare attack mot enemy
def spelare_attack():
    """Spelaren attackerar enemy genom att välja vapen i sin arsenal"""
    global boss_hp 
    attack = input("Skriv 1 för Pickaxe, 2 för yxan och 3 för den magiska klubban:\n")

    if attack == "1":
        boss_hp -= pickaxe
        if boss_hp <= 0:
            print(f"Bossen är död!")
        else:
            print(f"⚔️ 🗿 💥: Bossen har nu {boss_hp} hp efter din attack.")
    elif attack == "2":
        boss_hp -= yxa
        if boss_hp <= 0:
            print(f"Bossen är död:")
        else:
            print(f"⚔️ 🗿 💥💥: Bossen har nu {boss_hp} hp efter din attack.")
    elif attack == "3":
        boss_hp -= magisktlubba
        if boss_hp <= 0:
            print(f"Bossen är död!")
        else:
            print(f"⚔️ 🗿 💥💥💥: Bossen har nu {boss_hp} hp efter din attack.")
            #⚔️🦴💥
    else:
        combat.fel_combat_input()

#funktion för enemy attack mot spelaren
def boss_attack():
    """Enemy attackerar spelaren med random damage"""
    global player_hp
    damage = random.randint(20, 35)
    player_hp -= damage
    if player_hp < 0:
        print(f"Du har nu 0 hp efter Bossens attack.")
    else:
        print(f"⚔️ 🗿💥💥💥: Du har nu {player_hp} hp efter Bossens attack.")

#spelguide innan man börjar spela
def combat_guide():
    print (f"Du har dessa vapen i din arsenal: {arsenal}.")
    time.sleep(2)
    print(f"Din pickaxe gör 25 damage, yxan gör 30 och den magiska klubban gör 35!")
    time.sleep(2)
    print(f"Vilket vapen vill du attackera Bossen med?")
    time.sleep(2)

#loop för combat mellan spelaren och enemy tils en dör
def boss_combatloop():
    """Loop för combat mellan spelaren och enemy"""
    while player_hp > 0 or boss_hp > 0:
        spelare_attack()
        time.sleep(0.5)
        if boss_hp <= 0:
            print("Stenar faller från stenjätten och dör!")
            break

        boss_attack()
        time.sleep(0.5)
        if player_hp <= 0:
            print("GAME OVER")
            break