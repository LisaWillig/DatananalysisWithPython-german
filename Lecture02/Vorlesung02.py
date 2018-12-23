# Import Statements: Pythoncode (Statements, Expressions,
# Klassen, Definitionen,..) wird aus anderen Modulen geladen
# Üblicherweise steht es am Beginn des Pythonskripts (nach der Erklärung,
# was wer wann warum das Skript geschrieben hat)

# Importierung von fremden Modulen/Packages steht am Anfang (konventionell)
import numpy as np

# eigene Module werden danach geladen
# importiert das gesamte Modul
import Calculations

# Namen stehen zu Verfügung mit dem Prefix Calculations
print(Calculations.summation(1, 2))

# importiert ebenfalls das gesamte Modul, aber der Prefix wird geändert
import Calculations as calc

print(calc.summation(1, 2))

# importiert nur eine Funktion und fügt sie dem lokalen Namespace zu
from Calculations import summation

print(summation(1, 2))

# folgendes ist nicht klug, da man so den Datentyp "string" (der mit str
# bezeichnet wird) überschreibt. Es gibt keinen Fehler oder Warnung von
# Python
# from Calculations import StringOperations as str

from Calculations import StringOperations as myString

# folgende Zeile erzeugt ein Objekt, was dem Datentyp "StringOperations" folgt.
# Es hat also meine definierten Parameter, Variablen, Methoden zur Verfügung
newObject = myString('test')
print(newObject.myClassVar)
newObject.printHello()


# Vergleichsoperatoren

a = [2]
b = [2]
c = a
d = a.copy()

print('is equal: ', a == b)
print('is identical: ', a is b)

print('is equal: ', a == c)
print('is identical: ', a is c)

print('is equal: ', a == d)
print('is identical: ', a is d)
