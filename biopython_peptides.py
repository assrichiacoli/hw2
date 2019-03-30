import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


def add_Ns(sequence):
    mod = len(sequence)%3

    if mod != 0:
        return str(sequence + 'N'*(3-mod))
    else:
        return str(sequence)

def truncate(a):
    if len(a) > 25:
        return str(a[:20] + '...' + a[len(a)-5:])
    else:
        return a

def translate(sequence):
    for i in range(3):
        forward = Seq(add_Ns(sequence[i:]), generic_dna)
        print('{:<30} {} {} {:<30} {}'.format(truncate(forward), 'forward from', str(i+1)+'th', 'nucleotide', truncate(forward.translate(to_stop=False))))
    for i in range(1,4):
        rev = Seq(sequence[:-i]).complement()
        reverse = Seq(add_Ns(rev), generic_dna)
        print('{:<30} {} {} {:<16} {}'.format(truncate(reverse), 'reverse complementary from', str(i)+'th', 'nucleotide', truncate(reverse.translate(to_stop=False))))

def main(x):
    print('All possible peptides (* replaces stop-codon):')
    translate(x)


if __name__ == '__main__':
    main('AGTACTAGAGCATTCTATGGAG')