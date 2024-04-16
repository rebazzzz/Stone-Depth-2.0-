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
        print ("Du är inne i ett rum med inga mer vägar men en kista är framför dig!\n")
        time.sleep(2)

        val = int(input("Vill du öppna kistan eller inte? (skriv 1 för att öppna, 2 för att inte.):"))

        if val == 1:
            print ("Du öppna kistan och hittade inget där de bara stenar och kol inuti!\n")
            item_room = True
            item = True

        if val == 2:
            print ("Du valde att inte öppna kistan men du kan öppna den senare!\n")

    elif place == 2 and horizont == "right" and item_room == True:
        print("Du har redan vaarit här och öpppnat kistan\n")

    elif place == 3 and horizont == "right" and enemy1_room == False:
        Dialoger.enemyroom1()
        skelet.combat_guide()
        skelet.skelet_combatloop()
        enemy1_room = True
        key1 = True
    
    elif place == 3 and horizont == "right" and enemy1_room == True:
        print("skeletet är död och det finns inget mer här")
    
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
        print("du går tillbaks till Draku men han har inge fler gåtor åt dig\n")
    
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
    print("du går tillbaka till grottan bakom dig och är där nu\n")
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
    while deadend_option != "3":
        deadend_option = input("Du kan bara gå bak just nu!!! (Ange 3 för att gå backåt):")
    
        if deadend_option == "3":
           back()
           place = place - 1
        else:
            print("Du kan bara skriva 3 !!!\n")
        


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
        while start_option not in ["0", "1"]:
        
            start_option = input("Vill du gå vänster eller höger? (Ange 1 för vänster eller 0 för höger):")

            if start_option == "0":
                Dialoger.caveright()
                horizont = "right"
                place = place + 1
            elif start_option == "1":
                Dialoger.caveleft()
            else: 
                print("Du kan bara skriva 1 eller 0 !!!\n")

    elif place == 1 and horizont == "right" and key1 == False:
        Dialoger.room2()
        print("Hitta nyckeln till den låsta dörren!\n")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):")

            if general_option == "0":
                Dialoger.rightdoor1()
                place = place + 1
            elif general_option == "1":
                Dialoger.leftdoor1()
                place = place + 2
            elif general_option == "3":
                back()
                place = place - 1
                horizont = None
            else:
                print("Du kan bara skriva 0, 1 eller 3 !!!\n")
            
    elif place == 2 and horizont == "right" and key1 == False:
        Dialoger
        print("Du behöver att hitta en nyckel!")
        general_option = None
        deadend()
            
    elif place == 3 and horizont == "right" and key1 == False:
        print("Du behöver hitta en nyckel!\n")
        deadend_option = None
        while deadend_option != "3":
            deadend_option = input("Ange 3 för att gå backåt:")
    
            if deadend_option == "3":
                place = place - 2
                back()
            else:
                print("Bakåt är den enda vägen!(Ange 3 för att gå bakåt)\n")

    elif place == 1 and horizont == "right" and key1 == True:
        Dialoger.room2()
        print("Du har nyckeln nu, gå tillbaks till början och öppna den låsta dörren.\n")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):")

            if general_option == "0":
                Dialoger.rightdoor1()
                place = place + 1
            elif general_option == "1":
                Dialoger.leftdoor1()
                place = place + 2
            elif general_option == "3":
                back()
                place = place - 1
                horizont = None
            else:
                print("Du kan bara skriva 0, 1 eller 3 !!!\n")

    elif place == 2 and horizont == "right" and key1 == True:
        print("Du har nyckeln, gå tillbaks till start!\n")
        deadend()

    elif place == 3 and horizont == "right" and key1 == True:
        print("Du har nyckeln, gå tillbaks till början och öppna den låsta dörren.\n")
        deadend_option = None
        while deadend_option != "3":
            deadend_option = input("Du kan bara gå back just nu!!!(Ange 3 för att gå backåt):")
    
            if deadend_option == "3":
                place = place - 2
                back()
            else:
                print("Du kan bara skriva 3 !!!\n")

    elif place == 0 and horizont == None and key1 == True:
        print("du är tillbaks till början\n")
        print("Nu kan du öppna vänstra dörren!\n")
        option = None
        while option not in ["0", "1"]:
            option = input("Vill du gå höger eller vänster? (Ange 1 för vänster eller 0 för höger):")

            if option == "0":
                Dialoger.caveright()
                horizont = "right"
                place = place + 1
            elif option == "1":
                Dialoger.havekey()
                horizont = "left"
                place = place + 1
            else: 
                print("Du kan bara skriva 1 eller 0 !!!\n")

    elif place == 1 and horizont == "left" and key2 == False:
        key_option = None
        while key_option not in ["0", "1", "3"]:
        
            key_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):")

            if key_option == "0":
                place = place + 1
            elif key_option == "1":
                print("Dörren är låst, du behöver hitta den nya nyckeln!\n")
            elif key_option == "3":
                place = place - 1
                horizont = None
                print("du går tillbaka till grottan bakom dig")
                time.sleep(1)
            else: 
                print("Du kan bara skriva 1 eller 0 !!!\n")

    elif place == 2 and horizont == "left" and key2 == False:
        deadend()

    elif place == 2 and horizont == "left" and key2 == True:
        print("Det finns inget mer här.\n")
        deadend()

    elif place == 1 and horizont == "left" and key2 == True:
        print("Nu kan du öppna den vänstra dörren!\n")
        key_option = None
        while key_option not in ["0", "1", "3"]:
        
            key_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):")

            if key_option == "0":
                place = place + 1
            elif key_option == "1":
                Dialoger.nyckelnvänster()
                Dialoger.emptyroom()
                place = place + 2
            elif key_option == "3":
                back()
                place = place - 1
                horizont = None
            else: 
                print("Du kan bara skriva 1 eller 0 !!!\n")

    elif place == 3 and horizont == "left":
        print("Det finns inget mer här")
        key2_option = None
        while key2_option not in ["0", "1", "3"]:
        
            key2_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):")

            if key2_option == "0":
                place = place + 2
            elif key2_option == "1":
                place = place + 1
            elif key2_option == "3":
                back()
                place = place - 2
            else: 
                print("Du kan bara skriva 1, 0 eller 3 !!!\n")

    elif place == 4:
        deadend()

    elif place == 5:
        print("Stenarna blockerade vägen tillbaka och du kan bara gå framåt nu\n")
        end_option = None
        while end_option not in ["0", "1", "3"]:
        
            end_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):")

            if end_option == "0":
                place = place + 1
            elif end_option == "1":
                place = place + 2
            elif end_option == "3":
                print("Stenarna är för tunga och du lyckas inte ta dig tillbaka\n")
            else: 
                print("Du kan bara skriva 1 eller 0 !!!\n")
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
