inGame = True
rooms = []
items = []
switches_value = "0000000"
chances = 3
lion_eat = False
code_solution = "6473"
code_tip = ""
win = False
print("""Üdvözöllek a szabadulószobámban!
Egy szobában vagy, és 14 ajtó van körülötted.
Az egyik az ajtó a kiút.
Keresd meg a helyes ajtót, és add meg a 4 jegyű jelszót.
A számjegyek megtalálhatóak a többi 13 ajtó mögött.
Keress meg minden számjegyet, és szabadulj ki!""")

while inGame:
    room_number = input("Melyik ajtót akarod kinyitni (0-13)?\n")
    #--------- -1 --------------
    if room_number == "-1":
        print("Your story so far:")
        for i in range(len(items)):
            print("In room", rooms[i], ":", items[i])

    # --------- 0 --------------
    if room_number == "0":
        if "kulcs" not in items:
            print("""Egy sötét szobába érkeztél. Végigmész a falon, keresve az egyik kapcsolót...
            Végül sikerül felkapcsolnod a villanyt, és rájössz, hogy a szoba üres. Egyetlen villanykörte 
            lóg a szoba közepén. Valami furcsaságot érzel benne. Kicsavarod a körtét, majd összetöröd. 
            Mostmár újra sötét van, és a törmelékek között kell kutatnod. Megvágod magad, de megtalálsz 
            egy kulcsot a földön. Beleteszed a zsebedbe és elhagyod a szobát.""")
            items.append("kulcs")
            rooms.append(room_number)
            if "doboz" in items:
                print("Várj. Már van egy dobozod amihez kell egy kulcs.")
                print("""Kinyitod a dobozt és látsz egy kis hűtőt, amibe van egy kis nyers hús. Talán ezt még valaki megeheti...""")
                items.append("hús")
                rooms.append(room_number)
        else:
            print("Már begyűjtötted a kulcsot ami itt található, nincs itt semmi más.")
    # --------- 1 --------------
    if room_number == "1":
        print("""Egy ijesztő festményt látsz a falon. Bal oldalon egy oroszlán áll széken és cseréli ki a tört villanykörtét, 
        míg jobb oldalon egy bohóc áll egy táblával szemben, és próbálja megoldani a bonyolult egyenletet.""")
        if "painting" not in items:
            items.append("festmény")
            rooms.append(room_number)

    # --------- 2 --------------
    if room_number == "2":
        if "1010011" not in items:
            print("Egy sor számot látsz a falon. Talán valamihez jó: 1010011.")
            items.append("1010011")
            rooms.append(room_number)
        else:
            print("Ez ugyan az a kód, amit az előbb láttál.")

    # --------- 3 --------------
    if room_number == "3":
        if "cat video" not in items:
            print("""Egy videót vetítenek a falon. Egy kis macska rohan be egy konyhába, majd egy tálból eszik.""")
            items.append("macskás videó")
            rooms.append(room_number)
        else:
            print("""Egy videót vetítenek a falon. Egy kis macska rohan be egy konyhába, majd egy tálból eszik.""")

    # --------- 4 ---------------------6-os szám
    if room_number == "4":
        if "7 villanykörte" not in items:
            print("""Belépsz a szobába, és egy üresnek tűnő táblát látsz a falon, felette 7 villanykörte található. 
            Sajnos a szobában nem találsz kapcsolókat. Talán máshol megtalálod őket. """)
            items.append("7 villanykörte")
            rooms.append(room_number)
        else:
            if switches_value == "1010011":
                print("A 6-os szám lassan előtűnik a táblán")
                if "villanykörte 6-os számmal" not in items:
                    items.append("villanykörte 6-os számmal")
                    rooms.append(room_number)

    # --------- 5 --------------
    if room_number == "5":
        if "egyenlet" not in items:
            print("""Egy egyenletet látsz a falon. x = 10111 - 10001. 
            Hogyan lehet az x egyjegyű szám?""")
            items.append("egyenlet")
            rooms.append(room_number)
        else:
            print("Az egyenlet: x = 10111 - 10001")

    # --------- 6 ----------------------4-es szám
    if room_number == "6":
        if room_number not in rooms:
            print("""Egy oroszlán fekszik a földön és ránéz rád. A falon valami van az oroszlán mögött, 
            de nem tudod elolvasni.""")
            items.append("oroszlán")
            rooms.append(room_number)
            lion = input("El akarod lökni az oroszlánt a faltól? (igen/nem)")
            if lion == "igen":
                if "hús" not in items:
                    print("""Az oroszlánt a kezeddel próbálod eltolni. Az oroszlán kissé megharagszik és megesz téged. =( """)
                    inGame = False
                    lion_eat = True
                else:
                    print("""A nyers ételt a sarokba dobod, az oroszlán utánaugrik. A falon a 4-es szám van.""")
                    items.append("4-es szám az oroszlán mögött")
                    rooms.append(room_number)
            else:
                print("Talán majd legközelebb.")

        else:
            print("Az oroszlán még mindik téged néz a falnál.")
            lion = input("El akarod lökni az oroszlánt a faltól? (igen/nem)")
            if lion == "igen":
                if "hús" not in items:
                    print("""Az oroszlánt a kezeddel próbálod eltolni. Az oroszlán kissé megharagszik és megesz téged. =( """)
                    inGame = False
                    lion_eat = True
                else:
                    print("""A nyers ételt a sarokba dobod, az oroszlán utánaugrik. A falon a 4-es szám van.""")
                    items.append("4-es szám az oroszlán mögött")
                    rooms.append(room_number)
            else:
                print("Talán majd legközelebb.")

    # --------- 7 ------------------------7-es szám
    if room_number == "7":
        if room_number not in rooms:
            print("""Egy fejszét találsz a padlón, aminek a nyelére rá van írva a 7-es szám. 
            Legalább most van valami a kezedben.""")
            items.append("balta")
            rooms.append(room_number)
        else:
            print("A szoba üres.")

    # --------- 8 --------------
    if room_number == "8":
        print("""Egy festményt látsz a falon. Egy égő épület van rajta, 
        és két bohóc mászik fel egy létrán egy kérdőjeles ablakhoz. 
        Az egyik bohóc egy macskát tart a kezében.""")
        if room_number not in rooms:
            items.append("festmény bohóccal és macskával")
            rooms.append(room_number)
    # --------- 9 --------------
    if room_number == "9":
        print("""Ott egy darab papír egy üzenettel rajta: binárisból decimálisba.""")
        if room_number not in rooms:
            items.append("papír üzenete: binárisból decimálisba.")
            rooms.append(room_number)
    # --------- 10 --------------
    if room_number == "10":
        print("""Ez a szoba vezet a szabad világba. Látsz egy másik ajtót, ami lakatolt. 
        A lakatot négyjegyű kóddal lehet kinyitni. Az ajtó mellett üzenet van, 
        amely szerint csak három próbálkozásod van. Azután az ajtó örökre bezárul.""")

        if room_number not in rooms:
            items.append("kijárat")
            rooms.append(room_number)
        guess = input("Meg akarod tippelni a jelszót? (igen/nem)")
        if guess == "igen":
            print("Van még ", chances, "esélyed.")
            code_tip = input("Milyen jelszavat tippeltél??\n")
            if code_tip == code_solution:
                inGame = False
                win = True
            else:
                chances -= 1
                if chances == 0:
                    inGame = False
        else:
            print("Talán majd legközelebb.")
    # --------- 11 ---------------------3-as szám
    if room_number == "11":
        print("""Ott egy bohóc akinek van 3 lufi a kezében.""")
        if room_number not in rooms:
            items.append("bohóc 3 lufival")
            rooms.append(room_number)
    # --------- 12 --------------
    if room_number == "12":
        print("Látsz 7 kapcsolót a falon.")
        if room_number not in rooms:
            items.append("7 kapcsoló")
            rooms.append(room_number)
        switches_value = input("Hogy akarod felkapcsolni a kapcsolókat? (0/1)")
        if len(switches_value) == 7:
            print("Remélem így működik.")
        else:
            print("Pontosan 7 számmal kéne próbálkozni.")
    # --------- 13 --------------
    if room_number == "13":
        if room_number not in rooms:
            items.append("fa tábla")
            rooms.append(room_number)
        print("""Ott egy fa tábla a falon. """)
        if "balta" in items:
            print("""Felhasználod a baltát amit a földön találtál egy másik szobába, és eltöröd a fa darabot. 
            A fa darab mögött találsz egy kis dobozt. Talán egy kulcsal ki lehet nyitni.""")
            items.append("doboz")
            rooms.append(room_number)
            if "kulcs" in items:
                print("""Kinyitod a dobozt és találsz benne egy hűtőt amibe egy nyers hús van.""")
                items.append("hús")
                rooms.append(room_number)

if lion_eat:
    print("JÁTÉK VÉGE")
if win:
    print("Gratulálok, kijutottál!!")
if chances == 0:
    print("Megpróbáltad kinyitni az ajtót 3 alkalommal, most pedig örökre itt maradsz. JÁTÉK VÉGE")