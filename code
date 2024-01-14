import numpy as np
import matplotlib.pyplot as plt

def get_text_input():
    """Prompts the user to enter text and converts it to a bitstream."""
    text = input("Enter text to convert to bitstream: ")
    bits = np.array([ord(char) for char in text], dtype=np.uint8)
    bits = np.unpackbits(bits)  # Convert to individual bits
    return bits

def g(t):
    return np.where((0 <= t) & (t <= 1), 1, 0)

def modulate_and_plot(bits):
    """Modulates the bit stream with the pulse shaping filter and plots results."""
    N = len(bits)  # Calculate N based on the length of the bit stream
    Tb = 1  # Set a default bit period

    # Modulate bit stream with pulse shaping filter
    t = np.arange(-N * Tb / 2, (N + 1) * Tb / 2, 0.01)  # Adjust time axis
    S = np.zeros_like(t)
    for n in range(N):  # Loop within valid bit indices
        S += bits[n] * g(t - n * Tb)

    # Plot bits, g(t), and modulated signal S(t)
    plt.figure(figsize=(12, 5))
    plt.subplot(3, 1, 1)
    plt.stem(np.arange(N), bits, markerfmt='ro', linefmt='r-')  # Red color for stems
    plt.title("Bit Stream")
    plt.subplot(3, 1, 2)
    plt.plot(t, g(t), 'g-')  # Green color for the pulse shaping filter
    plt.title("Pulse Shaping Filter g(t)")
    plt.subplot(3, 1, 3)
    plt.plot(t, S, 'b-')  # Blue color for the modulated signal
    plt.title("Modulated Signal S(t)")
    plt.tight_layout()

    # Calculate autocorrelation and PSD
    R = np.correlate(S, S, mode='full')
    tau = np.arange(-len(R) // 2 + 1, len(R) // 2 + 1, 1)
    psd = np.fft.fft(R)
    f = np.fft.fftfreq(len(R), d=0.01)

    # Plot autocorrelation and PSD with colors
    plt.figure()
    plt.plot(tau, R, 'm-')  # Magenta color for autocorrelation
    plt.title("Autocorrelation of S(t)")
    plt.figure()
    plt.plot(f, np.abs(psd), 'c-')  # Cyan color for PSD
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Spectral Density (PSD)")
    plt.title("PSD of S(t)")
    plt.show()

bits = get_text_input()
modulate_and_plot(bits)
