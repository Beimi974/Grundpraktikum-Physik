#%% md
## **Messwerte:**
#%%
import numpy as np
import matplotlib.pyplot as plt
#Messwerte für die Maximalkraft in N
                                                  #Konzentration Tensidlösung
Messwerte = np.array([[0.074, 0.074, 0.074, 0.074, 0.073],  #0 mmol/l

                      [0.072, 0.073, 0.073, 0.073, 0.072],  # 8 mmol/l

                      [0.074, 0.074, 0.074, 0.074, 0.074],  # 4 mmol/l

                      [0.074, 0.074, 0.074, 0.075, 0.074],  # 2 mmol/l

                      [0.074, 0.075, 0.075, 0.074, 0.075],  # 1 mmol/l

                      [0.074, 0.074, 0.074, 0.074, 0.074],  # 0.5 mmol/l

                      [0.075, 0.074, 0.075, 0.075, 0.075]  # 0.25 mmol/l
                     ])

Konzentration = np.array([0, 8, 4, 2,1, 0.5, 0.25]) #Konzentrationen in mmol/l

Mittelwerte = np.mean(Messwerte, axis = 1) #Einzelne Mittelwerte über die 5 Messungen
MittelwertFehler = Mittelwerte * 1/100 #Konstanter Fehler in der Messung von 1 %

#Messwerte für Tensid
Molekulargewicht = 56.44 #Molekulargewicht in g/mol
Zugabemenge = 0.187 #Zugabemenge in g

#Messwerte für Flüssigkeit und Ring
Temp = 20.02 #Grad Celsius

Durchmesser = 5.95e-3 #Durchmesserin m
D_Fehler = 0.05e-3 #Fehler des Durchmessers in m


#Mittelwert für die Oberflächenspannung
Oberflaechenspannnung = Mittelwerte / (4 * np.pi *(Durchmesser/2))


#Fehlerbestimmung

#Fehlerbestimmung für die Oberflächenspannung durch Gaußsche Fehlerfortpflanzung
import sympy

#Automatische Berechnung Fehlerfortpflanzung nach Gauß

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


F, r = sympy.symbols("F, r")
Variablen = np.array([F,r])
expr = F / (4*np.pi*r)

FehlerObSp = np.array([]) #Berechnete Fehler für die Oberflächenspannung für die einzelnen Messreihen

for pos in range(len(Mittelwerte)):
    mean = Mittelwerte[pos]
    err = MittelwertFehler[pos]
    FehlerObSp = np.append(FehlerObSp, Gaußfehler(expr, Variablen, np.array([mean, Durchmesser/2]), np.array([err, D_Fehler]))) #Gaußfehler für die akutlle Messreihe

print(f"Fehler: {FehlerObSp}")


#%% md
## **Grafische Darstellung:**
#%%
#Grafische Darstellung
import scipy
import numpy as np

def f(x,k,c):
    return k*x +c

coefficients , pcov = scipy.optimize.curve_fit(f, Konzentration, Oberflaechenspannnung, sigma = FehlerObSp, absolute_sigma = True)
a = coefficients[0]
c = coefficients[1]

fig, ax1 = plt.subplots(1,1, figsize = (11,9))

ax1.errorbar(Konzentration, Oberflaechenspannnung, yerr = FehlerObSp , fmt = "o", label = "Datensatz", color = "black", markersize  = 4 , capsize = 3, ecolor = "r")
xvalues = np.linspace(0, np.max(Konzentration)+0.01, num = 100)
ax1.plot(xvalues, a * xvalues +c , "--", color = "blue", linewidth = 1)

ax1.set_xlabel("Konzentration (mmol/l)")
ax1.set_ylabel("Oberflächenspannung (N/m)")

ax1.grid(True)
ax1.set_title("Oberflächenspannung der Lösung")

plt.savefig("Plot.png")
plt.show()



