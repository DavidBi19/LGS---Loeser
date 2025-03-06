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

print("Gebe dein Lineares Gleichungssystem ein:")
A11 = int(input("A11 =" ))
A12 = int(input("A12 =" ))
A13 = int(input("A13 =" ))
A1A = int(input("A1A =" ))
A21 = int(input("A21 =" ))
A22 = int(input("A22 =" ))
A23 = int(input("A23 =" ))
A2A = int(input("A2A =" ))
A31 = int(input("A31 =" ))
A32 = int(input("A32 =" ))
A33 = int(input("A33 =" ))
A3A = int(input("A3A =" ))
Buffer = 0
Status = "OK"

### Programm ###

# Rechner:

if(A11 != 0) and (A21 != 0):
    Buffer = A11
    A11 *= A21
    A12 *= A21
    A13 *= A21
    A1A *= A21
    A21 *= Buffer
    A22 *= Buffer
    A23 *= Buffer
    A2A *= Buffer
else:
    Status = "Fehler"

if((A11 > 0) and (A21 > 0)) or ((A11 < 0) and (A21 < 0)):
    A21 -= A11
    A22 -= A12
    A23 -= A13
    A2A -= A1A
elif((A11 > 0) and (A21 < 0)) or ((A11 < 0) and (A21 > 0)):
    A21 += A11
    A22 += A12
    A23 += A13
    A2A += A1A
else:
    Status = "Fehler"

if(A11 != 0) and (A31 != 0):
    Buffer = A11
    A11 *= A31
    A12 *= A31
    A13 *= A31
    A1A *= A31
    A31 *= Buffer
    A32 *= Buffer
    A33 *= Buffer
    A3A *= Buffer
else:
    Status = "Fehler"

if((A11 > 0) and (A31 > 0)) or ((A11 < 0) and (A31 < 0)):
    A31 -= A11
    A32 -= A12
    A33 -= A13
    A3A -= A1A
elif((A11 > 0) and (A31 < 0)) or ((A11 < 0) and (A31 > 0)):
    A31 += A11
    A32 += A12
    A33 += A13
    A3A += A1A
else:
    Status = "Fehler"

if(A22 != 0) and (A32 != 0):
    Buffer = A22
    A22 *= A32
    A23 *= A32
    A2A *= A32
    A32 *= Buffer
    A33 *= Buffer
    A3A *= Buffer
else:
    Status = "Fehler"

if((A22 > 0) and (A32 > 0)) or ((A22 < 0) and (A32 < 0)):
    A32 -= A22
    A33 -= A23
    A3A -= A2A
elif((A22 > 0) and (A32 < 0)) or ((A22 < 0) and (A32 > 0)):
    A32 += A22
    A33 += A23
    A3A += A2A
else:
    Status = "Fehler"

if (A31 == 0) and (A32 == 0) and (A21 == 0):
    X3 = (A3A / A33)
    X2 = ((A2A - (A23*X3)) / A22)
    X1 = ((A1A - (A13 * X3) - (A12 * X2)) / A11)
else:
    Status = "Fehler"

# Ausgabe:

print("Dreiecksmatrix:")
print(A11, A12, A13, "|", A1A)
print(A21, A22, A23, "|", A2A)
print(A31, A32, A33, "|", A3A)

print("Status:", Status)
print("Dein Ergebnis lautet:")
print("X1 = ", X1)
print("X2 = ", X2)
print("X3 = ", X3)