import time, bat
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

def namn():
    global spelare
    spelare = input("Vad heter du kära spelare?\n")
namn()

def intro():
    text = f"""
    Välkommen till Grottan av Evigheten {spelare}. Mörkret här är tjockt, och dess hemligheter är lika mystiska som farliga. 
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
bat.forsta_enemy()

