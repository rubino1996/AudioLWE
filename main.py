'''
main.py

Main script to demonstrate encryption and decryption of audio signals using the Learning with Errors (LWE) approach.
'''

import time
import numpy as np
from audio_processing import load_audio, save_audio
from lwe_encryption import generate_public_key, encrypt_signal, decrypt_signal
from plotting import plot_signals

# Load the audio file
sample_freq, n_samples, signal_array = load_audio(
    "data/input_audio.wav")
times = np.linspace(0, n_samples / sample_freq, num=n_samples)

# Convert audio to binary message
m_binary = np.where(signal_array != 0, 1, 0)

# Set LWE parameters
n = 256
q = 7681
public_A, public_B = generate_public_key(n, q)
private_key = np.random.randint(1, q // 2) * 2 + 1

# Encrypt the binary audio signal
start_time = time.time()
encrypted_signal = encrypt_signal(public_A, public_B, m_binary, q)
encryption_time = time.time() - start_time

# Decrypt the encrypted signal
start_time = time.time()
decrypted_binary = decrypt_signal(encrypted_signal, private_key, public_A, q)
decryption_time = time.time() - start_time

# Save encrypted and decrypted audio
save_audio("data/output/LWE_encrypted_audio.wav",
           sample_freq, encrypted_signal.astype(np.int16))
save_audio("data/output/LWE_decrypted_audio.wav",
           sample_freq, decrypted_binary * signal_array)

# Plot results
plot_signals(times, signal_array, encrypted_signal,
             decrypted_binary * signal_array, save_path="data/output/plot.png")

# Display timing results
print(f"Encryption time: {encryption_time:.4f} seconds")
print(f"Decryption time: {decryption_time:.4f} seconds")
