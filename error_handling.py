import sys
import random
import re
import os


filename = "/Users/tatanavolkova/Desktop/python/prom.txt"

dna = ["A", "G", "C", "T"]

def create_snp_or_indel(seq, number):
    for i in range(number):
        pos = random.randint(1, len(seq)-1)
        primary = seq[pos]
        snp = random.choice(dna)
        print('{} {} {}'.format('SNP_'+primary+'_to_'+snp, 'at pos', pos))


def make_snp_loop(seq_id, dna):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    primary = dna[mutation_site]
    snp = random.choice(["A", "G", "C", "T"])
    dna_list[mutation_site] = snp
    print('{:>22} {} {:>8} {} {}'.format(seq_id, '|', primary + '_to_' + snp, '|', mutation_site))
    return ''.join(dna_list)


def process_line(seq_id, dna, number):
    for i in range(int(number)):
        new_seq = make_snp_loop(seq_id, dna)
        dna = new_seq
    return new_seq



def process_whole_file(filename, number):

    with open(filename) as f:
        print('{:>22} {} {} {} {}'.format('SEQ_ID', '|', 'MUTATION', '|', 'POSITION-OF-MUTATION'))

        for line in f:
            line = line.strip()

            seq_id, seq = re.split(r'\s+', line)
            if int(number) > len(seq):
                number = len(seq)
                print(
                    'Warning: X in SNPX is bigger than the length of the shortest string in a file. X is assigned to the length of the current string in a file.', number)
            process_line(seq_id, seq, number)



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: script.py <path_to_file> <SNP> <number>")
        exit()

    filename = sys.argv[1]
    number = re.findall(r'\d+', str(sys.argv[2]))[0]

    try:
        process_whole_file(filename, number)

    except FileNotFoundError as error:
        print('No such file')










#if file does not exist - make an exception
#if the number is bigger than the length of string - exception

