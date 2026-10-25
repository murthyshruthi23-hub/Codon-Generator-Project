# DNA Codon Generator

CODON_TABLE = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}


def validate_sequence(sequence):
    sequence = "".join(sequence.upper().split())

    if not sequence:
        return False, "The sequence cannot be empty."

    for base in sequence:
        if base not in "ATGC":
            return False, "Invalid DNA sequence. Use only A, T, G and C."

    return True, sequence



def split_into_codons(sequence):
    codons = []

    for i in range(0, len(sequence) - 2, 3):
        codons.append(sequence[i:i + 3])

    remainder = sequence[len(codons) * 3:]
    return codons, remainder



def translate_codons(codons):
    amino_acids = []

    for codon in codons:
        amino_acids.append(CODON_TABLE[codon])

    return amino_acids



def find_start_codons(codons):
    start_positions = []

    for i, codon in enumerate(codons):
        if codon == "ATG":
            start_positions.append(i + 1)

    return start_positions



def find_stop_codons(codons):
    stop_positions = []

    for i, codon in enumerate(codons):
        if codon in ["TAA", "TAG", "TGA"]:
            stop_positions.append(i + 1)

    return stop_positions



def display_codon_table():
    print("\nDNA CODON TABLE FOR REFERENCE")
    print("-----------------------------")

    for codon in sorted(CODON_TABLE):
        print(codon, ":", CODON_TABLE[codon])


