import PySimpleGUI as sg, start, bat, os, skelet2_0, time; from bat import player_hp, pickaxe_dmg, enemy_hp, vapen, bat_HP, yxa_dmg, magisktlubba_dmg, magisktlubba_uses, fel_combat_input, bat_alive
start_knapp = 0

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
    return sg.Window("Kontroller", layout)

theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("Rebaz") 

print("Tryck på start på kontrollen för att starta spelet!")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in ["Start"] and start_knapp == 0:
        start_knapp = start_knapp + 1
        # start.title()
        # start.start_screen()
        # start.intro()
        # bat.bat()
        # start.bat_dialog()
        bat.combatguide()
        print("Ange siffran du vill attackera fladdermusen med:")
    if event in ["Start"] and start_knapp <= 0: 
        print("Du har redan tryckt på start!")
        
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event in ["➀","➁","➂"]:
        pass
    if event in ["Credits"]:
        start.credit()
        
    if event in ["🎒"] and bat_alive == False:
        skelet2_0.skelet_combatguide()
    if event in ["🎒"] and bat_alive == True:
        bat.combatguide()
        
window.close()
