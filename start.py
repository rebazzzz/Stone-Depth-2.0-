import time, bat, custom, skelet2_0, threading

# def Stone_Depth_2_0():

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
# title()


# def wait():
#         input("Tryck på Start för att börja spela Stone Depth 2.0...")


# def credits():
#         print("\nDu verkar vara AFK\nCredits visas snart.... \nTryck på Star för att avsluta credits, annars kommer den att spelas om. Observera att alla credits måste spelas ut innan du kan fortsätta.")
#         time.sleep(1)
#         credits = [
#             "Credits:",
#             "Inspiration: Stone Depth",
#             "Huvudutvecklare: Rebaz Abdul Rashid",
#             "Story: Rebaz Abdul Rashid & ChatGPT",
#             "Design: Rebaz Abdul Rashid",
#             "Combat system: Rebaz Abdul Rashid & Malik Zahir",
#             "Testare: Veljko Jovic, David Wroblewski, Malik Zahir, Johanna Stode, Emin Kosovac, Edvin Schalin, Sixten Wilde & Victor Nordlund, Rangin Abdul Rashid",
#             "Specialtack till: Johanna Stode & ChatGPT",
#         ]
#         for x in credits:
#             for i in x:
#                 print(i, end='', flush=True)
#                 time.sleep(0.03)
#             time.sleep(1)
#             print()
        
# def start_credits():
#         thread = threading.Thread(target=wait)
#         thread.start()
#         thread.join(timeout=3)
        
#         while True:
#              if thread.is_alive():
#                 credits()
#              else:
#                 break
            
        
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

        

# start_credits()
# start_screen()



# custom.char_sel()
# def namn():
#         global spelare
#         print("Innan vi fortsätter behöver du ge ett namn till din karaktär.")
#         spelare = input("Vad vill du att karaktären ska heta?")
# namn()

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

# intro()

# bat.bat()
def bat_dialog():
    print(f"""
        Med en plötslig och grym attack känner du dess vassa klor nära din hud.
        Fladdermusen hotar: Jag vet varför du är här {spelare}. 
        Jag kommer suga ut allt ditt blod!
            
        """)
# bat_dialog()
# bat.forsta_enemy()

# def enemy1_enemy2():
#         text = """
#         Med hjärtat bultande av både spänning och fruktan fortsätter du din färd djupare in i grottans skrämmande djup. 
#         Dina fotsteg ekar mot de steniga väggarna. Plötsligt, i mörkret framför dig, hör du ljudet av skallrande ben och det döda, kusliga skrattet av ett skelett.
#         """
#         for ord in text:
#             print(ord, end='', flush=True)
#             time.sleep(0.05)

# enemy1_enemy2()

# skelet2_0.skelet()
# def skelet_dialog():
#         text = """
#         Du! Jag trodde att fladdermusen hade gjort slut på dig! Men nu spelar det ingen roll vad den gjorde, för jag ska se till att du inte lämnar den här grottan levande
#         Skelettets kusliga skratt fyller luften när han attackerar dig, du ser att han håller i en glimmande gyllene yxa. 
#         Med snabb reflex sparkar du ner honom och griper tag i yxan. Den är nu din. 
#         Med den nya yxan i handen står du redo att möta skelettet
#         """

#         for ord in text:
#             print(ord, end='', flush=True)
#             time.sleep(0.05)
# skelet_dialog()
# skelet2_0.andra_enemy()

# def draku_intro():
#         text = f"""
#         Djupare in i grottan möter du en mystisk staty med namnet Draku Sraku. 
#         Dess ögon lyser i mörkret när den plötsligt talar till dig. "Jag vet allt om dig, {spelare}" säger den med en viskande röst.

#         Du: Hur kan jag lita på dig?
#         Draku: Jag vet varför du är här. Din familj skickade dig hit för att bli av med dig!
#         Ingen i tusentals år har lyckats att döda monstret i den här grottan.
#         Din familj lurade dig!

#         Du: Hur kunde dem göra så mot mig?! 😭😭
        
#         Draku: Följ mig, och jag ska visa dig vägen till ett ställe i grottan där du kan finna bättre loot. 
#         Det kommer att hjälpa dig att besegra din sista fiende och ta dig ut i grottan levandes. 
        
#         Du känner en blandning av spänning och oro när du följer statyn in i djupet av grottan, med förhoppningen om att den har svaren och resurserna du behöver för att överleva.
#         """
#         print("""       
    
#                 )   )\/ ( ( (
#               ((  /     ))\))  (  )    
#                 )\(          |  ))( )  (
#                ))/   |          )/  \((  ) 1
#               (      .        -.     V )/   )   
#             /     .   \            .       \))   
#                 (  | |   )            .    (  
#               ,'))     \ /          \( `.    )
#              ,'/__      ))            __`.  /
#               | /  ___   ( \/     ___   \ | ( 
#              |/  /   \__      __/   \   \|  ))
#            . |>  \      | __ |      /   <|  /
#             )/    \____/ :..: \____/     \ <
#            (|__  .      / ;: \          __| )  
#            \)  ~--_     --  --      _--~    /  
#             |  ||               ||  |   (  /
#              .  |  ||_             _||  |  /
#               :  |  ~V+-I_I_I-+V~  |  : (.
#                \:  T\   _     _   /T  : ./
#                :    T^T T-+-T T^T    ;<
#                 \..`_       -+-       _'
#                . `--=.._____..=--'. ./     """)
#         for ord in text:
#             print(ord, end='', flush=True)
#             time.sleep(0.05)

# def draku_outro():
#         text = f"""
#         Precis innan du når ingången vänder Draku plötsligt om och säger: "Innan jag kan släppa in dig måste du svara på en fråga.
#         Svara med bara siffror annars straffar jag dig!"
#         """
#         for ord in text:
#             print(ord, end='', flush=True)
#             time.sleep(0.05)
#         while True:
#             gata = int(input("Vilket år är Stone Depth skaparen Rebaz född?"))
#             if gata == 2006:
#                 print("""
#             Grattis du svarade rätt på frågan. 
#             Nu kan jag släppa in dig!
#             Hoppas att looten du får här hjälper dig att besegra monstret.
#                 """)
#                 break
#             elif gata == 2001:
#                 print("9/11 Joke how original 😐")

#             elif gata <= 1900:
#                 ban = input("Är du dum i huvudet?").lower()
#                 if ban == "ja":
                
#                  while True:
#                     print("Då ska jag krascha spelet åt dig!")
                    
#                 elif ban == "nej":
#                     print("Bäst för dig!")
#                 else:("Svara ja/nej din idiot!")

#             elif gata >= 2100:
#                 bann = input("Är du dum i huvudet?").lower()
#                 if bann == "nej":
#                     print("Bäst för dig!")
#                 elif bann == "ja":
#                     while True:
#                         print("Då ska jag krascha spelet åt dig!")
#                 else:
#                     ("Svara ja/nej din idiot!")
#             else:
#                 print("Gissa igen!")
                

# draku_intro()
# draku_outro()
# custom.loot()
# custom.ending()

# def credit():
#         print("\nTack för att du spelade Stone Depth 2.0\nCredits visas snart...")
#         credits = [
#             "Credits:",
#             "Inspiration: Stone Depth",
#             "Huvudutvecklare: Rebaz Abdul Rashid",
#             "Story: Rebaz Abdul Rashid & ChatGPT",
#             "Design: Rebaz Abdul Rashid",
#             "Combat system: Rebaz Abdul Rashid & Malik Zahir",
#             "Testare: Veljko Jovic, David Wroblewski, Malik Zahir, Johanna Stode, Emin Kosovac, Edvin Schalin, Sixten Wilde & Victor Nordlund, Rangin Abdul Rashid",
#             "Specialtack till: Johanna Stode & ChatGPT",
#         ]
#         for x in credits:
#             for i in x:
#                 print(i, end='', flush=True)
#                 time.sleep(0.03)
#             time.sleep(1)
#             print()
        

# credit()
