#####################################################################
#####################################################################
##                                                                 ##
##      Programm zum Lösen eines Linearen Gleichungssystems        ##
##                                                                 ##
#####################################################################
#####################################################################

# Autoren:   David Binder; Niklas Dreher
# Stand:     13.03.2025

### Variablen ###

Buffer_Zeile = [float(0), float(0), float(0), float(0), float(0)]
Status = "OK"
Array_Rang = 0
Null_Status = 0
Fehler_Counter = 0
Error = False
Buffer_Loesung = float(0)

### Programm ###

while True:
    
    ### Eingabe:
    
    Error = False
    Status = "OK"

    if (Error == False):

        try:

            Array_Rang = int(input("Wie viele Variablen hat dein LGS?"))

        except ValueError:

            Error = True
            Status = "Eingabefehler"

    LGS = [[0]]

    for i in range(Array_Rang - 1):
        LGS.append([0])

    for i in range(Array_Rang):
        for a in range(Array_Rang):
            LGS[i].append(0)

    Loesung = [float(0)]

    for i in range(Array_Rang - 1):
        Loesung.append(float(0))

    if (Error == False):

        print("Gebe hier deine Werte ein: \n(Die letzte Variable pro Zeile ist der Ergebnis-Wert) \n")

        try:

            for i in range(Array_Rang):

                for a in range((Array_Rang + 1)):

                    print("Zeile", i + 1 ,", Variable", a + 1, ":")
                    LGS[i][a] = float(input())

        except ValueError:

                Error = True
                Status = "Eingabefehler"

    for Zeilen in LGS:
        print(Zeilen)

    for Variablen in Loesung:
        print(Variablen)

    ### Rechner:
    
    for a in range(0, Array_Rang):

        if (LGS[a][a] != 0):

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

    if (Error == False):
    
        print("Dreiecksmatrix: \n")
        for Zeilen in LGS:
            print(Zeilen)

        print("Status:", Status, "\n")

        if Status == "OK":

            print("Dein Ergebnis lautet: \n")

            for i in range(Array_Rang):

                print("Variable", (i + 1), "= ", Loesung[i], "\n")

    else:
        
        print("Es gab folgenden Fehler:", Status, "\nBitte gebe dein LGS erneut ein \n")
    