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

Buffer_Zeile = [float(0), float(0), float(0), float(0), float(0)]
Status = "OK"
Array_Rang = 0
Error = False
Buffer_Loesung = float(0)
LGS_korrektur = "Ja"

### Programm ###

while True:
    
    ### Eingabe:
    
    Error = False
    Status = "OK"

    # Anzahl der Variablen festlegen:

    try:

        Array_Rang = int(input("Wie viele Variablen hat dein LGS: "))

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

        try:

            for i in range((Array_Rang - 1), -1, -1):

                Buffer_Loesung = LGS[i][Array_Rang]
                
                for a in range(Array_Rang):

                    Buffer_Loesung -= ((LGS[i][a]) * (Loesung[a]))

                Loesung[i] = Buffer_Loesung / LGS[i][i]

        except ZeroDivisionError:

            Error = True
            Status = "Nullzeile"

    ### Ausgabe:

    # Ausgabe bei korrekter Berechnung:

    if (Error == False):
    
        print("Dreiecksmatrix: \n")

        for Zeilen in LGS:

            print(Zeilen)

        print("\nStatus:", Status, "\n")

        if Status == "OK":

            print("Dein Ergebnis lautet: \n")

            for i in range(Array_Rang):

                print(f"{Variablen[i]} = {Loesung[i]}\n")

    # Ausgabe bei Fehler:

    else:
        
        print(f"Es gab folgenden Fehler: {Status} \nBitte gebe dein LGS erneut ein \n")

### Programm Ende ###    