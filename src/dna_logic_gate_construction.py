import random
from typing import List, Tuple

class DNAStrand:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def __repr__(self):
        return f"DNAStrand('{self.sequence}')"

def generate_complementary_strand(strand: DNAStrand) -> DNAStrand:
    """Generate a complementary DNA strand."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return DNAStrand(''.join(complement[base] for base in strand.sequence))

def strand_displacement(target: DNAStrand, input_strand: DNAStrand) -> Tuple[DNAStrand, DNAStrand]:
    """Simulate strand displacement reaction."""
    if input_strand.sequence in target.sequence:
        displaced = DNAStrand(target.sequence.replace(input_strand.sequence, '', 1))
        return input_strand, displaced
    return target, input_strand

def dna_and_gate(input1: DNAStrand, input2: DNAStrand) -> DNAStrand:
    """Implement AND gate using DNA strands."""
    # Assuming input1 and input2 are complementary to parts of a longer strand
    target = DNAStrand(input1.sequence + input2.sequence + "GGGG")
    _, result1 = strand_displacement(target, input1)
    output, _ = strand_displacement(result1, input2)
    return output

def dna_or_gate(input1: DNAStrand, input2: DNAStrand) -> DNAStrand:
    """Implement OR gate using DNA strands."""
    # Assuming either input can displace the output strand
    target = DNAStrand(input1.sequence + "GGGG")
    output, _ = strand_displacement(target, input1)
    if output == target:
        output, _ = strand_displacement(target, input2)
    return output

def dna_not_gate(input_strand: DNAStrand) -> DNAStrand:
    """Implement NOT gate using DNA strands."""
    # NOT gate is implemented by displacing a complementary strand
    target = generate_complementary_strand(input_strand)
    _, output = strand_displacement(target, input_strand)
    return output

def main():
    # Example usage
    input_a = DNAStrand("ATCG")
    input_b = DNAStrand("GCTA")

    print("AND Gate:")
    result_and = dna_and_gate(input_a, input_b)
    print(f"Input A: {input_a}, Input B: {input_b}, Output: {result_and}")

    print("\nOR Gate:")
    result_or = dna_or_gate(input_a, input_b)
    print(f"Input A: {input_a}, Input B: {input_b}, Output: {result_or}")

    print("\nNOT Gate:")
    result_not = dna_not_gate(input_a)
    print(f"Input: {input_a}, Output: {result_not}")

if __name__ == "__main__":
    main()
