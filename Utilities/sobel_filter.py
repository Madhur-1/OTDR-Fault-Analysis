import numpy as np


def apply_sobelfilter(signaltdB, dist):
    k = 0
    while k < len(dist):
        if signaltdB[k] > 0:
            signaltdB[k] = 0
        k += 1

    sobelfilter = np.linspace(0, 0, len(dist))
    k = 1
    while k < len(dist) - 2:
        sobelfilter[k] = signaltdB[k + 1] - signaltdB[k - 1]
        k += 1
    return sobelfilter
