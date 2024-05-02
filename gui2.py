import PySimpleGUI as sg, bat, skelet2_0; from bat import spelare_attack, enemy_attack, bat_alive
start_knapp = 0

def bat_gui2():
    val = {
        "➀": 1,
        "➁": 2,
        "➂": 3}
    def create_window(theme):
        sg.theme(theme)
        sg.set_options(font = "Franklin 14", button_element_size = (4,1,5))
        button_size = (3,2)
        layout = [[sg.Text(
            "", font = "Franklin 26", justification = "right", expand_x = True, pad = (10,20), right_click_menu = theme_menu, key = "-TEXT-")],      
            [sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push() ,sg.Push(), sg.Push(),sg.Push(), sg.Button("➀", size = button_size),sg.Push(), sg.Push() ,sg.Push(), sg.Button("🎒", size = button_size)],
            [sg.Button("➁", size = button_size), sg.Push() ,sg.Push() ,sg.Push(), sg.Button("➂", size = button_size), sg.Push(), sg.Push()],
            []
            
        ]
        return sg.Window("Kontroller", layout)
    theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
    window = create_window("DarkTeal9")
     
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event in val:
            weapon_choice = val[event]
            print("Ange siffran du vill attackera fladdermusen med:")
            spelare_attack(weapon_choice) 
            enemy_attack() 
        if bat.bat_HP <=0:
            window.close

        if event in ["🎒"] and bat_alive == False:
            skelet2_0.skelet_combatguide()
        if event in ["🎒"] and bat_alive == True:
            bat.combatguide()
            
    window.close()