import os

from Utilities.add_events import add_events
from Utilities.consts import generations_path
from Utilities.signal import generate_signal
from Utilities.sobel_filter import apply_sobelfilter
from Utilities.visualize import plot_sobel, plot_trace
from Utilities.write_utils import save_sobel_filter_out, save_trace_raw

signaltdB, dist = generate_signal()

signaltdB = add_events(
    signaltdB, dist, filepath=os.path.join(generations_path, "events.csv")
)


sobelfilter = apply_sobelfilter(signaltdB, dist)


plot_trace(dist, signaltdB, filepath=os.path.join(generations_path, "trace.png"))


plot_sobel(dist, sobelfilter, filepath=os.path.join(generations_path, "sobel_plot.png"))


save_sobel_filter_out(
    dist, sobelfilter, filepath=os.path.join(generations_path, "sobel.csv")
)


save_trace_raw(
    dist, signaltdB, filepath=os.path.join(generations_path, "trace_raw.csv")
)
