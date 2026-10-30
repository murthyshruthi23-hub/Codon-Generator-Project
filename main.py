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


def validate_sequence(sequence, sequence_type):
    sequence = sequence.upper()
    sequence = sequence.replace(" ", "")
    sequence = sequence.replace("\n", "")
    sequence = sequence.replace("\t", "")

    if sequence == "":
        return False, "The sequence cannot be empty."

    if sequence_type == "DNA":
        allowed_bases = "ATGC"
    else:
        allowed_bases = "AUGC"

    for base in sequence:
        if base not in allowed_bases:
            return False, "Invalid base found: " + base

    return True, sequence


def split_into_codons(sequence):
    codons = []
    position = 0

    while position + 3 <= len(sequence):
        codon = sequence[position:position + 3]
        codons.append(codon)
        position = position + 3

    remainder = sequence[position:]
    return codons, remainder



def translate_codons(codons, sequence_type):
    amino_acids = []

    for codon in codons:
        lookup_codon = codon

        if sequence_type == "RNA":
            lookup_codon = codon.replace("U", "T")

        amino_acid = CODON_TABLE[lookup_codon]
        amino_acids.append(amino_acid)

    return amino_acids



def find_start_codons(codons, sequence_type):
    if sequence_type == "DNA":
        start_codon = "ATG"
    else:
        start_codon = "AUG"

    positions = []

    for index in range(len(codons)):
        if codons[index] == start_codon:
            positions.append(index + 1)

    return positions



def find_stop_codons(codons, sequence_type):
    if sequence_type == "DNA":
        stop_codons = ["TAA", "TAG", "TGA"]
    else:
        stop_codons = ["UAA", "UAG", "UGA"]

    positions = []

    for index in range(len(codons)):
        if codons[index] in stop_codons:
            positions.append(index + 1)

    return positions



def display_codon_table():
    print("\nDNA CODON TABLE FOR REFERENCE")
    print("-----------------------------")

    for codon in sorted(CODON_TABLE):
        print(codon, ":", CODON_TABLE[codon])



def main():
    print("DNA Codon Table Generator")
    print("-------------------------")

    sequence = input("Enter a DNA sequence: ")

    valid, result = validate_sequence(sequence)

    if not valid:
        print(result)
        return

    sequence = result

    codons, remainder = split_into_codons(sequence)
    amino_acids = translate_codons(codons)

    print("\nDNA sequence:", sequence)
    print("Codons:", "-".join(codons))
    print("Amino acids:", " - ".join(amino_acids))


    start_positions = find_start_codons(codons)
    print("\nStart codons:-")

    if len(start_positions) > 0:
        for position in start_positions:
            print("Codon:", codons[position - 1],
                  "| Position:", position)
    else:
        print("No start codons found.")


    stop_positions = find_stop_codons(codons)
    print("\nStop codons:-")

    if len(stop_positions) > 0:
        for position in stop_positions:
            print("Codon:", codons[position - 1],
                  "| Position:", position)
    else:
        print("No stop codons found.")


    if remainder:
        print("\nIncomplete codon at the end:", remainder)
        print("These bases were not translated.")

    display_codon_table()


if __name__ == "__main__":
    main()