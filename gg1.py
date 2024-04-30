from bat import enemy_hp, magisktlubba_uses, pickaxe_dmg, bat_HP, yxa_dmg, magisktlubba_dmg, fel_combat_input
def spelare_attack(weapon_choice):
    global enemy_hp
    global magisktlubba_uses
    
    if weapon_choice == 1:
        enemy_hp -= pickaxe_dmg
        if enemy_hp < 0:
            pass
        else:
            bat_HP()
            print("""Du hör ett skrik från fladdermusen när din pickaxe träffar den.""")
            
    elif weapon_choice == 2:
        enemy_hp -= yxa_dmg
        if enemy_hp < 0:
            pass
        else:
            bat_HP()
            print("""Din yxa biter djupt in i fladdermusens vinge, vilket gör ett hål i den.""")
            
    elif weapon_choice == 3 and magisktlubba_uses < 1:
        enemy_hp -= magisktlubba_dmg
        magisktlubba_uses += 1
        print("""Din magiska klubba gör väldigt mycket skada 😉, men fladdermusen fångar och slänger iväg din magiska klubba efter din attack!""")
        
        if enemy_hp <= 0:
            pass
        else:
            bat_HP()
            
    elif weapon_choice == 3 and magisktlubba_uses == 1:
        print("""Fladdermusen slängde iväg din magiska klubba, så du kan inte använda den för tillfället.""")
          
    else:
        print("""Använd rätt vapen!""")
        fel_combat_input()
