#####################################################################
#####################################################################
##                                                                 ##
##      Programm zum Lösen eines Linearen Gleichungssystems        ##
##                                                                 ##
#####################################################################
#####################################################################

# Autoren:   David Binder; Niklas Dreher
# Stand:     06.03.2025

### Variablen ###

Buffer_Zeile = [float(0), float(0), float(0), float(0), float(0)]
Status = "OK"
X1 = 0
X2 = 0
X3 = 0
X4 = 0
Counter = 0

### Programm ###
while True:
#Eingabe:

    print("Gebe dein Lineares Gleichungssystem ein:")
    Zeile1 = [float(input("A11 = ")), float(input("A12 = ")), float(input("A13 = ")), float(input("A14 = ")), float(input("A1A = "))]
    Zeile2 = [float(input("A21 = ")), float(input("A22 = ")), float(input("A23 = ")), float(input("A24 = ")), float(input("A2A = "))]
    Zeile3 = [float(input("A31 = ")), float(input("A32 = ")), float(input("A33 = ")), float(input("A34 = ")), float(input("A3A = "))]
    Zeile4 = [float(input("A41 = ")), float(input("A42 = ")), float(input("A34 = ")), float(input("A44 = ")), float(input("A4A = "))]
    
    # Rechner:
    
    if (Zeile1[0] != 0):
            
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
    
            else:
                Status = "Fehler"
                
            
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
                
            else:
                Status = "Fehler"
    
            
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
                Status = "Fehler"
    else:
        Status = "Fehler" 
    
    if (Zeile2[1] != 0):
            
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
    
            else:
                Status = "Fehler"
                
            
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
                Status = "Fehler"
    
    else: 
        Status = "Fehler"
    
    if (Zeile3[2] != 0):
    
        if (Zeile4[2] != 0):
        
            Buffer1 = Zeile3[2]
            Buffer2 = Zeile4[2]
            Buffer_Zeile = Zeile3
            Buffer_Zeile = [i * Buffer2 for i in Buffer_Zeile]
            Zeile4 = [i * Buffer1 for i in Zeile4]
    
            if ((Buffer_Zeile[2] < 0) and (Zeile4[2] < 0)) or ((Buffer_Zeile[2] > 0) and (Zeile4[2] > 0)):
                for i in range(5):
                    Zeile4[Counter] -= Buffer_Zeile[Counter]
    
            elif ((Buffer_Zeile[2] < 0) and (Zeile4[2] > 0)) or ((Buffer_Zeile[2] > 0) and (Zeile4[2] < 0)):
                for i in range(5):
                    Zeile4[i] += Buffer_Zeile[i]
    
            else:
                Status = "Fehler"
    
    else: 
        Status = "Fehler"
    
    # if (A31 == 0) and (A32 == 0) and (A21 == 0):
    #     X3 = (A3A / A33)
    #     X2 = ((A2A - (A23*X3)) / A22)
    #     X1 = ((A1A - (A13 * X3) - (A12 * X2)) / A11)
    # else:
    #     Status = "Fehler"
    
    # Ausgabe:
    
    print("Dreiecksmatrix:")
    print(Zeile1)
    print(Zeile2)
    print(Zeile3)
    print(Zeile4)
    
    print("Status:", Status)
    print("Dein Ergebnis lautet:")
    print("X1 = ", X1)
    print("X2 = ", X2)
    print("X3 = ", X3)
    print("X4 = ", X4)
    