"""
Define the constants for the project.
"""

WIDTH = 20  # width of pulse in meters

P_MAX = 100  # power of the laser in mV
NOISE_POWER = 0.00001  # noise level in mV

ATTEND_B = 0.30
SAMPLING_DIST = 2

PPM = 1.0 / SAMPLING_DIST  # number of points sampled per metre

S = 0.15  # chchromatic dispersion in ps/nm-km
V = 2 * 10**8  # speed of light in the medium
DLAMDA = 5  # linewidth of laser in nm

generations_path = "Generations/"
