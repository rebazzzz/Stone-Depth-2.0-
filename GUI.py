import PySimpleGUI as sg, start, bat, os, time; from bat import player_hp, pickaxe_dmg, enemy_hp, vapen, bat_HP, yxa_dmg, magisktlubba_dmg, magisktlubba_uses, fel_combat_input
# def fonster(theme):
#     sg.theme(theme)
#     sg.set_options(font="Franklin 15", button_element_size=(6, 3))
#     button_size = (5, 4)
#     layout = [
#         [sg.Text("", font="Franklin 26", justification="right", expand_x=True, pad=(11, 21), right_click_menu=meny, key="-TEXT-")],
#         [sg.Button(0, expand_x=True), sg.Button(".", size=button_size)],
#         [sg.Button(2, size=button_size), sg.Button(5, size=button_size), sg.Button(3, size=button_size), sg.Button("*", size=button_size)],
#         [sg.Button(7, size=button_size), sg.Button(1, size=button_size), sg.Button(6, size=button_size), sg.Button("Clear", expand_x=True)],
#         [sg.Button(9, size=button_size), sg.Button(8, size=button_size), sg.Button(4, size=button_size), sg.Button("-", size=button_size)],
#         [sg.Button("/", size=button_size), sg.Button("Enter", expand_x=True), sg.Button("+", size=button_size)],
#         [sg.Button("x^2", size=(10, 2))]
#     ]
#     return sg.Window("Storräknare", layout)

# meny = ["menu",["Rebaz","DarkTeal1","Red", "Black", "Purple", "Yellow", "Brown"]]
# window = fonster("Tan")

# cn = []
# op = []


# def kvadrat(num):
#     return num ** 2

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
    
#     if event in meny[1]:
#         window.close()
#         window = fonster(event)
    
#     if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
#         cn.append(event)
#         num_string = "".join(cn)
#         window["-TEXT-"].update(num_string)
    
#     if event in ["+", "-", "/", "*"]:
#         op.append("".join(cn))
#         cn = []
#         op.append(event)
#         window["-TEXT-"].update("")
            
#     if event == "Enter":
#         op.append("".join(cn))
#         result = eval("".join(op))
#         window["-TEXT-"].update(result)
#         op = []
    
#     if event == "Clear":
#         cn = []
#         op = []
#         window["-TEXT-"].update("")
    
#     if event == "x^2":
#         if cn:
#             num = float("".join(cn))
#             result = kvadrat(num)
#             window["-TEXT-"].update(result)
#             cn = []


# window.close()

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Franklin 14", button_element_size = (4,1,5))
    button_size = (3,2)

    layout = [[sg.Text(
        "", font = "Franklin 26", justification = "right", expand_x = True, pad = (10,20), right_click_menu = theme_menu, key = "-TEXT-")],      
         [sg.Button("Credits"), sg.Button("Start")],
         [sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push() ,sg.Push(), sg.Push(),sg.Push(), sg.Button("➀", size = button_size),sg.Push(), sg.Push() ,sg.Push(), sg.Button("🎒", size = button_size)],
         [sg.Button("➁", size = button_size), sg.Push() ,sg.Push() ,sg.Push(), sg.Button("➂", size = button_size), sg.Push(), sg.Push()],
         []
         
    ]
    return sg.Window("Stone Depth 2.0", layout)

theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("BrownBlue") 

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

def combatloop():
    global magisktlubba_uses
    while player_hp > 0 or enemy_hp > 0:
        bat.spelare_attack()
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

        bat.enemy_attack()
        time.sleep(0.5)
        if player_hp <= 0:
            print("GAME OVER")
            break

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in ["Start"]:
        start.title()
        start.start_screen()
        start.intro()
        bat.bat()
        start.bat_dialog()
        bat.combatguide()
        
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event in ["➀","➁","➂"]:
        bat.forsta_enemy()

    if event in ["Credits"]:
        start.credit()
        
    if event in ["🎒"]:
        bat.combatguide()
        
    if event == "Enter":
        op.append("".join(cn))
        result = eval(" ".join(op))
        window["-TEXT-"].update(result)
        op = []
    
    if event == "Clear":
        cn = []
        op = []
        window["-TEXT-"].update("")

window.close()
