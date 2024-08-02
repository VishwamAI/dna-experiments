import random
from typing import List, Tuple

def generate_dna_sequence(length: int) -> str:
    """Generate a random DNA sequence of given length."""
    return ''.join(random.choice('ACGT') for _ in range(length))

def dna_to_binary(dna_sequence: str) -> str:
    """Convert DNA sequence to binary."""
    return ''.join('00' if base == 'A' else '01' if base == 'C' else '10' if base == 'G' else '11' for base in dna_sequence)

def binary_to_dna(binary_sequence: str) -> str:
    """Convert binary sequence back to DNA."""
    return ''.join('A' if binary_sequence[i:i+2] == '00' else 'C' if binary_sequence[i:i+2] == '01' else 'G' if binary_sequence[i:i+2] == '10' else 'T' for i in range(0, len(binary_sequence), 2))

def introduce_errors(sequence: str, error_rate: float) -> str:
    """Introduce random errors in the binary sequence."""
    bases = list(sequence)
    for i in range(len(bases)):
        if random.random() < error_rate:
            bases[i] = '1' if bases[i] == '0' else '0'
    return ''.join(bases)

def hamming_encode(data: str) -> str:
    """Encode the data using a simple Hamming code."""
    encoded = list(data)
    for i in range(1, len(encoded) + 1):
        if bin(i).count('1') == 1:  # If i is a power of 2
            encoded.insert(i - 1, '0')

    for i in range(len(encoded)):
        if bin(i + 1).count('1') == 1:  # Parity bits
            parity = sum(int(encoded[j]) for j in range(len(encoded)) if j != i and (j + 1) & (i + 1)) % 2
            encoded[i] = str(parity)

    return ''.join(encoded)

def hamming_decode(encoded: str) -> str:
    """Decode the Hamming-encoded data and correct single-bit errors."""
    data = list(encoded)
    error_pos = 0
    for i in range(len(data)):
        if bin(i + 1).count('1') == 1:  # Parity bits
            parity = sum(int(data[j]) for j in range(len(data)) if (j + 1) & (i + 1)) % 2
            if parity != 0:
                error_pos += i + 1

    if error_pos != 0:
        data[error_pos - 1] = str(1 - int(data[error_pos - 1]))

    return ''.join(bit for i, bit in enumerate(data) if bin(i + 1).count('1') != 1)

def simulate_error_correction(data_length: int, error_rate: float) -> Tuple[str, str, str, str]:
    """Simulate the error correction process."""
    original_dna = generate_dna_sequence(data_length)
    original_binary = dna_to_binary(original_dna)

    print(f"Original DNA: {original_dna}")
    print(f"Original binary: {original_binary}")

    encoded_data = hamming_encode(original_binary)
    print(f"Encoded data: {encoded_data}")

    corrupted_data = introduce_errors(encoded_data, error_rate)
    corrected_data = hamming_decode(corrupted_data)

    corrected_dna = binary_to_dna(corrected_data)

    return original_dna, encoded_data, corrupted_data, corrected_dna

def main():
    data_length = 4  # This will result in 8 binary digits
    error_rate = 0.1

    original, encoded, corrupted, corrected = simulate_error_correction(data_length, error_rate)

    print(f"Original DNA: {original}")
    print(f"Encoded data: {encoded}")
    print(f"Corrupted data: {corrupted}")
    print(f"Corrected DNA: {corrected}")
    print(f"Correction successful: {original == corrected}")

if __name__ == "__main__":
    main()
