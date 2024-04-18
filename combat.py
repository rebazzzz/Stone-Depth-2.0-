#import
import random, time

#variabel
enemy_hp = 60
player_hp = 120
pickaxe_dmg = 25
yxa_dmg = 40
magisktlubba_dmg = 50

vapen = {
    "Pickaxe 🪓": {"dmg": 25},
    "Yxa 🔨": {"dmg": 40},
    "Magisktlubba 🍭✨": {"dmg": 50}
}

inventory = list(vapen.keys())

# Meddelande när spelaren skriver fel input
def fel_combat_input():
    print("Du tar fortfarande skada om du skriver fel input! Du kan bara skriva 1, 2 eller 3")

#funktion för enemy attack mot spelaren
def enemy_attack():
    """Enemy attackerar spelaren med random damage"""
    global player_hp
    damage = random.randint(20, 30)
    player_hp -= damage
    if player_hp < 0:
        print(f"Du dog 💀")
    else:
        print(f"❤: {player_hp}")

#funktion för spelare attack mot enemy
def spelare_attack():
    """Spelaren attackerar enemy genom att välja vapen i sin arsenal"""
    global enemy_hp    
    attack = int(input("Ange siffran till vapnet du vill attackera med:\n"))

    if attack == 1:
        enemy_hp -= pickaxe_dmg

        if enemy_hp < 0:
            print(f"Enemy är död!")
        else:
            print("💔")
            print(f"Enemy HP: {enemy_hp}")

    elif attack == 2:
        enemy_hp -= yxa_dmg

        if enemy_hp < 0:
            print(f"Enemy är död!")
        else:
            print("💔")
            print(f"Enemy HP: {enemy_hp}")

    elif attack == 3 and magisktlubba_cd == 1:
        enemy_hp -= magisktlubba_dmg
        magisktlubba_cd = magisktlubba_cd + 1

        if enemy_hp < 0:
            print(f"Enemy är död!")
        else:
            print("💔")
            print(f"Enemy HP: {enemy_hp}")
            #⚔️🦴💥
    else:
        print("Använd rätt vapen!")


#spelguide innan man börjar spela
def combatguide():
   print("Din arsenal:")
   for i, weapon in enumerate(inventory, 1):
      print(f"{i}. {weapon}, Skada: {vapen[weapon]['dmg']}")
      time.sleep(1)
    #print(f"Din pickaxe gör 25 damage, yxan gör 30 och den magiska klubban gör 35!")
    #time.sleep(2)
    
#loop för combat mellan spelaren och enemy tils en dör
def combatloop():
    """Loop för combat mellan spelaren och enemy"""
    while player_hp > 0 or enemy_hp > 0:
        spelare_attack()
        time.sleep(0.5)
        if enemy_hp <= 0:
            print("Raslande benen faller och en nyckel ligger på marken.")
            break

        enemy_attack()
        time.sleep(0.5)
        if player_hp <= 0:
            print("GAME OVER")     
            break

combatguide()
combatloop()