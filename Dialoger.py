import time


def pop_up_text(text, delay=1):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)


# Jag har fått Asciiart från Asciiart.eu, Dessutom så fick jag time sleep samt delay text från en yt video.

# Title 
def title():
  print (""" 
  __ _                        ___           _   _         
 / _\ |_ ___  _ __   ___     /   \___ _ __ | |_| |__  ___ 
 \ \| __/ _ \| '_ \ / _ \   / /\ / _ \ '_ \| __| '_ \/ __|
 _\ \ || (_) | | | |  __/  / /_//  __/ |_) | |_| | | \__ 
 \__/\__\___/|_| |_|\___| /___,' \___| .__/ \__|_| |_|___/
                                    |_|                  
        """)

#Miljö beskrivning, Här börjar alla dialoger och text för varje rum.

#Room1

def kartaintruktion():
    print("*** Ange 'k' om du vill se var du befinner dig på kartan ***")


def room1():
  print ("Du vaknar in i grottan och känner av den kalla luften forsa över.\n")
  time.sleep(2)

  print ("Vid grottans slut finns de två vägar en öppen tunnel åt höger och en dörr åt vänster...\n")
  time.sleep(2)

def caveleft ():
  print ("Du går mot dörren och försöker öppna den men den är låst och du går tillbaka till var du börja.\n")
  time.sleep(2)

def caveright():
  print ("Du går igenom tunneln och fortsätter in i grottan åt höger...\n")
  time.sleep(2)


#om man har nyckeln 
def havekey():
  print ("låsta dörren öppnades och du går igenom.\n")
  time.sleep(2)


#Room2
def room2():
  print ("Två öppna vägar är framför dig en åt höger och en åt vänster...\n")
  time.sleep(2)

def leftdoor1():
  print ("Du går igenom tunneln åt vänster!\n")
  time.sleep(2)

def rightdoor1():
  print ("Du går igenom tunneln åt höger!\n")
  time.sleep(2)


#Deadend1
def loreinfo():
  print ("""Du befinner dig i ett rum utan fler utvägar och hör ett ljud. 
  "Nu när du har kommit in i Grottan, kan du inte lämna förrän du har tagit Stenjättens kärna. Många har inträtt i Grottan, men ingen har lyckats lämna. Det ögonblick du trädde in utlöste du Acinet cursen och är nu fast i en evig loop.    
   Det kan vara din femte loop, men du har ingen aning. Inte ens döden kan bryta cursen. För att bryta denna förbannelse, bege dig nu mot målet och ta Stenjättens kärna. Tiden är knapp, och varje ögonblick räknas."
        """)
  time.sleep(2)



#Enemy room 1 
def enemyroom1():
 print ("Rummet är kallt och du hör raslande ljud från andra sidan.\n")
 time.sleep(2)

 print("""
                               _.--""-._
   .                         ."         ".
  / \    ,^.         /(     Y             |      )1
 /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
 |        :|    `>   '.     l_..-------.._l      .'
 |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
  \  .-' | |  `              l._       _.'
   \/    | |                   l`^^'^^'j
         | |                _   \_____/     _
         j |               l `--__)-'(__.--' |
         | |               | /`---``-----'"1 |  ,-----.
         | |               )/  `--' '---'   \'-'  ___  `-.
         | |              //  `-'  '`----'  /  ,-'   I`.  1
       _ L |_            //  `-.-.'`-----' /  /  |   |  `. 1
      '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
       `._;l _'--------_/        )-'/     :  |___.    _._./ ;
         | |                 .__ )-'\  __  \  \  I   1   / /
         `-'                /   `-\-(-'   \ \  `.|   | ,' /
                            \__  `-'    __/  `-. `---'',-'
                               )-._.-- (        `-----'
                              )(  l\ o ('..-.
                        _..--' _'-' '--'.-. |
                 __,,-'' _,,-''            \ 1
                f'. _,,-'                   \ 1
               ()--  |                       \ 1
                 \.  |                       /  1
                   \ \                      |._  |
                    \ \                     |  ()|
                     \ \                     \  /
                      ) `-.                   | |
                     // .__)                  | |
                 _ ./ /7'                      | |
                '---'                         j_| `
                                             (| |
                                              |  1
                                              |lllj
                                              |||||  """)

 print ("Ett skelet kom fram!!!\n")

def DeadEnemy1():
 print ("Raslande benen faller och en nyckel ligger på marken...\n")
 time.sleep(2)

 print ("Du plockar upp nyckeln från marken\n")
 time.sleep(2)


#Enemy room 2
def enemyroom2():
 print ("Rummet känns varmare än förut och ljud av fallande stenar hörs...\n")
 time.sleep(2)

 print ("Något börjar komma fram från den mörka grottan mot dig!\n")
 time.sleep(2)

 print("""           )        )
                  (  (|              .
              )   )\/ ( ( (
      *  (   ((  /     ))\))  (  )    )
    (     \   )\(          |  ))( )  (|
    >)     ))/   |          )/  \((  ) 1
    (     (      .        -.     V )/   )(    (
     \   /     .   \            .       \))   ))
       )(      (  | |   )            .    (  /
      )(    ,'))     \ /          \( `.    )
      (\>  ,'/__      ))            __`.  /
     ( \   | /  ___   ( \/     ___   \ | ( (
      \.)  |/  /   \__      __/   \   \|  ))
     .  \. |>  \      | __ |      /   <|  /
          )/    \____/ :..: \____/     \ <
   )   \ (|__  .      / ;: \          __| )  (
  ((    )\)  ~--_     --  --      _--~    /  ))
   \    (    |  ||               ||  |   (  /
         \.  |  ||_             _||  |  /
           > :  |  ~V+-I_I_I-+V~  |  : (.
          (  \:  T\   _     _   /T  : ./
           \  :    T^T T-+-T T^T    ;<
            \..`_       -+-       _'  )
  )            . `--=.._____..=--'. ./     """)

 print("Ett skelet kom fram!!!\n")

def DeadEnemy2():
 print("Skeletet har dött och du går till slutet av grottan.\n")
 time.sleep(2)

 print ("Framför dig finns två dörrar en åt höger och en åt vänster...\n")
 time.sleep(2)

#höger dörren
def rightdoor2():
 print("Dörren är olåst och du går igenom den.\n")

#vänster dörren
def leftdoor():
 print("Dörren är låst!\n")

#om man har nyckeln
def nyckelnvänster():
 print("Den låsta dörren öppnades och du går igenom dörren till nästa rum...\n")

#Rum med gåttan
def riddle():
  print("Rummet är upplyst av lysande crystaler runt om i grottan.\n")
  time.sleep(2)

  print("Du ser en liten staty av en drake i mitten av rummet...\n")
  time.sleep(2)

  print("Statyn börjar röra sig och dess ögon öppnas!!!\n")
  time.sleep(2)

  punkt = (". . .")
  pop_up_text(punkt, delay=0.5)

  print("Mitt namn är Draku.\n")
  time.sleep(2)

  print("Besvara min gåta rätt och jag ger dig nyckeln till den låsta dörren.\n")
  time.sleep(2)

 
  while True:
    dragonquest = input(". . . Jag lyser upp natten och styr havets vågor, men lyser inte lika starkt som min bror ?").lower()
    if dragonquest == "måne" or dragonquest == "månen":
      print("Det är rätt!")
      break
    else:
      print("Gissa igen!")

  print("Du fick en nyckel till rummet!")
  time.sleep(2)

#Tomt rum
def emptyroom():
 print("Du kliver in i det mörka rummet och tänder ett ljus.")
 time.sleep(2)

 print("Du ser två öppna dörrar en åt vänster och en åt höger...")
 time.sleep(2)

#Gamla gubbens rum
def oldman():
 print("\nDu kliver in i den vänstra dörren och kollar runt...")
 time.sleep(2)

 print("De hörs raslande ljud!\n")
 time.sleep(2)

 print ("det var länge sen jag såg en person här")
 time.sleep(2)

 print ("Ah! ber om ursäkt mitt namn är Gunnar.")
 time.sleep(2)

 print ("Jag gissar på att du är här för jättens kärna.\n")
 time.sleep(2)

 print ("Om du vill så kan jag ge dig lite information du kanske vill veta…")
 time.sleep(2)

 print ("Men! Besvara min gåta och du får veta.\n")
 time.sleep(2)
 
 print ("Vad är stort och lysser starkt i himlen?")
 time.sleep(2)

 while True:
     svar = (input("Vad gissar du på?")).lower()

     if svar == "sol" or svar == "solen":
        print("Solen, det är rätt!")
        break

     else:
         print("Det är fel, försök igen!")

 print ("Nu när du har gissat rätt så ska jag ge dig ledtråden…")
 time.sleep(2)

 print ("Vid slutet så kommer två dörrar att visas…")
 time.sleep(2)

 print ("Om du väljer dörren åt vänster så kommer glädje att falla över dig...")
 time.sleep(2)

#Boss rummet.
def boss():
 print("Du går igenom högra dörren och bemöts av en intensiv känsla...")
 time.sleep(2)

 print("Stenar och sand faller ner från väggarna!")
 time.sleep(2)

 print("PLIN PLIN PLON ...")
 time.sleep(2)

 print("Tunga steg hörs kommande mot dig...")
 time.sleep(2)

 print("kommandes från mörkret är stenjätten!")
 time.sleep(2)

 print("""                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ ,          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      .',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L1
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `1
                -,-..\  _  \  `  /  ,  / `._) _,-\`       1
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               1
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`""")


#här i mellan så slås man mått jätten
def bossdead():
 print("Du plockar upp kärnan som du letade efter. ")
 time.sleep(2)

 print("Bakom jättens kropp ser du två vägar en åt höger och en åt vänster...")
 time.sleep(2)


#vänster dörren
def lastleft():
 print("Du öppnar dörren och kliver in...")
 time.sleep(2)

 print("EN GIGANTISK STEN KULA KOMMER FALLANDES MOT DIG")
 time.sleep(2)

 print("Du försöker springa i väg men blir krossad!!!")
 time.sleep(2)

#höger dörren
def lastright():
 print("Du öppnar dörren och kliver in...")
 time.sleep(2)

 print("Framför dig finns trappor uppåt och du går upp dem...")
 time.sleep(2)

 print("... vid slutet av trapporna öppnar du en dörr och kommer ut från grottan!")
 time.sleep(2)

 print("Grattis du överlevde grottan!!!")
 time.sleep(2)