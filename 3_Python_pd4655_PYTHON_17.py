from Bio import Entrez, SeqIO, Align

# stawienie email 
Entrez.email = "emanowiczpaulina@gmail.com"

# Pobieranie sekwencji nukleotydowych z bazy GenBank
ids = ["JX669568", "JX669571"]
sequences = []

for seq_id in ids:
    handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    sequences.append(record)
    handle.close()

# zzapisanie sekwencji do FASTA
fasta_file = "sequences.fasta"
with open(fasta_file, "w") as output_handle:
    SeqIO.write(sequences, output_handle, "fasta")

print(f"Sekwencje zapisano w pliku {fasta_file}.")

# wczytanie sekwencji z FASTA
with open(fasta_file, "r") as input_handle:
    records = list(SeqIO.parse(input_handle, "fasta"))

# porównanie sekwencji za pomocą Needleman-Wunsch
aligner = Align.PairwiseAligner()
aligner.mode = "global"

# dopasowanie pierwszej sekwencji do drugiej
alignment = aligner.align(records[0].seq, records[1].seq)[0]

# wyświetlenie najlepszego dopasowania i punktacji
print("\nNajlepsze dopasowanie:")
print(alignment)
print(f"Punktacja dopasowania: {alignment.score}")
