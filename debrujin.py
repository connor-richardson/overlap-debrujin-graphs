from graphviz import Digraph
import sys

#All works
def parse_fasta(filepath):
    sequence = []
    with open(filepath, 'r') as f:
        lines = f.readlines()

    sequence = ''.join(line.strip() for line in lines[1:])
    return sequence

def generate_kmers(sequence, k):
    return [sequence[i:i+k] for i in range(len(sequence) -k +1)]

def generate_debrujin(kmers, output_file = 'brujin'):
    graph = Digraph(format = 'png')
    nodes = set()

    for kmer in kmers:
        start_node = kmer[:-1]
        end_node = kmer[1:]
        nodes.add(start_node)
        nodes.add(end_node)
        graph.edge(start_node, end_node)


    for node in nodes:
        graph.node(node)

    graph.render(output_file, cleanup = True)



if __name__ == "__main__":
    fasta_file = sys.argv[1]
    sequence = parse_fasta(fasta_file)
    kmers = generate_kmers(sequence, 10)
    generate_debrujin(kmers)

