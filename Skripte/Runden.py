
import math

def errRound(Mittelwert, Fehler):
    """
    :param Mittelwert: Mittelwert des Expermiments
    :param Fehler: bestimmter Fehler des Mittelwerts
    :return: gerundete Liste (Mittelwert, Fehler)
    """

    if Fehler <= 0:
        return Mittelwert, Fehler

    exp = math.floor(math.log10(Fehler)) #Bestimme die Stelle, an der die Erste Stelle ungleich 0 vorkommt

    ziffer = int(Fehler / (10**exp)) #Bestimme die gesuchte Ziffer durch Teilen und Abschneiden

    if ziffer in [1,2]:
        rundest = int(math.fabs(exp) + 1)
    else:
        rundest = int(math.fabs(exp))

    fehler_r = math.ceil(Fehler * (10**rundest)) / (10**rundest)


    mittelwert_r = round(Mittelwert, rundest)

    return mittelwert_r, fehler_r


