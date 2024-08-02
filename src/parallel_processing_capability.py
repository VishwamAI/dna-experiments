import time
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Tuple

def simulate_dna_computation(sequence: str) -> str:
    """Simulate a DNA computation on a given sequence."""
    # This is a placeholder for a more complex DNA computation
    time.sleep(random.uniform(0.1, 0.5))  # Simulate varying computation times
    return ''.join(sorted(sequence))

def generate_dna_sequences(count: int, length: int) -> List[str]:
    """Generate a list of random DNA sequences."""
    return [''.join(random.choice('ACGT') for _ in range(length)) for _ in range(count)]

def sequential_processing(sequences: List[str]) -> List[str]:
    """Process DNA sequences sequentially."""
    return [simulate_dna_computation(seq) for seq in sequences]

def parallel_processing(sequences: List[str]) -> List[str]:
    """Process DNA sequences in parallel."""
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(simulate_dna_computation, seq) for seq in sequences]
        return [future.result() for future in as_completed(futures)]

def compare_processing_methods(sequence_count: int, sequence_length: int) -> Tuple[float, float]:
    """Compare sequential and parallel processing times."""
    sequences = generate_dna_sequences(sequence_count, sequence_length)

    start_time = time.time()
    sequential_results = sequential_processing(sequences)
    sequential_time = time.time() - start_time

    start_time = time.time()
    parallel_results = parallel_processing(sequences)
    parallel_time = time.time() - start_time

    # Verify that both methods produce the same results
    assert sorted(sequential_results) == sorted(parallel_results)

    return sequential_time, parallel_time

def main():
    sequence_count = 100
    sequence_length = 20

    sequential_time, parallel_time = compare_processing_methods(sequence_count, sequence_length)

    print(f"Sequential processing time: {sequential_time:.4f} seconds")
    print(f"Parallel processing time: {parallel_time:.4f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")

if __name__ == "__main__":
    main()
