import PySimpleGUI as sg
import skelet2_0

def skelet_gui():
    val = {
        "➀": 1,
        "➁": 2,
        "➂": 3
    }

    def create_window(theme):
        sg.theme(theme)
        sg.set_options(font="Franklin 14", button_element_size=(4, 1, 5))
        button_size = (6, 3)
        layout = [
            [sg.Text("Välkommen till Stone Depth 2.0", font=("Helvetica", 20), text_color="white", 
                     background_color="midnightblue", pad=(0, 20))],
            [sg.Column([
                [sg.Text("Tryck på en knapp i taget!", font=("Helvetica", 14), text_color="white", 
                         background_color="midnightblue", pad=(0, 20))],
                [sg.Button("➀", size=button_size, font=("Helvetica", 16), key="➀", button_color=("white", "darkslategrey")),
                 sg.Button("🎒", size=(3, 2), font=("Helvetica", 16), key="🎒", button_color=("white", "darkslategrey"))],
                [sg.Button("➁", size=button_size, font=("Helvetica", 16), key="➁", button_color=("white", "darkslategrey")),
                 sg.Button("➂", size=button_size, font=("Helvetica", 16), key="➂", button_color=("white", "darkslategrey"))]
            ], justification='center')],
            []
        ]
        return sg.Window("Kontroller", layout)

    theme_menu = ["menu", ["LightGrey1", "DarkTeal1", "DarkGray8", "DarkRed", "BluePurple", "BrightColors",
                           "BrownBlue", "Dark"]]
    window = create_window("DarkTeal9")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event in val:
            weapon_choice = val[event]
            print("Ange siffran du vill attackera skelettet med:")
            skelet2_0.spelare_attack(weapon_choice)
            if skelet2_0.enemy_hp > 0:
                skelet2_0.enemy_attack()
            else:
                print("Skelettet har besegrats!")
                window.close()
                break

        if event == "🎒":
            skelet2_0.skelet_combatguide()
            if not skelet2_0.enemy_hp:
                skelet2_0.skelet_combatguide()

    window.close()

if __name__ == "__main__":
    skelet_gui()
