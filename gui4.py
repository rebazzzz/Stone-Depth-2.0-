import PySimpleGUI as sg
import time

def ending():
    text = """
    Så fort du läser den förvandlas grottan till ditt barndomshem. En röst talar till dig och påminner om vad som står på spel. 
    Du ser att valet är ditt: 
    Antingen ge upp och fly, och riskera att bli betraktad som en fegis, eller fortsätta framåt och möta din säkra död i striden. 
    Men då blir du en hjälte och familjens stolthet.
    Men är det värt att offra dig för din familjs stolthet, särskilt om det var de som ville bli av med dig?
    """

    layout = [
        [sg.Text("", size=(60, 10), key='-TEXT-')],
        [sg.Button("Dö som en hjälte", key='1', size=(15, 2)), sg.Button("Leva som en fegis", key='2', size=(15, 2))],
    ]
    
    window = sg.Window("Valet är ditt", layout, finalize=True)

    for ord in text:
        current_text = window['-TEXT-'].get()
        window['-TEXT-'].update(current_text + ord)
        time.sleep(0.05)
        window.refresh()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == '2':
            sg.popup("Monstret öppnar upp en väg som leder direkt hem, men när familjen ser att du har flytt så samlar de byn och markerar dig som fredlös.")
            break

        if event == '1':
            sg.popup("Innan du hinner reagera exploderar ditt huvud och du faller livlös till marken. När flera dagar går utan att du dyker upp i byn reser de en staty till dig för att minnas dig som en hjälte och för att hedra dig.")
            break

        else:
            sg.popup("Du kan inte undvika att fatta ett beslut! Skriv 1 eller 2")
    
    window.close()

if __name__ == "__main__":
    ending()
