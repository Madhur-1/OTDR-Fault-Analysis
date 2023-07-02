import matplotlib.pyplot as plt


def plot_trace(dist, signaltdB, filepath="trace.png"):
    plt.figure(figsize=(30, 6))
    plt.plot(dist, signaltdB)
    plt.title("OTDR TRACE")
    plt.xlabel("DISTANCE(KM)")
    plt.ylabel("SIGNAL POWER(dB")
    plt.savefig(filepath, dpi=300)
    plt.show()


def plot_sobel(dist, sobelfilter, filepath="sobel_plot.png"):
    plt.figure(figsize=(30, 6))
    plt.plot(dist, sobelfilter)
    plt.savefig(filepath, dpi=300)
    plt.show()
