import Dialoger, time, skelet, lavaskelet, boss, maps

place = 0
horizont = None
key1 = False
key2 = False
item_room = False
item = False
wiseman_room = False
enemy1_room = False
enemy2_room = False
riddle_room = False

death = False
win = False

def event():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    if place == 2 and horizont == "right" and item_room == False:
        Dialoger.loreinfo()
    elif place == 2 and horizont == "right" and item_room == True:
        print("Du har redan varit här och öpppnat kistan\n")

    elif place == 3 and horizont == "right" and enemy1_room == False:
        Dialoger.enemyroom1()
        skelet.combat_guide()
        skelet.skelet_combatloop()
        enemy1_room = True
        key1 = True
    
    elif place == 3 and horizont == "right" and enemy1_room == True:
        print("Skeletet är död och det finns inget mer här")
    
    elif place == 1 and horizont == "left" and enemy2_room == False:
        Dialoger.enemyroom2()
        lavaskelet.combat_guide()
        lavaskelet.lavaskelet_combatloop()
        enemy2_room = True
    
    elif place == 1 and horizont == "left" and enemy2_room == True:
        print("lavaskeletet är död men det finns en ny dörr som verkar vara låst\n")

    elif place == 2 and horizont == "left" and riddle_room == False:
        Dialoger.riddle()
        riddle_room = True
        key2 = True
    
    elif place == 2 and horizont == "left" and riddle_room == True:
        print("Du går tillbaks till Draku men han har inge fler gåtor åt dig\n")
    
    elif place == 4 and wiseman_room == False:
        Dialoger.oldman()
        wiseman_room = True
    
    elif place == 4 and wiseman_room == True:
        print("Du går tillbaks till Gunnar men han har inga fler gåtor åt dig\n")

    elif place == 5:
        Dialoger.boss()
        boss.combat_guide()
        boss.boss_combatloop()
        Dialoger.bossdead()

    elif place == 6:
        Dialoger.lastright()
        death = True

    elif place == 7:
        Dialoger.lastleft()
        win = True

def back():
    print("Du går tillbaka till grottan bakom dig och är där nu\n")
    time.sleep(1)

def deadend():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    deadend_option = None
    Dialoger.kartaintruktion()
    while deadend_option != "2":
        
        deadend_option = input("Du kan bara gå bak just nu!!! (Ange 2 för att gå bakåt):").lower()
    
        if deadend_option == "2":
           back()
           place = place - 1
        elif deadend_option == "k":
            maps.map_guuide()
        else:
            print("Du kan bara skriva 2 eller k !!!\n")
        


def position():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    if place == 0 and horizont == None and key1 == False:
        
        start_option = None
        Dialoger.kartaintruktion()
        while start_option not in ["3", "1"]:
            
            start_option = input("Vill du gå vänster eller höger? (Ange 1 för vänster eller 3 för höger):").lower()

            if start_option == "3":
                Dialoger.caveright()
                horizont = "right"
                place = place + 1
            elif start_option == "1":
                Dialoger.caveleft()
            elif start_option == "k":
                maps.map_guuide()
                maps.start_map()
            else: 
                print("Du kan bara skriva 1, 3 ellr k !!!\n")

    elif place == 1 and horizont == "right" and key1 == False:
        Dialoger.room2()
        general_option = None
        Dialoger.kartaintruktion()
        while general_option not in ["3", "1", "2"]:
            
            general_option = input("Vart vill du gå? (Ange 1 för vänster, 3 för höger eller 2 för att gå bakåt):").lower()

            if general_option == "3":
                Dialoger.rightdoor1()
                place = place + 1
            elif general_option == "1":
                Dialoger.leftdoor1()
                place = place + 2
            elif general_option == "2":
                back()
                place = place - 1
                horizont = None
            elif general_option == "k":
                maps.map_guuide()
                maps.högra_tunneln_map()
            else:
                print("Du kan bara skriva 3, 1, 2 eller k !!!\n")
            
    elif place == 2 and horizont == "right" and key1 == False:
        Dialoger
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":
        
            deadend_option = input("Du kan bara gå bak just nu!!! (Ange 2 för att gå bakåt):").lower()
    
            if deadend_option == "2":
                back()
                place = place - 1
            elif deadend_option == "k":
                maps.map_guuide()
                maps.dead_end_map()
            else:
                print("Du kan bara skriva 2 eller k !!!\n")
            
    elif place == 3 and horizont == "right" and key1 == False:
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":
            
            deadend_option = input("Ange 2 för att gå bakåt:").lower()

            if deadend_option == "2":
                place = place - 2
                back()
            elif deadend_option == "k":
                maps.map_guuide()
                maps.skelet_map()
            else:
                print("Bakåt är den enda vägen!(Ange 2 för att gå bakåt)\n")

    elif place == 1 and horizont == "right" and key1 == True:
        Dialoger.room2()
        print("Du har nyckeln nu, gå tillbaks till början och öppna den låsta dörren.\n")
        general_option = None
        Dialoger.kartaintruktion()
        while general_option not in ["3", "1", "2"]:

            general_option = input("Vart vill du gå? (Ange 1 för vänster, 3 för höger eller 2 för att gå bakåt):").lower()

            if general_option == "3":
                Dialoger.rightdoor1()
                place = place + 1
            elif general_option == "1":
                Dialoger.leftdoor1()
                place = place + 2
            elif general_option == "2":
                back()
                place = place - 1
                horizont = None
            elif general_option == "k":
                maps.map_guuide()
                maps.högra_tunneln_map()
            else:
                print("Du kan bara skriva 3, 1, 2 eller k !!!\n")

    elif place == 2 and horizont == "right" and key1 == True:
        print("Du har nyckeln, gå tillbaks till start!\n")
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":
        
            deadend_option = input("Du kan bara gå bak just nu!!! (Ange 2 för att gå bakåt):").lower()
    
            if deadend_option == "2":
                back()
                place = place - 1
            elif deadend_option == "k":
                maps.map_guuide()
                maps.dead_end_map()
            else:
                print("Du kan bara skriva 2 eller k!!!\n")

    elif place == 3 and horizont == "right" and key1 == True:
        print("Du har nyckeln, gå tillbaks till början och öppna den låsta dörren.\n")
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":

            deadend_option = input("Du kan bara gå bak just nu!!!(Ange 2 för att gå bakåt):").lower()
            
            if deadend_option == "2":
                place = place - 2
                back()
            elif deadend_option == "k":
                maps.map_guuide()
                maps.skelet_map()
            else:
                print("Du kan bara skriva 2 eller k !!!\n")

    elif place == 0 and horizont == None and key1 == True:
        print("Du är tillbaks till början\n")
        print("Nu kan du öppna vänstra dörren!\n")
        option = None
        Dialoger.kartaintruktion()
        while option not in ["3", "1"]:
            
            option = input("Vill du gå höger eller vänster? (Ange 1 för vänster eller 3 för höger):").lower()

            if option == "3":
                Dialoger.caveright()
                horizont = "right"
                place = place + 1
            elif option == "1":
                Dialoger.havekey()
                horizont = "left"
                place = place + 1
            elif option == 'k':
                maps.map_guuide()
                maps.start_map()
            else: 
                print("Du kan bara skriva 1, 3 eller k !!!\n")

    elif place == 1 and horizont == "left" and key2 == False:
        key_option = None
        Dialoger.kartaintruktion()
        while key_option not in ["3", "1", "2"]:
            
            key_option = input("Vart vill du gå? (Ange 1 för vänster, 3 för höger eller 2 för att gå bakåt):").lower()

            if key_option == "3":
                place = place + 1
            elif key_option == "1":
                print("Dörren är låst, du behöver hitta den nya nyckeln!\n")
            elif key_option == "2":
                place = place - 1
                horizont = None
                print("Du går tillbaka till grottan bakom dig")
                time.sleep(1)
            elif key_option == "k":
                maps.map_guuide()
                maps.lava_skelet_map()
            else: 
                print("Du kan bara skriva 1, 3 eller k !!!\n")

    elif place == 2 and horizont == "left" and key2 == False:
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":
        
            deadend_option = input("Du kan bara gå bak just nu!!! (Ange 2 för att gå bakåt):").lower()
    
            if deadend_option == "2":
                back()
                place = place - 1
            elif deadend_option == "k":
                maps.map_guuide()
                maps.draku_map()
            else:
                print("Du kan bara skriva 2 eller k !!!\n")

    elif place == 2 and horizont == "left" and key2 == True:
        print("Det finns inget mer här.\n")
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":
        
            deadend_option = input("Du kan bara gå bak just nu!!! (Ange 2 för att gå bakåt):").lower()
    
            if deadend_option == "2":
                back()
                place = place - 1
            elif deadend_option == "k":
                maps.map_guuide()
                maps.draku_map()
            else:
                print("Du kan bara skriva 2 eller k!!!\n")

    elif place == 1 and horizont == "left" and key2 == True:
        print("Nu kan du öppna den vänstra dörren!")
        key_option = None
        Dialoger.kartaintruktion()
        while key_option not in ["3", "1", "2"]:
            
            key_option = input("Vart vill du gå? (Ange 1 för vänster, 3 för höger eller 2 för att gå bakåt):").lower()

            if key_option == "3":
                place = place + 1
            elif key_option == "1":
                Dialoger.nyckelnvänster()
                Dialoger.emptyroom()
                place = place + 2
            elif key_option == "2":
                back()
                place = place - 1
                horizont = None
            elif key_option == "k":
                maps.map_guuide()
                maps.lava_skelet_map()
            else: 
                print("Du kan bara skriva 1, 3 eller k !!!\n")

    elif place == 3 and horizont == "left":
        print("Det finns inget mer här")
        key2_option = None
        Dialoger.kartaintruktion()
        while key2_option not in ["3", "1", "2"]:
            
            key2_option = input("Vart vill du gå? (Ange 1 för vänster, 3 för höger eller 2 för att gå bakåt):").lower()

            if key2_option == "3":
                place = place + 2
            elif key2_option == "1":
                place = place + 1
            elif key2_option == "2":
                back()
                place = place - 2
            elif key2_option == 'k':
                maps.map_guuide()
                maps.tom_tunnel2_map()
            else: 
                print("Du kan bara skriva 1, 3, 2 eller k !!!\n")

    elif place == 4:
        deadend_option = None
        Dialoger.kartaintruktion()
        while deadend_option != "2":
        
            deadend_option = input("Du kan bara gå bak just nu!!! (Ange 2 för att gå bakåt):").lower()
    
            if deadend_option == "2":
                back()
                place = place - 1
            elif deadend_option == "k":
                maps.map_guuide()
                maps.gammal_man_map()
            else:
                print("Du kan bara skriva 2 eller k!!!\n")

    elif place == 5:
        print("Stenarna blockerade vägen tillbaka och du kan bara gå framåt nu\n")
        end_option = None
        while end_option not in ["3", "1"]:
            
            end_option = input("Vart vill du gå? (Ange 1 för vänster eller 3 för höger):")

            if end_option == "3":
                place = place + 1
            elif end_option == "1":
                place = place + 2
            else: 
                print("Du kan bara skriva 1 eller 3 !!!\n")
    elif place == 6:
        print("DU DOG\n")

    elif place == 7:
        print("DU VANN\n")

Dialoger.title()
Dialoger.room1()

def stone_depth():
    global death
    global win
    while win != True and death != True:
        position()
        event()
