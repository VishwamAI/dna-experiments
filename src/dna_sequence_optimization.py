import random
from typing import List, Tuple

def generate_dna_sequence(length: int) -> str:
    """Generate a random DNA sequence of given length."""
    return ''.join(random.choice('ACGT') for _ in range(length))

def calculate_hamming_distance(seq1: str, seq2: str) -> int:
    """Calculate the Hamming distance between two DNA sequences."""
    return sum(s1 != s2 for s1, s2 in zip(seq1, seq2))

def calculate_gc_content(sequence: str) -> float:
    """Calculate the GC content of a DNA sequence."""
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

def optimize_dna_sequence(sequence: str, target_gc: float = 0.5, min_distance: int = 3) -> str:
    """
    Optimize a DNA sequence for GC content and minimum Hamming distance.

    Args:
    sequence (str): The input DNA sequence.
    target_gc (float): The target GC content (default 0.5).
    min_distance (int): The minimum Hamming distance between any two subsequences (default 3).

    Returns:
    str: The optimized DNA sequence.
    """
    optimized = list(sequence)

    # Optimize GC content
    current_gc = calculate_gc_content(sequence)
    for i in range(len(optimized)):
        if current_gc < target_gc and optimized[i] in 'AT':
            optimized[i] = random.choice('GC')
            current_gc = calculate_gc_content(''.join(optimized))
        elif current_gc > target_gc and optimized[i] in 'GC':
            optimized[i] = random.choice('AT')
            current_gc = calculate_gc_content(''.join(optimized))

    # Optimize minimum distance
    for i in range(len(optimized) - min_distance + 1):
        for j in range(i + 1, len(optimized) - min_distance + 1):
            if calculate_hamming_distance(optimized[i:i+min_distance], optimized[j:j+min_distance]) < min_distance:
                optimized[j:j+min_distance] = generate_dna_sequence(min_distance)

    return ''.join(optimized)

def main():
    # Example usage
    original_sequence = generate_dna_sequence(50)
    print(f"Original sequence: {original_sequence}")
    print(f"Original GC content: {calculate_gc_content(original_sequence):.2f}")

    optimized_sequence = optimize_dna_sequence(original_sequence)
    print(f"Optimized sequence: {optimized_sequence}")
    print(f"Optimized GC content: {calculate_gc_content(optimized_sequence):.2f}")

if __name__ == "__main__":
    main()
