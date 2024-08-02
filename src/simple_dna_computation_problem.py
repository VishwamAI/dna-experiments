import random
from typing import List, Tuple

class DNAStrand:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def __repr__(self):
        return f"DNAStrand('{self.sequence}')"

def binary_to_dna(binary: str) -> DNAStrand:
    """Convert a binary string to a DNA sequence."""
    return DNAStrand(''.join('A' if bit == '0' else 'T' for bit in binary))

def dna_to_binary(dna: DNAStrand) -> str:
    """Convert a DNA sequence back to a binary string."""
    return ''.join('0' if base == 'A' else '1' for base in dna.sequence)

def generate_random_binary(length: int) -> str:
    """Generate a random binary string of given length."""
    return ''.join(random.choice('01') for _ in range(length))

def dna_addition(a: DNAStrand, b: DNAStrand) -> DNAStrand:
    """Simulate binary addition using DNA strands."""
    binary_a = dna_to_binary(a)
    binary_b = dna_to_binary(b)

    # Perform binary addition
    result = bin(int(binary_a, 2) + int(binary_b, 2))[2:]

    # Pad the result to match the length of inputs
    result = result.zfill(max(len(binary_a), len(binary_b)))

    return binary_to_dna(result)

def visualize_addition(a: DNAStrand, b: DNAStrand, result: DNAStrand):
    """Visualize the DNA addition process."""
    print(f"Input A (DNA): {a}")
    print(f"Input A (Binary): {dna_to_binary(a)}")
    print(f"Input B (DNA): {b}")
    print(f"Input B (Binary): {dna_to_binary(b)}")
    print(f"Result (DNA): {result}")
    print(f"Result (Binary): {dna_to_binary(result)}")

def main():
    # Generate two random binary numbers
    length = 8
    binary_a = generate_random_binary(length)
    binary_b = generate_random_binary(length)

    # Convert to DNA strands
    dna_a = binary_to_dna(binary_a)
    dna_b = binary_to_dna(binary_b)

    # Perform DNA addition
    result = dna_addition(dna_a, dna_b)

    # Visualize the process
    visualize_addition(dna_a, dna_b, result)

if __name__ == "__main__":
    main()
