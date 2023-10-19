python
import numpy as np
from scipy.signal import butter, lfilter, is_stable

# Generate a test signal with noise
t = np.linspace(0, 1, 1000, False)
sig = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*20*t) + 0.1*np.random.randn(len(t))

# Define the filter specifications
order = 4
fs = 1000.0       # Sample rate, Hz
cutoff = 15       # Desired cutoff frequency of the filter, Hz

# Design the Butterworth filter using 'butter()'
nyq = 0.5 * fs    # Nyquist Frequency
normal_cutoff = cutoff / nyq
b, a = butter(order, normal_cutoff, btype='low', analog=False)

# Verify stability of the filter using 'is_stable()'
if is_stable(np.roots(a)):
    print("Filter is stable.")

# Apply the Butterworth filter to the test signal using 'lfilter()'
filtered_sig = lfilter(b, a, sig)
pip install scipy