from graphviz import Digraph
import sys
#All works

def parse_fastq(filepath):
    sequences = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for i in range(1, len(lines), 4):
            sequences.append(lines[i].strip())
    return sequences

#Good
def find_overlap(read1, read2, min_length=10):
    max_overlap = 0
    for i in range(1, min(len(read1), len(read2)) + 1):
        if read1[-i:] == read2[:i] and i >= min_length:
            max_overlap = i
    return max_overlap

#Good
def generate_overlap_graph(sequences, output_file='overlap.png'):
    graph = Digraph(format='png')
    
    for i, seq in enumerate(sequences):
        graph.node(f'read{i}', seq)
    
    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if i != j:  # Avoid self-loops
                overlap = find_overlap(seq1, seq2)
                if overlap > 0:
                    graph.edge(f'read{i}', f'read{j}', label=str(overlap))
    
    graph.render(output_file, cleanup=True)


if __name__ == "__main__":
    file = sys.argv[1]
    sequences = parse_fastq(file)
    generate_overlap_graph(sequences, output_file='overlap')
