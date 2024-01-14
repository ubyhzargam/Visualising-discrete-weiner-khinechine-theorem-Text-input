The provided code implements a visualization of bitstream modulation and explores the application of the Discrete Wiener-Khinchin Theorem. 
The user interacts with the program by entering text, and the code converts this text into a bitstream. 
The bitstream is then modulated using a pulse shaping filter, and the resulting signals are graphically presented. 
The code includes colorful user prompts, and the plots are enhanced with different colors for clarity.
Explanation:
User Input (get_text_input):
The program starts by prompting the user to enter text.
The entered text is converted into a bitstream using the ord function to get ASCII values and np.unpackbits to represent each character as a sequence of bits.
Pulse Shaping Filter (g(t)):
The pulse shaping filter, represented by the function g(t), is defined to shape the transmitted signal.
Bitstream Modulation (modulate_and_plot):
The program modulates the bitstream with the pulse shaping filter.
The modulated signal is calculated and plotted along with the original bitstream and the pulse shaping filter.
Autocorrelation and Power Spectral Density (PSD):
Autocorrelation of the modulated signal is calculated using the Discrete Wiener-Khinchin Theorem.
The Power Spectral Density (PSD) is computed using the Fast Fourier Transform (FFT) of the autocorrelation.
Plotting:
The results are displayed through multiple plots, including the original bitstream, pulse shaping filter, modulated signal, autocorrelation, and PSD.
Different colors are used in the plots to enhance visualization and distinguish between different components.
Here is a video demostration of the same : https://drive.google.com/file/d/1r_8A-Vau2tPglWFxH0J8-epX7NTFHWDU/view?usp=sharing
