import os
import random
import re


def fasta_gen(path_to_fasta: str):
    """ Generator for reading fasta file
    :param path_to_fasta: path to your file
    :return: tuple of seq ID and complete sequence for this read
    """
    ident = None
    with open(path_to_fasta, 'r') as file_fasta:
        for line in file_fasta:
            if line.startswith('>'):
                if ident:
                    yield ident, ''.join(sequence)
                ident = line.strip()
                sequence = []
            elif re.search(r'^[A-z]+', line):
                sequence.append(line.strip())


your_path = os.path.join('data', 'sequences.fasta')
data_seq = fasta_gen(your_path)


class FastaRead:
    def __init__(self, path_to_fasta, type_of_seq='dna'):
        """
        :param: path_to_fasta: path to your fasta file
        :param: type_of_seq: type of your sequences containing in file (dna, rna, amino, acid)
        """
        self.path_to_fasta = path_to_fasta
        self.type_of_seq = type_of_seq

        # define what kind of changes need depending on a type
        if type_of_seq == 'dna':
            self.changes = ['A', 'C', 'G', 'T']
        elif type_of_seq == 'rna':
            self.change = ['A', 'C', 'G', 'U']
        elif type_of_seq == 'amino_acid':
            self.change = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W',
                           'Y', 'V']
        else:
            raise 'Unknown type of sequence'

    def change_seq(self, seq_to_change: list):
        """
        :param: seq_to_change: list that contains one str sequence
        :return: change sequence in str format
        """
        len_seq = len(seq_to_change)
        # how many elements in sequence change
        el_ch = random.randint(0, len_seq % 5)
        while el_ch > 0:
            seq_to_change[random.randint(0, len_seq - 1)] = random.choice(self.change)
            el_ch -= 1
        return ''.join(seq_to_change)

    def __iter__(self):
        ident = None
        while True:
            with open(self.path_to_fasta, 'r') as fasta:
                for line in fasta:
                    if line.startswith('>'):
                        if ident:
                            # convert list of lines of sequence into one list, for correct work
                            # of function change_seq
                            yield self.change_seq(list(''.join(sequence)))
                        ident = line.strip()
                        sequence = []
                    elif re.search(r'^[A-z]+', line):
                        sequence.append(line.strip())


get_chaos = FastaRead(your_path, 'amino_acid')

