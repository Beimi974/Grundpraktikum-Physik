#Automatische Berechnung Fehlerfortpflanzung nach Gauß
import sympy


# noinspection NonAsciiCharacters
def Gaußfehler(expr, Variablen, Mittelwerte, Fehler):
    """
    :param expr: Sympy Gleichung für die Ergebnisvariable, für die der Fehler bestimmt werden soll,
    :param Variablen: 1D Array mit den fehlerbehafteten Variablen in expr (Als sympy.Symbol())
    :param Mittelwerte: 1D Array mit den Mittelwerten der fehlerbehafteten Variablen (Reihenfolge)
    :param Fehler: 1D Array mit den Fehlern der fehlerbehafteten Variablen (Reihenfolge!)
    :return: Fehler für die Varaible die druch expr berechnet wird
    """

    import sympy
    import numpy as np

    count = 0
    for pos in range(len(Variablen)): #Loop durch alle fehlerbehafteten Variablen

        deriv = expr.diff(Variablen[pos]) #Ableitung nach der aktuellen Variablen

        deriv_func = sympy.lambdify(Variablen, deriv, "numpy") #Ableitung in aufrufbare Funktion umwandeln

        count += (Fehler[pos] * deriv_func(*Mittelwerte)) ** 2 #Nach der Formel (Fehler * Ableitung)**2 addieren

    error = np.sqrt(count) #Nach Formel Wurzel aus der bestimmten Summe ziehen

    return error

# noinspection NonAsciiCharacters
def VisualGaußfehler(expr, Variablen):
    """
    :param expr: Sympy Gleichung für die Ergebnisvariable, für die der Fehler bestimmt werden soll,
    :param Variablen: 1D Array mit den fehlerbehafteten Variablen in expr (Als sympy.Symbol())
    :param Mittelwerte: 1D Array mit den Mittelwerten der fehlerbehafteten Variablen (Reihenfolge)
    :param Fehler: 1D Array mit den Fehlern der fehlerbehafteten Variablen (Reihenfolge!)
    :return: Fehlerterm für expr
    """

    import sympy as sp

    count = 0
    for pos in range(len(Variablen)): #Loop durch alle fehlerbehafteten Variablen

        deriv = expr.diff(Variablen[pos]) #Ableitung nach der aktuellen Variablen

        count += (deriv * sp.Symbol(f"Delta_{str(Variablen[pos])}")) ** 2 #Nach der Formel (Fehler * Ableitung)**2 addieren

    error = sp.sqrt(count) #Nach Formel Wurzel aus der bestimmten Summe ziehen

    return error