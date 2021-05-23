from DNAToolKit import  *
import  random
randomDNAString =''.join([random.choice(Nuclotides)for nuc in range(20)])
print (validataSeq(randomDNAString))
print (Counter_Of_Nucleotides(randomDNAString))
