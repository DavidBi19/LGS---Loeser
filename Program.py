#####################################################################
#####################################################################
##                                                                 ##
##      Programm zum Lösen eines Linearen Gleichungssystems        ##
##                                                                 ##
#####################################################################
#####################################################################

# Autoren:   David Binder; Niklas Dreher
# Stand:     13.03.2025

### Bibliotheken ###

import math

### Variablen ###

Buffer_Zeile = [float(0), float(0), float(0), float(0), float(0)]
Status = "OK"
Array_Rang = 0
X1 = 0
X2 = 0
X3 = 0
X4 = 0
Null_Status = 0
Fehler_Counter = 0
Error = False

### Programm ###

while True:
    
    # Eingabe:
    
    Error = False
    Status = "OK"

    if (Error == False):

        try:

            Array_Rang = int(input("Wie viele Variablen hat dein LGS?"))

        except ValueError:

            Error = True
            Status = "Eingabefehler"

    LGS = [[float(0), float(0), float(0), float(0), float(0)], [float(0), float(0), float(0), float(0), float(0)], [float(0), float(0), float(0), float(0), float(0)], [float(0), float(0), float(0), float(0), float(0)]]
    
    # if (Error == False):

    #     try:

    #         print("Gebe dein Lineares Gleichungssystem im folgenden Format ein: \n")
    #         print("A11 A12 A13 A14 | A1A \n" "A21 A22 A23 A24 | A2A \n" "A31 A32 A33 A34 | A3A \n" "A41 A42 A43 A44 | A4A \n")

    #         Zeile1 = [float(input("A11 = ")), float(input("A12 = ")), float(input("A13 = ")), float(input("A14 = ")), float(input("A1A = "))]
    #         Zeile2 = [float(input("A21 = ")), float(input("A22 = ")), float(input("A23 = ")), float(input("A24 = ")), float(input("A2A = "))]
    #         Zeile3 = [float(input("A31 = ")), float(input("A32 = ")), float(input("A33 = ")), float(input("A34 = ")), float(input("A3A = "))]
    #         Zeile4 = [float(input("A41 = ")), float(input("A42 = ")), float(input("A43 = ")), float(input("A44 = ")), float(input("A4A = "))]

    #     except ValueError:

    #         Error = True
    #         Status = "Eingabefehler"

    try:

        if (Error == False):

            for i in range(Array_Rang):

                for a in range((Array_Rang + 1)):

                    print("Zeile", i+1 ,", Spalte", a+1, ":")
                    LGS[i][a] = [float(input())]
    
    except ValueError:

            Error = True
            Status = "Eingabefehler"

    for Zeilen in LGS:
        print(Zeilen)

    # Error = True
    # Status = "Test"

    # Rechner:
    
    while(Null_Status == 0 and Error == False):
    
        if (LGS[0][0] != 0):
        
            Null_Status = 1
    
            if (LGS[1][0] != 0):
            
                Buffer1 = LGS[0][0]
                Buffer2 = LGS[1][0]
                Buffer_Zeile = LGS[0]
                Buffer_Zeile = [float(i) * float(Buffer2) for i in Buffer_Zeile]
                LGS[1] = [float(i) * float(Buffer1) for i in LGS[1]]
    
                if ((Buffer_Zeile[0] < 0) and (LGS[1][0] < 0)) or ((Buffer_Zeile[0] > 0) and (LGS[1][0] > 0)):
                    for i in range(5):
                        LGS[1][i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[0] < 0) and (LGS[1][0] > 0)) or ((Buffer_Zeile[0] > 0) and (LGS[1][0] < 0)):
                    for i in range(5):
                        LGS[1][i] += Buffer_Zeile[i]
    
            if (LGS[2][0] != 0):
            
                Buffer1 = LGS[0][0]
                Buffer2 = LGS[2][0]
                Buffer_Zeile = LGS[0]
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                LGS[2] = [i * Buffer1 for i in LGS[2]]
    
                if ((Buffer_Zeile[0] < 0) and (LGS[2][0] < 0)) or ((Buffer_Zeile[0] > 0) and (LGS[2][0] > 0)):
                    for i in range(5):
                        LGS[2][i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[0] < 0) and (LGS[2][0] > 0)) or ((Buffer_Zeile[0] > 0) and (LGS[2][0] < 0)):
                    for i in range(5):
                        LGS[2][i] += Buffer_Zeile[i]
    
            if (LGS[3][0] != 0):
            
                Buffer1 = LGS[0][0]
                Buffer2 = LGS[3][0]
                Buffer_Zeile = LGS[0]
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                LGS[3] = [i * Buffer1 for i in LGS[3]]
    
                if ((Buffer_Zeile[0] < 0) and (LGS[3][0] < 0)) or ((Buffer_Zeile[0] > 0) and (LGS[3][0] > 0)):
                    for i in range(5):
                        LGS[3][i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[0] < 0) and (LGS[3][0] > 0)) or ((Buffer_Zeile[0] > 0) and (LGS[3][0] < 0)):
                    for i in range(5):
                        LGS[3][i] += Buffer_Zeile[i]
    
        else:
            if Fehler_Counter == 0:
                Buffer_Zeile = LGS[0]
                LGS[0] = LGS[1]
                LGS[1] = Buffer_Zeile
                Fehler_Counter += 1
            elif Fehler_Counter == 1:
                Buffer_Zeile = LGS[0]
                LGS[0] = LGS[2]
                LGS[2] = Buffer_Zeile
                Fehler_Counter += 1
            elif Fehler_Counter == 2:
                Buffer_Zeile = LGS[0]
                LGS[0] = LGS[3]
                LGS[3] = Buffer_Zeile
                Fehler_Counter += 1
            else:
                Status = "Nullspalte"
                Error = True
    
    Null_Status = 0
    Fehler_Counter = 0
    
    while (Null_Status == 0 and Error == False):
    
        if (LGS[1][1] != 0):
            Null_Status = 1
            if (LGS[2][1] != 0):
            
                Buffer1 = LGS[1][1]
                Buffer2 = LGS[2][1]
                Buffer_Zeile = LGS[1]
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                LGS[2] = [i * Buffer1 for i in LGS[2]]
    
                if ((Buffer_Zeile[1] < 0) and (LGS[2][1] < 0)) or ((Buffer_Zeile[1] > 0) and (LGS[2][1] > 0)):
                    for i in range(5):
                        LGS[2][i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[1] < 0) and (LGS[2][1] > 0)) or ((Buffer_Zeile[1] > 0) and (LGS[2][1] < 0)):
                    for i in range(5):
                        LGS[2][i] += Buffer_Zeile[i]

            if (LGS[3][1] != 0):
            
                Buffer1 = LGS[1][1]
                Buffer2 = LGS[3][1]
                Buffer_Zeile = LGS[1]
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                LGS[3] = [i * Buffer1 for i in LGS[3]]
    
                if ((Buffer_Zeile[1] < 0) and (LGS[3][1] < 0)) or ((Buffer_Zeile[1] > 0) and (LGS[3][1] > 0)):
                    for i in range(5):
                        LGS[3][i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[1] < 0) and (LGS[3][1] > 0)) or ((Buffer_Zeile[1] > 0) and (LGS[3][1] < 0)):
                    for i in range(5):
                        LGS[3][i] += Buffer_Zeile[i]
    
        else:
            if Fehler_Counter == 0:
                Buffer_Zeile = LGS[1]
                LGS[1] = LGS[2]
                LGS[2] = Buffer_Zeile
                Fehler_Counter += 1
            elif Fehler_Counter == 1:
                Buffer_Zeile = LGS[1]
                LGS[1] = LGS[3]
                LGS[3] = Buffer_Zeile
                Fehler_Counter += 1
            else:
                Status = "Nullspalte"
                Error = True
    
    Null_Status = 0
    Fehler_Counter = 0
    
    if (Error == False):

        if (LGS[2][2] != 0): 
    
            if (LGS[3][2] != 0):
            
                Buffer1 = LGS[2][2]
                Buffer2 = LGS[3][2]
                Buffer_Zeile = LGS[2]
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                LGS[3] = [i * Buffer1 for i in LGS[3]]

                if ((Buffer_Zeile[2] < 0) and (LGS[3][2] < 0)) or ((Buffer_Zeile[2] > 0) and (LGS[3][2] > 0)):
                    for i in range(5):
                        LGS[3][i] -= Buffer_Zeile[i]

                elif ((Buffer_Zeile[2] < 0) and (LGS[3][2] > 0)) or ((Buffer_Zeile[2] > 0) and (LGS[3][2] < 0)):
                    for i in range(5):
                        LGS[3][i] += Buffer_Zeile[i]

        else: 
            Buffer_Zeile = LGS[2]
            LGS[2] = LGS[3]
            LGS[3] = Buffer_Zeile
    
    if (Error == False):
        try:
            X4 = (LGS[3][4] / LGS[3][3])
            X3 = ((LGS[2][4] - (LGS[2][3] * X4)) / LGS[2][2])
            X2 = ((LGS[1][4] - (LGS[1][3] * X4) - (LGS[1][2] * X3)) / LGS[1][1])
            X1 = ((LGS[0][4] - (LGS[0][3] * X4) - (LGS[0][2] * X3) - (LGS[0][1]) * X2) / LGS[0][0])
        except ZeroDivisionError:
            Status = "Nullzeile"

    # Ausgabe:

    if (Error == False):
    
        print("Dreiecksmatrix: \n")
        for Zeilen in LGS:
            print(Zeilen)

        print("Status:", Status, "\n")

        if Status == "OK":

            print("Dein Ergebnis lautet: \n")
            print("X1 = ", X1)
            print("X2 = ", X2)
            print("X3 = ", X3)
            print("X4 = ", X4, "\n")

    else:
        
        print("Es gab folgenden Fehler:", Status, "\nBitte gebe dein LGS erneut ein \n")
    