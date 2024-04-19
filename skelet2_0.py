import time

enemy_hp = 100
player_hp = 160
pickaxe_dmg = 25
gyllene_yxa = 45
magisktlubba_dmg = 50
magisktlubba_uses = 1

vapen = {
    "Pickaxe 🪓": {"dmg": 25},
    "Gyllene Yxa 🔨🧈": {"dmg": 45},
    "Magisktlubba 🍭✨": {"dmg": 50}
}

inventory = list(vapen.keys())

def spelare_HP():
    Hp = player_hp // 10
    symbol = "❤️ " * Hp
    print(f"""Din HP:{symbol}""")
    time.sleep(1)
    print("""Du känner smärtan bränna när skelettet attackerar dig med sina karga klor, dess anfall är lika iskallt som dödens omfamning.
          """)


def enemy_attack():
    global player_hp
    damage = 40
    player_hp -= damage
    if player_hp < 0:
        print(f"Du dog 💀")
    else:
        spelare_HP()

def skelet_HP():
    skelet_hp = enemy_hp // 5
    skelet_symbol = "☠️ " * skelet_hp
    print(f"""Skelettets HP:{skelet_symbol}""")

def fel_combat_input():
    print("Du tar fortfarande skada om du skriver fel input! Skriv 1, 2 eller 3")

def spelare_attack():
    global enemy_hp   
    global magisktlubba_uses 
    global vapen
    attack = int(input("Ange siffran till vapnet du vill attackera skelettet med:"))

    if attack == 1:
        enemy_hp -= pickaxe_dmg

        if enemy_hp < 0:
            pass
        else:
            skelet_HP()
            print("""Skelettet skakas när din pickaxe träffar dess kropp, benen raslar och det låter ut ett dött skrik.
                  """)
            

    elif attack == 2:
        enemy_hp -= gyllene_yxa

        if enemy_hp < 0:
            pass
        else:
            skelet_HP()
            print("""Skelettet viker sig under din attack, dess ben darrar och dess attacker blir svagare när det kämpar för att stå kvar.
                  """)
            

    #elif attack == 3 and magisktlubba_uses < 1:
        # enemy_hp -= magisktlubba_dmg
        # magisktlubba_uses += 1
        # print("""Din magiska klubba gör väldigt mycket skada 😉, men fladdermusen fångar och slänger iväg din magiska klubba efter din attack!""")
    
        # if enemy_hp <= 0:
        #    pass
         
        # else:
            # skelet_HP()

    elif attack == 3 and magisktlubba_uses == 1:
        print("""Din magiska klubba svingas mot skelettet 😉, men dess kraft verkar inte ha någon effekt på den köttlösa fienden 😉😲.
              """)
          
    else:
        print("""Använd rätt vapen!""")
        fel_combat_input()


def skelet():
    print(""" 
          Vem vågar utmana mig?""")

    time.sleep(2)
    print("""
          Du hör en mörk röst eka genom korridoren när skelettet träd fram ur skuggorna.""")

    time.sleep(3)
    print("""
          Du känner en iskall vind svepa förbi när skelettet närmare sig.""")
    
    time.sleep(5)
    print("""
                               _.--""-._
   .                         ."         ".
  / \    ,^.         /(     Y             |      )1
 /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
 |        :|    `>   '.     l_..-------.._l      .'
 |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
  \  .-' | |  `              l._       _.'
   \/    | |                   l`^^'^^'j
         | |                _   \_____/     _
         j |               l `--__)-'(__.--' |
         | |               | /`---``-----'"1 |  ,-----.
         | |               )/  `--' '---'   \'-'  ___  `-.
         | |              //  `-'  '`----'  /  ,-'   I`.  1
       _ L |_            //  `-.-.'`-----' /  /  |   |  `. 1
      '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
       `._;l _'--------_/        )-'/     :  |___.    _._./ ;
         | |                 .__ )-'\  __  \  \  I   1   / /
         `-'                /   `-\-(-'   \ \  `.|   | ,' /
                            \__  `-'    __/  `-. `---'',-'
                               )-._.-- (        `-----'
                              )(  l\ o ('..-.
                        _..--' _'-' '--'.-. |
                 __,,-'' _,,-''            \ 1
                f'. _,,-'                   \ 1
               ()--  |                       \ 1
                 \.  |                       /  1
                   \ \                      |._  |
                    \ \                     |  ()|
                     \ \                     \  /
                      ) `-.                   | |
                     // .__)                  | |
                 _ ./ /7'                      | |
                '---'                         j_| `
                                             (| |
                                              |  1
                                              |lllj
                                      """)
    

def combatguide():
   global vapen
   time.sleep(2)
   print("Inventory:")
   for i, weapon in enumerate(inventory, 1):
      print(f"{i}. {weapon}, Skada: {vapen[weapon]['dmg']}")
      time.sleep(1)
    

def combatloop():
    global magisktlubba_uses
    while player_hp > 0 or enemy_hp > 0:
        spelare_attack()
        time.sleep(0.5)
        if enemy_hp <= 0:
            print("Med en sista dödsryckning faller skelettet till marken, dess ben sprids och dess skratt tystnar för evigt.")
            time.sleep(1.5)
            print("Din magiska klubba börjar fungera igen när du ser skelettet på marken 😉.")
            magisktlubba_uses = 0
            time.sleep(2)
            print("En skugga av allvar sveper över dig när du inser att det inte längre finns utrymme för misstag...")
            break

        enemy_attack()
        time.sleep(0.5)
        if player_hp <= 0:
            print("GAME OVER")
            break

def andra_enemy():
    combatguide()
    combatloop()

