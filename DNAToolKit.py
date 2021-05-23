Nuclotides=['A','C','T','G']
import collections

def validataSeq(dna_seq):
    temp_seq=dna_seq.upper()
    for nuc in temp_seq:
        if nuc not in Nuclotides:
            return False
    return temp_seq


def Counter_Of_Nucleotides(seq):
    # temp_seq={'A':0,'C':0,'T':0,'G':0}
    # for nuc in seq:
    #     temp_seq[nuc]+=1
    # return temp_seq
    return dict(collections.Counter(seq))