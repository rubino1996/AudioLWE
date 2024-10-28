'''
audio_processing.py

This module handles loading and saving audio files in WAV format. It returns
audio data in a format compatible with the encryption and decryption process.
'''

import wave
import numpy as np
from scipy.io.wavfile import write

def load_audio(file_path):
    '''
    Load an audio file and return its sample frequency, number of samples, and audio data.
    
    Parameters:
    - file_path (str): Path to the WAV audio file.

    Returns:
    - tuple: (sample frequency, number of samples, audio data as NumPy array)
    '''
    audio = wave.open(file_path)
    sample_freq = audio.getframerate()
    n_samples = audio.getnframes()
    signal_wave = audio.readframes(-1)
    audio.close()
    return sample_freq, n_samples, np.frombuffer(signal_wave, dtype=np.int16)

def save_audio(file_path, sample_freq, signal_array):
    '''
    Save a NumPy array as an audio file in WAV format.
    
    Parameters:
    - file_path (str): Path to save the audio file.
    - sample_freq (int): Sample frequency for the audio.
    - signal_array (np.ndarray): Audio data as a NumPy array.
    '''
    write(file_path, sample_freq, signal_array)
