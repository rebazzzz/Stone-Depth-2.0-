import PySimpleGUI as sg
import time, start
from bat import combatguide, spelare_attack, enemy_attack, bat_HP, bat_alive

start_knapp = 0


weapon_choices = {
    "➀": 1,
    "➁": 2,
    "➂": 3
}

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font="Franklin 14", button_element_size=(4, 1, 5))
    button_size = (3, 2)

    layout = [
        [sg.Text("", font="Franklin 26", justification="right", expand_x=True, pad=(10, 20), key="-TEXT-")],
        [sg.Button("Credits"), sg.Button("Start")],
        [sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Push(),
         sg.Button("➀", size=button_size), sg.Push(), sg.Push(), sg.Push(), sg.Button("🎒", size=button_size)],
        [sg.Button("➁", size=button_size), sg.Push(), sg.Push(), sg.Push(), sg.Button("➂", size=button_size),
         sg.Push(), sg.Push()],
        []
    ]
    return sg.Window("Kontroller", layout)


theme_menu = ["menu", ["LightGrey1", "DarkTeal1", "DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("Rebaz")

print("Tryck på start på kontrollen för att starta spelet!")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Start" and start_knapp == 0:
        start_knapp = start_knapp + 1
        combatguide()
        print("Ange siffran du vill attackera fladdermusen med:")
        
    if event == "Start" and start_knapp <= 0:
        print("Du har redan tryckt på start!")

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in weapon_choices:
        weapon_choice = weapon_choices[event]
        spelare_attack(weapon_choice) 
        enemy_attack()  

    if event == "Credits":
        start.credit()

    if event == "🎒" and bat_alive == False:
        combatguide()
    elif event == "🎒" and bat_alive == True:
        combatguide()

window.close()
