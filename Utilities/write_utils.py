import csv


def save_sobel_filter_out(dist, sobelfilter, filepath="sobel.csv"):
    f = open(filepath, "w", newline="")
    wfile = csv.writer(f)
    n = 0
    while n < len(dist):
        wfile.writerow([dist[n], sobelfilter[n]])
        n += 1
    f.close()


def save_trace_raw(dist, signaltdB, filepath="trace_raw.csv"):
    f = open(filepath, "w", newline="")
    wfile = csv.writer(f)
    n = 0
    while n < len(dist):
        wfile.writerow([n, dist[n], signaltdB[n]])
        n += 1
    f.close()
