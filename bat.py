import time
import os

enemy_hp = 90
player_hp = 100
pickaxe_dmg = 25
yxa_dmg = 35
magisktlubba_dmg = 50
magisktlubba_uses = 0
bat_alive = True
vapen = {
    "Pickaxe 🪓": {"dmg": 25},
    "Yxa 🔨": {"dmg": 35},
    "Magisktlubba 🍭✨": {"dmg": 50}
}
inventory = list(vapen.keys())

def spelare_HP():
    global player_hp
    Hp = player_hp // 10
    symbol = "❤️ " * Hp
    print(f"""Din HP:{symbol}""")
    time.sleep(1)
    print("""Du känner smärtan bränna genom din kropp varje gång fladdermusen biter dig.""")

def enemy_attack():
    global player_hp
    damage = 20
    player_hp -= damage
    if player_hp <= 0:
        print(f"Du dog 💀")
        player_hp = 0
    else:
        spelare_HP()

def bat_HP():
    global enemy_hp
    bat_hp = enemy_hp // 5
    bat_symbol = "🦇 " * bat_hp
    print(f"""Fladermusens HP:{bat_symbol}""")

def fel_combat_input():
    print("Du tar fortfarande skada om du skriver fel input! Skriv 1, 2 eller 3")

def spelare_attack(val):
    global enemy_hp
    global magisktlubba_uses
    if val == 1:
        enemy_hp -= pickaxe_dmg
        if enemy_hp <= 0:
            enemy_hp = 0
        bat_HP()
        print("""Du hör ett skrik från fladdermusen när din pickaxe träffar den.""")
    elif val == 2:
        enemy_hp -= yxa_dmg
        if enemy_hp <= 0:
            enemy_hp = 0
        bat_HP()
        print("""Din yxa biter djupt in i fladdermusens vinge, vilket gör ett hål i den.""")
    elif val == 3 and magisktlubba_uses < 1:
        enemy_hp -= magisktlubba_dmg
        magisktlubba_uses += 1
        print("""Din magiska klubba gör väldigt mycket skada 😉, men fladdermusen fångar och slänger iväg din magiska klubba efter din attack!""")
        if enemy_hp <= 0:
            enemy_hp = 0
        bat_HP()
    elif val == 3 and magisktlubba_uses == 1:
        print("""Fladdermusen slängde iväg din magiska klubba, så du kan inte använda den för tillfället.""")
    else:
        print("""Använd rätt vapen!""")
        fel_combat_input()

def bat():
    print(""" 
          Screeeee!""")
    time.sleep(2)
    print("""
          Du hör ett svagt susande ljud i fjärran, som om något mörkt närmar sig.""")
    time.sleep(3)
    print("""
          Ditt hjärta börjar bulta när du hör svaga vingslag nära dig. Striden är nära, och du står redo att möta din fiende.""")
    time.sleep(1)
    print("""
                  Screeeee!""")
    time.sleep(5)
    print("""
                                     =***-           +*+=-        
                                   =###*-            +*#***+-         
                                -****###*-           +###****+                          
                               =**######*-           +####*****                          
                              -**########-           +#####****+                            
                       ==++-..=*#########*************######****        -++==             
                  =****#***+..=#######**************##########**        +***#****=           
               -***###*****=..=######**************#######*###*-        =*#***###***-      
             =**###*****##*+..=########*********#########**###**        +*###**##*###*=  
           =*###******##*##*=.+######***################*######*       =****##******###*=     
           *####******##***##*+*#*###**############*+############      +******##*******###+        
            ##********##****####*--+*############+---*###############**********#********###*        
       -####********##*****####*-:.:-+#######+-:..:-*#############************##*********###-       
      -####********#******######=....:-==**=::.....=###########***************###*********###-      
      *###*********#******########=::----=+#=::::=#############***************##**********###*  
     =###**********#*******#######*+=*+=#+=+*###################**************##***********###=  
     ##************#********######+-+#+=**==+###################**************###***********###  
    =#*****####***********########*+=--===++*#############################****##*****####***###=    
    ##**##*=---+#####***##=.    -*#*::+**::+#################*           =##***#####+    *######   
    ####=.      .:*##*##=.      .-*#***#*+*#################*              =#####*         =####  
    ###-         ..*###:         ..+#######################-                 ####           -###  
    ##*            -##=              =###################-                   =##-            *##
                                       =*##########*+-               
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
    global enemy_hp
    global player_hp
    while player_hp > 0 and enemy_hp > 0:
        print("Ange siffran för ditt vapenval: 1, 2 eller 3")
        try:
            val = int(input())
            if val not in [1, 2, 3]:
                raise ValueError
            spelare_attack(val)
        except ValueError:
            fel_combat_input()
        
        if enemy_hp <= 0:
            bat_alive = False
            print("Ett dött tystnad faller över när fladdermusen kollapsar till marken.")
            time.sleep(1.5)
            print("Du springer och plockar upp din magiska klubba.")
            magisktlubba_uses = 0
            time.sleep(2)
            print("Du känner en våg av lättnad skölja över dig när fladdermusen har äntligen besegrats och du har fått tillbaka din magiska klubba 😉.")
            print("Du går djupare in i grottan...")
            time.sleep(12)
            os.system("cls" if os.name == "nt" else "clear")
            print("... Plötsligt rasar ingången bakom dig. Det finns inget återvändande nu!")
            break

        enemy_attack()
        if player_hp <= 0:
            print("GAME OVER")
            break

def forsta_enemy():
    combatguide()
    combatloop()
