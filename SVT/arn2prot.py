rna = (input("Brin ARN à transcrire"))
print ("Brin ARN: ", rna)

rna_codon = {"UUU" : "Phe", "CUU" : "Leu", "AUU" : "Iso", "GUU" : "Val",
           "UUC" : "Phe", "CUC" : "Leu", "AUC" : "Iso", "GUC" : "Val",
           "UUA" : "Leu", "CUA" : "Leu", "AUA" : "Iso", "GUA" : "Val",
           "UUG" : "Leu", "CUG" : "Leu", "AUG" : "M", "GUG" : "Val",
           "UCU" : "Ser", "CCU" : "Pro", "ACU" : "Thr", "GCU" : "Ala",
           "UCC" : "Ser", "CCC" : "Pro", "ACC" : "Thr", "GCC" : "Ala",
           "UCA" : "Ser", "CCA" : "Pro", "ACA" : "Thr", "GCA" : "Ala",
           "UCG" : "Ser", "CCG" : "Pro", "ACG" : "Thr", "GCG" : "Ala",
           "UAU" : "Tyr", "CAU" : "His", "AAU" : "Asp", "GAU" : "Asp",
           "UAC" : "Tyr", "CAC" : "His", "AAC" : "Asp", "GAC" : "Asp",
           "UAA" : "STOP", "CAA" : "Gln", "AAA" : "Lys", "GAA" : "Gln",
           "UAG" : "STOP", "CAG" : "Gln", "AAG" : "Lys", "GAG" : "Gln",
           "UGU" : "Cys", "CGU" : "Agr", "AGU" : "Ser", "GGU" : "Gly",
           "UGC" : "Cys", "CGC" : "Agr", "AGC" : "Ser", "GGC" : "Gly",
           "UGA" : "STOP", "CGA" : "Agr", "AGA" : "Agr", "GGA" : "Gly",
           "UGG" : "Try", "CGG" : "Agr", "AGG" : "Agr", "GGG" : "Gly" 
           }

protein_string = ""

for i in range(0, len(rna)-(3+len(rna)%3), 3):
    if rna_codon[rna[i:i+3]] == "STOP" :
        break
    protein_string += rna_codon[rna[i:i+3]]

print ("Proteine: ", protein_string)
