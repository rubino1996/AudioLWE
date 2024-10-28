'''
lwe_encryption.py

This module provides functions for generating LWE-based keys, encrypting audio signals,
and decrypting the encrypted signals. Learning with Errors (LWE) is used for secure audio processing.
'''

import numpy as np
from numpy.polynomial import polynomial as P
import random


def generate_public_key(n, q):
    '''
    Generate public key components A and B for LWE encryption.

    Parameters:
    - n (int): Degree of the polynomials used.
    - q (int): Prime modulus for the field.

    Returns:
    - tuple: Public key components (A, B).
    '''
    A = np.random.randint(0, q, size=n)
    sA = np.random.randint(0, q, size=4)
    eA = np.random.uniform(-1, 1, size=n)
    xN_1 = np.array([1] + [0] * (n - 1) + [1])
    public_A = np.floor(P.polydiv(A, xN_1)[1])
    calculating_B = P.polymul(public_A, sA) % q
    calculating_B = np.floor(P.polydiv(calculating_B, xN_1)[1])
    public_B = P.polyadd(calculating_B, eA) % q
    public_B = np.floor(P.polydiv(public_B, xN_1)[1])
    return public_A, public_B  # Return only public_A and public_B


def encrypt_signal(public_A, public_B, message, q):
    '''
    Encrypt binary audio signal using the LWE method.

    Parameters:
    - public_A (np.ndarray): Polynomial A from the public key.
    - public_B (np.ndarray): Polynomial B from the public key.
    - message (np.ndarray): Binary message signal.
    - q (int): Prime modulus for the field.

    Returns:
    - np.ndarray: Encrypted audio signal.
    '''
    u = sum(public_A)
    return np.array([sum(public_B) - (q / 2 * m) for m in message])


def decrypt_signal(encrypted_signal, private_key, public_A, q, threshold=None):
    '''
    Decrypt encrypted audio signal using LWE-based decryption.

    Parameters:
    - encrypted_signal (np.ndarray): Encrypted audio signal.
    - private_key (int): Private key for decryption.
    - public_A (np.ndarray): Polynomial A from the public key.
    - q (int): Prime modulus for the field.
    - threshold (int, optional): Threshold for binary signal recovery.

    Returns:
    - np.ndarray: Decrypted binary audio signal.
    '''
    if threshold is None:
        threshold = q // 2  # Default threshold if none provided
    u = sum(public_A)
    decrypted_values = [(v - private_key * u) % q for v in encrypted_signal]
    return np.array([1 if value >= threshold else 0 for value in decrypted_values])
