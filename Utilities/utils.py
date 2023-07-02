import numpy as np

from .consts import DLAMDA, PPM, WIDTH, S, V


def widconvert(wid, dis):  # gives the number of points in which the pulse can sampled
    return int((WIDTH + V * S * 10**-8 * DLAMDA * dis) * PPM)


def event(loss, distance, t, dist):
    sig = np.linspace(loss, loss, len(dist))
    if t == 0:
        k = 0
        while k < distance * len(dist) // 150.0:
            sig[k] = 0
            k += 1
        i = 0
        while i < widconvert(WIDTH, distance):
            sig[int(distance * len(dist) / 150) + i] = (
                loss / widconvert(WIDTH, distance)
            ) * i
            i += 1

    else:
        k = 0
        while k < distance * len(dist) // 150.0:
            sig[k] = 0
            k += 1
        i = 0
        while i < widconvert(WIDTH, distance):
            sig[int(distance * len(dist) / 150) + i] = 20
            i += 1
    return sig
