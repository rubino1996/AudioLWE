'''
plotting.py

This module provides a function to visualize the original, encrypted, and decrypted audio signals
to analyze encryption and decryption effectiveness.
'''

import matplotlib.pyplot as plt


def plot_signals(times, original, encrypted, decrypted, save_path=None):
    '''
    Plot the original, encrypted, and decrypted audio signals.

    Parameters:
    - times (np.ndarray): Time axis for plotting.
    - original (np.ndarray): Original audio signal data.
    - encrypted (np.ndarray): Encrypted audio signal data.
    - decrypted (np.ndarray): Decrypted audio signal data.
    - save_path (str, optional): File path to save the plot as an image.
    '''
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6))
    ax1.plot(times, original)
    ax1.set_title("Original Signal")
    ax2.plot(times, encrypted)
    ax2.set_title("Encrypted Signal")
    ax3.plot(times, decrypted)
    ax3.set_title("Decrypted Signal")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")
    plt.show()
