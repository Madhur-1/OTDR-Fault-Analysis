import csv
import random

from Utilities.utils import event


def add_events(signaltdB, dist, filepath="events.csv"):
    f = open(filepath, "w", newline="")
    wfile = csv.writer(f)
    wfile.writerow(["type", "location", "loss"])
    noe = random.randrange(1, 6, 1)  # gives the number of events
    i = 0
    while i < noe:
        loc = random.randrange(
            100, int(100 * len(dist) / 150), 1
        )  # randomly generating the location and loss and the type(splice or reflection)
        los = random.randrange(20, 100, 1) / 10
        typ = random.randrange(0, 2, 1)
        signaltdB += event(-los, dist[loc], typ, dist)
        wfile.writerow(
            ["reflection" if (typ == 1) else "splice", round(dist[loc], 2), los]
        )
        i += 1

    f.close()
    return signaltdB
