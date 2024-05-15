import PySimpleGUI as sg
import start, gui2, bat, skelet2_0, gui3, custom, gui4

start_knapp = 0

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font="Franklin 14", button_element_size=(10, 2))
    layout = [
        [sg.Text("", font="Franklin 26", justification="center", expand_x=True, pad=(10, 20), right_click_menu=theme_menu, key="-TEXT-")],
        [sg.Text("Tryck på en knapp i taget!", justification="center", expand_x=True, font="Franklin 18")],
        [sg.Button("Start", size=(10, 2), pad=(5, 20)), sg.Button("Avsluta", size=(10, 2))],
        [sg.Text("Välj tema:", size=(15, 1), font="Franklin 14"), sg.Combo(values=theme_menu[1], default_value=theme, readonly=True, key="-THEME-")]
    ]
    return sg.Window("Kontroller", layout, finalize=True)

theme_menu = ["menu", ["LightGrey1", "DarkTeal1", "DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark"]]
window = create_window("DarkTeal9")

print("Tryck på start på kontrollen för att starta spelet!")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Avsluta":
        break

    if event == "Start" and start_knapp == 0:
        start_knapp += 1
        start.title()
        start.start_screen()
        start.intro()
        bat.bat()
        start.bat_dialog()
        bat.combatguide()
        gui2.bat_gui2()
        start.enemy1_enemy2()
        skelet2_0.skelet()
        start.skelet_dialog()
        skelet2_0.skelet_combatguide()
        gui3.skelet_gui()
        start.draku_intro()
        custom.loot()
        gui4.ending()

    elif event == "Start" and start_knapp > 0:
        print("Du har redan tryckt på start!")

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

window.close()
