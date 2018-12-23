"""
Externes Modul mit einfachen Funktionen.
Hier: im Kontext der Temperaturumrechnung
"""

def tempConversion_FtoDeg(temp):
    return (temp-32) * 5/9

def warnTemp(temp, threshold=95):
    if temp>threshold:
        print('Warning!')