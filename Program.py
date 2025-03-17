#####################################################################
#####################################################################
##                                                                 ##
##      Programm zum Lösen eines Linearen Gleichungssystems        ##
##                                                                 ##
#####################################################################
#####################################################################

# Autoren:   David Binder; Niklas Dreher
# Stand:     17.03.2025

### Variablen ###

Buffer_Zeile = [float(0), float(0), float(0), float(0), float(0)]   #Bufferzeile später zum Tauschen von Zeilen verwendet 
Status = "OK"
X1 = 0
X2 = 0
X3 = 0
X4 = 0
Null_Status = 0                                                     #Wird 1 wenn an der 1.Stelle einer Zeile eine Null steht
Fehler_Counter = 0
Error = False

### Programm ###

while True:
    
    # Eingabe:
    
    Error = False
    Status = "OK"

    try:
        print("Gebe dein Lineares Gleichungssystem im folgenden Format ein:")
        print("A11 A12 A13 A14 | A1A")
        print("A21 A22 A23 A24 | A2A")
        print("A31 A32 A33 A34 | A3A")
        print("A41 A42 A43 A44 | A4A")
        
        Zeile1 = [float(input("A11 = ")), float(input("A12 = ")), float(input("A13 = ")), float(input("A14 = ")), float(input("A1A = "))]
        Zeile2 = [float(input("A21 = ")), float(input("A22 = ")), float(input("A23 = ")), float(input("A24 = ")), float(input("A2A = "))]
        Zeile3 = [float(input("A31 = ")), float(input("A32 = ")), float(input("A33 = ")), float(input("A34 = ")), float(input("A3A = "))]
        Zeile4 = [float(input("A41 = ")), float(input("A42 = ")), float(input("A43 = ")), float(input("A44 = ")), float(input("A4A = "))]
    except ValueError:
        Error = True
        Status = "Eingabefehler"

    # LGS-Liste, Lösungs-Liste und Variablen-Namen-Liste an Variablen-Anzahl anpassen:

    LGS = [[0]]

    for i in range(Array_Rang - 1):

        LGS.append([0])

    for i in range(Array_Rang):

        for a in range(Array_Rang):

            LGS[i].append(0)

    Loesung = [float(0)]

    for i in range(Array_Rang - 1):

        Loesung.append(float(0))

    Variablen = ["X"]

    for i in range(Array_Rang):

        Variablen.append("X")

    if (Error == False):

        # Eingabe der Variablen-Namen:

        print("Gebe hier deine Variablen-Namen ein: \n")

        try:

            for i in range(Array_Rang):

                print(f"Variable {i + 1}:")
                Variablen[i] = str(input())

        except ValueError:

            Error = True
            Status = "Eingabefehler"

        Variablen[Array_Rang] = "Lösung"

        # Eingabe der Werte:

        print("\nGebe hier deine Werte ein: \n")

        try:

            for i in range(Array_Rang):

                for a in range((Array_Rang + 1)):

                    print(f"Zeile {i + 1}, {Variablen[a]}:")
                    
                    LGS[i][a] = float(input())

        except ValueError:

            Error = True
            Status = "Eingabefehler"

    # Überprüfung der eingegebenen Werte:

    if(Error == False):

        print("\nHier ist dein eingegebenes LGS: \n")

        for Zeilen in LGS:

            print(Zeilen)

        LGS_korrektur = str(input("\nIst das LGS korrekt eingegeben? (Ja/Nein): "))

        if(LGS_korrektur != "Ja"):

            Error = True
            Status = "Eingabefehler"

    print("\n")

    ### Rechner:

    # Berechnung der Dreiecksmatrix vom Format:
    # (X, X, X | Lösung)
    # (0, X, X | Lösung)
    # (0, 0, X | Lösung)

    if(Error == False):
    
        for a in range(Array_Rang):

            # Vertauschung der Zeilen bei Null im ersten Faktor:
            # (0, X, X | Lösung)
            # (X, X, X | Lösung)
            # (X, X, X | Lösung)

            if (LGS[a][a] == 0):

                try:

                    for c in range(1, 1 + Array_Rang - a):

                        if (LGS[a][a] == 0):

                            Buffer_Zeile = LGS[a]
                            LGS[a] = LGS[a + c]
                            LGS[a + c] = Buffer_Zeile 

                except IndexError:

                    Error = True
                    Status = "Nullspalte"
                    break

            # Verechnung jeweils zweier Zeilen um Null in der zweiten Zeile, die verrechnet wird, zu bekommen:
            # (X, X, X | Lösung)
            # (0, X, X | Lösung)
            # (X, X, X | Lösung) usw.
                
            for b in range(a, Array_Rang - 1):

                if (LGS[b + 1][a] != 0):

                    Buffer1 = LGS[a][a]
                    Buffer2 = LGS[b + 1][a]
                    Buffer_Zeile = LGS[a]
                    Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                    LGS[b + 1] = [i * Buffer1 for i in LGS[b + 1]]

                    if ((Buffer_Zeile[a] < 0) and (LGS[b + 1][a] < 0)) or ((Buffer_Zeile[a] > 0) and (LGS[b + 1][a] > 0)):

                        for i in range(Array_Rang + 1):

                            LGS[b + 1][i] -= Buffer_Zeile[i]

                    elif ((Buffer_Zeile[a] < 0) and (LGS[b + 1][a] > 0)) or ((Buffer_Zeile[a] > 0) and (LGS[b + 1][a] < 0)):

                        for i in range(Array_Rang + 1):

                            LGS[b + 1][i] += Buffer_Zeile[i]

    # Berechnung der Lösung der Variablen:

    if (Error == False):

        if (Zeile3[2] != 0): 
    
            if (Zeile4[2] != 0):
            
                Buffer1 = Zeile3[2]
                Buffer2 = Zeile4[2]
                Buffer_Zeile = Zeile3
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                Zeile4 = [i * Buffer1 for i in Zeile4]

                if ((Buffer_Zeile[2] < 0) and (Zeile4[2] < 0)) or ((Buffer_Zeile[2] > 0) and (Zeile4[2] > 0)):
                    for i in range(5):
                        Zeile4[i] -= Buffer_Zeile[i]

                elif ((Buffer_Zeile[2] < 0) and (Zeile4[2] > 0)) or ((Buffer_Zeile[2] > 0) and (Zeile4[2] < 0)):
                    for i in range(5):
                        Zeile4[i] += Buffer_Zeile[i]

        else: 
            Buffer_Zeile = Zeile3
            Zeile3 = Zeile4
            Zeile4 = Buffer_Zeile
    
    if (Status == "OK"):
        try:
            X4 = (Zeile4[4] / Zeile4[3])
            X3 = ((Zeile3[4] - (Zeile3[3] * X4)) / Zeile3[2])
            X2 = ((Zeile2[4] - (Zeile2[3] * X4) - (Zeile2[2] * X3)) / Zeile2[1])
            X1 = ((Zeile1[4] - (Zeile1[3] * X4) - (Zeile1[2] * X3) - (Zeile1[1]) * X2) / Zeile1[0])
        except ZeroDivisionError:
            Status = "Nullzeile"

    # Ausgabe:

    if Error == False:
    
        print("Dreiecksmatrix:")
        print(Zeile1)
        print(Zeile2)
        print(Zeile3)
        print(Zeile4)

        print("Status:", Status)

        if Status == "OK":

            print("Dein Ergebnis lautet:")
            print("X1 = ", X1)
            print("X2 = ", X2)
            print("X3 = ", X3)
            print("X4 = ", X4)

    else:
        
        print("Es gab einen Fehler, bitte gebe dein LGS erneut ein")
    