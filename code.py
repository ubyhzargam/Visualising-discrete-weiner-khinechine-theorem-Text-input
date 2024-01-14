import numpy as np
import matplotlib.pyplot as plt

def get_text_input():
    """Prompts the user to enter text and converts it to a bitstream."""
    text = input("Enter text to convert to bitstream: ")
    bits = np.array([ord(char) for char in text], dtype=np.uint8)
    bits = np.unpackbits(bits)  
    return bits

def g(t):
    return np.where((0 <= t) & (t <= 1), 1, 0)

def modulate_and_plot(bits):
    """Modulates the bit stream with the pulse shaping filter and plots results."""
    N = len(bits)  
    Tb = 1  

  
    t = np.arange(-N * Tb / 2, (N + 1) * Tb / 2, 0.01) 
    S = np.zeros_like(t)
    for n in range(N):  
        S += bits[n] * g(t - n * Tb)

  
    plt.figure(figsize=(12, 5))
    plt.subplot(3, 1, 1)
    plt.stem(np.arange(N), bits, markerfmt='ro', linefmt='r-') 
    plt.title("Bit Stream")
    plt.subplot(3, 1, 2)
    plt.plot(t, g(t), 'g-')  
    plt.title("Pulse Shaping Filter g(t)")
    plt.subplot(3, 1, 3)
    plt.plot(t, S, 'b-')  
    plt.title("Modulated Signal S(t)")
    plt.tight_layout()

    
    R = np.correlate(S, S, mode='full')
    tau = np.arange(-len(R) // 2 + 1, len(R) // 2 + 1, 1)
    psd = np.fft.fft(R)
    f = np.fft.fftfreq(len(R), d=0.01)

    
    plt.figure()
    plt.plot(tau, R, 'm-')  
    plt.title("Autocorrelation of S(t)")
    plt.figure()
    plt.plot(f, np.abs(psd), 'c-')  
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Spectral Density (PSD)")
    plt.title("PSD of S(t)")
    plt.show()

bits = get_text_input()
modulate_and_plot(bits)
