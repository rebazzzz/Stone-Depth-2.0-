import time, bat, custom, skelet2_0
spelare = ""
def title():
    print("""
    __ _                        ___           _   _           ____         ___  
   / _\ |_ ___  _ __   ___     /   \___ _ __ | |_| |__  ___  |___ \       / _ \ 
   \ \| __/ _ \| '_ \ / _ \   / /\ / _ \ '_ \| __| '_ \/ __|   __) |     | | | |
   _\ \ || (_) | | | |  __/  / /_//  __/ |_) | |_| | | \__    / __/   _  | |_| | 
   \__/\__\___/|_| |_|\___| /___,' \___| .__/ \__|_| |_|___/ |_____| (_)  \___/ 
                                      |_|                  
             
    Välkommen till Stone Depth 2.0
          """)
title()

def start_screen():
    text = f"""
    Du har blivit tilldelad en uppdrag av din familj att utforska denna grotta, 
    upptäcka dess hemligheter och återvända med "Monstrets hjärta" för att få leva med dem.
    De har gett dig med en fackla och några vapen för att hjälpa dig överleva i grottan.
    Du stiger in i grottan, vars mörker omsluter dig som en tätnande dimma...
    """
    for ord in text:
        print(ord, end='', flush=True)
        time.sleep(0.05)
start_screen()



custom.char_sel()
def namn():
    global spelare
    print("Innan vi fortsätter behöver du ge ett namn till din karaktär.")
    spelare = input("Vad vill du att karaktären ska heta?")
namn()

def intro():
    text = f"""
    ...Välkommen till Grottan av Evigheten {spelare}. Mörkret här är tjockt, och dess hemligheter är lika mystiska som farliga. 
    Legender talar om skatter och skräckinjagande varelser som gömmer sig i de mörka skuggorna. Men du är inte rädd. 
    Du är redo att utforska, att upptäcka, och kanske till och med att överleva. 
    Din resa börjar nu. Ta dig ut LEVANDE!
    
    Med bara en fackla för att lysa upp vägen, trampar du försiktigt framåt. Varje steg du tar känns som ett steg djupare in i det okända."""
    for ord in text:
        print(ord, end='', flush=True)
        time.sleep(0.05)

intro()

bat.bat()
print(f"""
      Med en plötslig och grym attack känner du dess vassa klor nära din hud.
      Fladdermusen hotar: Jag vet vem du är {spelare}. 
      Jag kommer suga ut allt ditt blod!
        
    """)

print

bat.forsta_enemy()

skelet2_0.andra_enemy()
