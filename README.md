# AudioLWE
 A Python project demonstrating Learning with Errors (LWE) encryption applied to audio signals. Encrypts and decrypts audio waveforms, enabling secure audio processing. Includes tools for audio handling, key generation, and visualization of original, encrypted, and decrypted signals. 

## 📜Table of Contents 
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#projectstructure)
- [Example](#example)


## ✨ Features
- **Audio Encryption/Decryption**: Encrypt and decrypt audio signals with ECC.
- **Key Generation**: Generate public and private ECC keys for both sender and recipient.
- **Visualization**: Plot original, encrypted, and decrypted audio signals for comparison.
- **Educational Purpose**: Showcases ECC’s application in multimedia security (not optimized for performance).

## 📥 Installation
1. Clone this repository:
https://github.com/rubino1996/AudioLWE.git
2. Install the required dependencies:
pip install -r requirements.txt

## 🚀 Usage
1. Prepare an Audio File: Place your audio file (e.g., input_audio.wav) in the data/ directory.
2. Run the Main Script: python main.py
3. View Output: Encrypted and decrypted audio files will be saved in data/output/, and a plot showing the original, encrypted, and decrypted waveforms will be saved and displayed.

## 📁 Project Structure
- AudioLWE/
- ├── README.md                  # Project documentation
- ├── audio_processing.py        # Audio I/O functions
- ├── LWE_encryption.py          # LWE encryption/decryption functionst
- ├── main.py                    # Main script
- ├── plotting.py                # Plotting functions    
- └── requirements.txt           # List of required packages

## 🛠 Examples
**Encrypting and Decrypting an Audio File**
1. Load your audio file (input_audio.wav).
2. Run main.py to encrypt and decrypt the audio.
3. View the generated plot and listen to encrypted_audio.wav and decrypted_audio.wav in data/output/.
   
**Plotting**
1. The plot_signals function in plotting.py generates a side-by-side comparison of the original, encrypted, and decrypted audio signals.

