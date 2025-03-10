#####################################################################
#####################################################################
##                                                                 ##
##      Programm zum Lösen eines Linearen Gleichungssystems        ##
##                                                                 ##
#####################################################################
#####################################################################

# Autoren:   David Binder; Niklas Dreher
# Stand:     10.03.2025

### Variablen ###

Buffer_Zeile = [float(0), float(0), float(0), float(0), float(0)]
Status = "OK"
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

    # Rechner:
    
    while(Null_Status == 0 and Error == False):
    
        if (Zeile1[0] != 0):
        
            Null_Status = 1
    
            if (Zeile2[0] != 0):
            
                Buffer1 = Zeile1[0]
                Buffer2 = Zeile2[0]
                Buffer_Zeile = Zeile1
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                Zeile2 = [i * Buffer1 for i in Zeile2]
    
                if ((Buffer_Zeile[0] < 0) and (Zeile2[0] < 0)) or ((Buffer_Zeile[0] > 0) and (Zeile2[0] > 0)):
                    for i in range(5):
                        Zeile2[i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[0] < 0) and (Zeile2[0] > 0)) or ((Buffer_Zeile[0] > 0) and (Zeile2[0] < 0)):
                    for i in range(5):
                        Zeile2[i] += Buffer_Zeile[i]
    
            if (Zeile3[0] != 0):
            
                Buffer1 = Zeile1[0]
                Buffer2 = Zeile3[0]
                Buffer_Zeile = Zeile1
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                Zeile3 = [i * Buffer1 for i in Zeile3]
    
                if ((Buffer_Zeile[0] < 0) and (Zeile3[0] < 0)) or ((Buffer_Zeile[0] > 0) and (Zeile3[0] > 0)):
                    for i in range(5):
                        Zeile3[i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[0] < 0) and (Zeile3[0] > 0)) or ((Buffer_Zeile[0] > 0) and (Zeile3[0] < 0)):
                    for i in range(5):
                        Zeile3[i] += Buffer_Zeile[i]
    
            if (Zeile4[0] != 0):
            
                Buffer1 = Zeile1[0]
                Buffer2 = Zeile4[0]
                Buffer_Zeile = Zeile1
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                Zeile4 = [i * Buffer1 for i in Zeile4]
    
                if ((Buffer_Zeile[0] < 0) and (Zeile4[0] < 0)) or ((Buffer_Zeile[0] > 0) and (Zeile4[0] > 0)):
                    for i in range(5):
                        Zeile4[i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[0] < 0) and (Zeile4[0] > 0)) or ((Buffer_Zeile[0] > 0) and (Zeile4[0] < 0)):
                    for i in range(5):
                        Zeile4[i] += Buffer_Zeile[i]
    
        else:
            if Fehler_Counter == 0:
                Buffer_Zeile = Zeile1
                Zeile1 = Zeile2
                Zeile2 = Buffer_Zeile
                Fehler_Counter += 1
            elif Fehler_Counter == 1:
                Buffer_Zeile = Zeile1
                Zeile1 = Zeile3
                Zeile3 = Buffer_Zeile
                Fehler_Counter += 1
            elif Fehler_Counter == 2:
                Buffer_Zeile = Zeile1
                Zeile1 = Zeile4
                Zeile4 = Buffer_Zeile
                Fehler_Counter += 1
            else:
                Status = "Nullspalte"
                Null_Status = 1
    
    Null_Status = 0
    Fehler_Counter = 0
    
    while (Null_Status == 0 and Error == False):
    
        if (Zeile2[1] != 0):
            Null_Status = 1
            if (Zeile3[1] != 0):
            
                Buffer1 = Zeile2[1]
                Buffer2 = Zeile3[1]
                Buffer_Zeile = Zeile2
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                Zeile3 = [i * Buffer1 for i in Zeile3]
    
                if ((Buffer_Zeile[1] < 0) and (Zeile3[1] < 0)) or ((Buffer_Zeile[1] > 0) and (Zeile3[1] > 0)):
                    for i in range(5):
                        Zeile3[i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[1] < 0) and (Zeile3[1] > 0)) or ((Buffer_Zeile[1] > 0) and (Zeile3[1] < 0)):
                    for i in range(5):
                        Zeile3[i] += Buffer_Zeile[i]

            if (Zeile4[1] != 0):
            
                Buffer1 = Zeile2[1]
                Buffer2 = Zeile4[1]
                Buffer_Zeile = Zeile2
                Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
                Zeile4 = [i * Buffer1 for i in Zeile4]
    
                if ((Buffer_Zeile[1] < 0) and (Zeile4[1] < 0)) or ((Buffer_Zeile[1] > 0) and (Zeile4[1] > 0)):
                    for i in range(5):
                        Zeile4[i] -= Buffer_Zeile[i]
    
                elif ((Buffer_Zeile[1] < 0) and (Zeile4[1] > 0)) or ((Buffer_Zeile[1] > 0) and (Zeile4[1] < 0)):
                    for i in range(5):
                        Zeile4[i] += Buffer_Zeile[i]
    
        else:
            if Fehler_Counter == 0:
                Buffer_Zeile = Zeile2
                Zeile2 = Zeile3
                Zeile3 = Buffer_Zeile
                Fehler_Counter += 1
            elif Fehler_Counter == 1:
                Buffer_Zeile = Zeile2
                Zeile2 = Zeile4
                Zeile4 = Buffer_Zeile
                Fehler_Counter += 1
            else:
                Status = "Nullspalte"
                Null_Status = 1
    
    Null_Status = 0
    Fehler_Counter = 0
    
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
    