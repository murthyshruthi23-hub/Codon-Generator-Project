
# Codon Table Generator

## Project Description
The Codon Table Generator is a Python-based program that accepts DNA or RNA sequences and translates them into their corresponding amino acid sequences using the standard genetic code.

The project demonstrates the use of Python dictionaries, loops, conditional statements, string manipulation, and input validation in bioinformatics.

## Objectives
- Create a dictionary containing all 64 standard genetic code codons and their corresponding amino acids.
- Accept DNA and RNA sequences as user input.
- Validate the input sequences to ensure that only the correct nucleotide bases are used.
- Divide the sequences into groups of three bases called codons.
- Translate each codon into its corresponding amino acid.
- Identify start and stop codons.
- Handle incomplete codons at the end of a sequence.
- Display the codon table and translated amino acid sequence.

## Features
1. **DNA Sequence Input:** Accepts DNA sequences containing A, T, G and C.
2. **RNA Sequence Input:** Accepts RNA sequences containing A, U, G and C.
3. **Sequence Validation:** Checks whether the entered sequence contains valid nucleotide bases.
4. **Codon Splitting:** Divides the sequence into triplets of three nucleotides.
5. **Amino Acid Translation:** Converts each codon into its corresponding amino acid using the standard genetic code.
6. **Start Codon Identification:** Identifies ATG in DNA and AUG in RNA.
7. **Stop Codon Identification:** Identifies TAA, TAG and TGA in DNA and UAA, UAG and UGA in RNA.
8. **Incomplete Codon Handling:** Identifies leftover bases that do not form a complete codon and excludes them from translation.
9. **Codon Table Display:** Displays the corresponding DNA or RNA codon table.

## Requirements
- Python 3.x
- No additional external libraries are required.

## How to Run the Program

1. Clone or download this repository.
2. Open the project folder in a terminal or Python IDE.
3. Run the Python program:

   ```bash
   python main.py
   ```

4. Select the sequence type by entering `DNA` or `RNA`.
5. Enter the nucleotide sequence when prompted.
6. The program displays:
   - The input sequence
   - Codons obtained after splitting
   - Corresponding amino acid sequence
   - Start codon positions
   - Stop codon positions
   - Any incomplete codon at the end
   - The codon table


## Example

### DNA Input
```text
Enter sequence type (DNA/RNA): DNA
Enter a DNA sequence: ATGGCTTAA
```

### RNA Input
```text
Enter sequence type (DNA/RNA): RNA
Enter a RNA sequence: AUGGCUUAA
```

Both sequences produce the following translation:

```text
Codons: ATG-GCT-TAA  (DNA)
Amino acids: Methionine - Alanine - Stop
```

For RNA, the codons displayed are `AUG-GCU-UAA`.

## Project Structure

```text
Codon-Table-Generator/
│
├── main.py
└── README.md
```

## Learning Outcomes
Through this project, we learned how to:
- Use Python dictionaries to store genetic code information.
- Apply loops and conditional statements to process biological sequences.
- Perform string manipulation and input validation.
- Understand codon-based translation of DNA and RNA sequences.
- Identify important genetic signals such as start and stop codons.
- Apply basic Python programming concepts to a bioinformatics problem.
- Use Git and GitHub for project development and version control.

## References
- Standard Genetic Code / NCBI Genetic Codes: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi

---

**Project:** Development of a Codon Table Generator  
**Language:** Python  
**Domain:** Bioinformatics
