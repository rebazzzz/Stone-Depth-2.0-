import PySimpleGUI as sg

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
         [sg.Button("Options"), sg.Button("Start")],
         [sg.Button("↑", size = button_size), sg.Button("🎒", size = button_size), sg.Push(), sg.Button("➀", size = button_size)],
         [sg.Button("←", size = button_size), sg.Button("→", size = button_size), sg.Push(), sg.Button("➁", size = button_size), sg.Push(), sg.Button("➂", size = button_size)],
         [sg.Button("↓", size = button_size)],
         
    ]
    return sg.Window("Stone Depth 2.0", layout)

theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("BrownBlue") 

cn = []
op = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event in ["0","1","2","3","4","5","6","7","8","9","."]:
        cn.append(event)
        num_string = "".join(cn)
        window["-TEXT-"].update(num_string)
        
    if event in ["+","-","/","*"]:
        op.append("".join(cn))
        cn = []
        op.append(event)
        print(op)
        window["-TEXT-"].update("")
        
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