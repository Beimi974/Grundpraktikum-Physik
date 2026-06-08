
#TODO: WIP


def linReg(xvals, yvals, yerr, Verschiebung):
    import scipy
    import numpy as np
    import matplotlib.pyplot as plt

    error_theta = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]) *(2*np.pi)/360
    theta = np.array([10, 21, 32, 40, 56, 68, 79, 92, 110 ]) * (2*np.pi)/360
    m = np.array([2, 4, 6 , 8, 10, 12, 14, 16, 18])*(10**-3)

    if Verschiebung:
        def f(x, k, c ):
            #Fit Funktion
            return k*x



    coefficients , pcov = scipy.optimize.curve_fit(f, m, theta, sigma = error_theta, absolute_sigma = True)

    fig, ax1 = plt.subplots(1,1, figsize = (10,10))
    a = coefficients[0]

    ax1.errorbar(m, theta, yerr = error_theta , fmt = "o", label = "Datensatz", color = "black", markersize  = 4 , capsize = 3, ecolor = "r")
    xvalues = np.linspace(0, np.max(m)+0.01, num = 100)
    ax1.plot(xvalues, a * xvalues  , "--", color = "blue", linewidth = 1)
    plt.show()
