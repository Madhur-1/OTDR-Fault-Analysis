import numpy as np

from Utilities.consts import ATTEND_B, NOISE_POWER, P_MAX, PPM


def generate_signal():
    dist = np.linspace(0, 150, int(PPM * 150000))

    # signaldB = -ATTEND_B * dist
    signal = P_MAX * 10 ** (-2 * ATTEND_B * dist / 10)
    noise = np.random.normal(0, NOISE_POWER, len(dist))

    signaltdB = 10 * np.log10((signal + noise) / P_MAX)
    noise_reduction_factor = 10
    while np.isnan(signaltdB).sum() > 0:
        signaltdB[np.isnan(signaltdB)] = (
            10 * np.log10((signal + (noise / noise_reduction_factor)) / P_MAX)
        )[np.isnan(signaltdB)]
        noise_reduction_factor *= 10
    return signaltdB, dist
