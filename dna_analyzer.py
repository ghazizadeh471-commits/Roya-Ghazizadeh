def analyze_dna(sequence):
    sequence = sequence.upper()

    result = {
        "Length": len(sequence),
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    gc_content = ((result["G"] + result["C"]) / len(sequence)) * 100
    result["GC Content"] = round(gc_content, 2)

    return result


dna = "ATGCGTACGTTAGC"

analysis = analyze_dna(dna)

for key, value in analysis.items():
    print(f"{key}: {value}")
