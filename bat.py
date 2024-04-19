import time, os

enemy_hp = 90
player_hp = 100
pickaxe_dmg = 25
yxa_dmg = 35
magisktlubba_dmg = 50
magisktlubba_uses = 0

vapen = {
    "Pickaxe 🪓": {"dmg": 25},
    "Yxa 🔨": {"dmg": 35},
    "Magisktlubba 🍭✨": {"dmg": 55}
}

inventory = list(vapen.keys())

def spelare_HP():
    Hp = player_hp // 10
    symbol = "❤️ " * Hp
    print(f"""Din HP:{symbol}""")
    time.sleep(1)
    print("""Du känner smärtan bränna genom din kropp varje gång fladdermusen biter dig.
          """)


def enemy_attack():
    global player_hp
    damage = 25
    player_hp -= damage
    if player_hp < 0:
        print(f"Du dog 💀")
    else:
        spelare_HP()

def bat_HP():
    bat_hp = enemy_hp // 5
    bat_symbol = "🦇 " * bat_hp
    print(f"""Fladermusens HP:{bat_symbol}""")

def fel_combat_input():
    print("Du tar fortfarande skada om du skriver fel input! Skriv 1, 2 eller 3")

def spelare_attack():
    global enemy_hp   
    global magisktlubba_uses 
    global vapen
    attack = int(input("Ange siffran till vapnet du vill attackera fladdermusen med:"))

    if attack == 1:
        enemy_hp -= pickaxe_dmg

        if enemy_hp < 0:
            pass
        else:
            bat_HP()
            print("""Du hör ett skrik från fladdermusen när din pickaxe träffar den.
                  """)
            

    elif attack == 2:
        enemy_hp -= yxa_dmg

        if enemy_hp < 0:
            pass
        else:
            bat_HP()
            print("""Din yxa biter djupt in i fladdermusens vinge, vilket gör ett hål i den.
                  """)
            

    elif attack == 3 and magisktlubba_uses < 1:
         enemy_hp -= magisktlubba_dmg
         magisktlubba_uses += 1
         print("""Din magiska klubba gör väldigt mycket skada 😉, men fladdermusen fångar och slänger iväg din magiska klubba efter din attack!""")
    
         if enemy_hp <= 0:
            pass
         
         else:
             bat_HP()

    elif attack == 3 and magisktlubba_uses == 1:
        print("""Fladdermusen slängde iväg din magiska klubba, så du kan inte använda den för tillfället.
              """)
          
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
    while player_hp > 0 or enemy_hp > 0:
        spelare_attack()
        time.sleep(0.5)
        if enemy_hp <= 0:
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
        time.sleep(0.5)
        if player_hp <= 0:
            print("GAME OVER")
            break

def forsta_enemy():
    combatguide()
    combatloop()

