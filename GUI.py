import PySimpleGUI as sg, start, gui2, bat, skelet2_0; from bat import spelare_attack, enemy_attack, bat_alive
start_knapp = 0

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Franklin 14", button_element_size = (4,1,5))
    layout = [[sg.Text(
        "", font = "Franklin 26", justification = "right", expand_x = True, pad = (10,20), right_click_menu = theme_menu, key = "-TEXT-")],      
         [sg.Text("Tryck på en knapp i taget!")],
         [sg.Button("Credits"), sg.Button("Start")]]
    return sg.Window("Kontroller", layout)
theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("DarkTeal9") 
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
        # bat.combatguide()
        # print("Ange siffran du vill attackera fladdermusen med:")
        gui2.bat_gui2()

    if event in ["Start"] and start_knapp <= 0: 
        print("Du har redan tryckt på start!")

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ["Credits"]:
        start.credit()
        
    window.close()