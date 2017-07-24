import copy
import operator
from Bio.Seq import Seq
import re
from string import maketrans

try:
    f = open('dna2.fasta', 'r')
except IOError:
    print("The file dna.example.fasta doesnot exists!!")




def count_seq(f):
    seq = {}
    for line in f:
        line = line.strip()
        if line[0] == '>' :
        #if line.startswith('>'):
            #print line
            words =line.split()
            name =words[0] [1:]
            seq[name] = ''
        else :
                seq[name] = seq[name] + line
    return seq



def rt_key(dict, value):
    return (k for k,v in dict.iteritems() if v == value)

def reverse_string(sequence):
    return sequence[::-1]

def compliment(sequence):
    """ Returns complimentary sequence string"""
    basecompliment = {'A':'T', 'C':'G', 'T':'A', 'G':'C','N':'N','n':'n','a':'t','t':'a','c':'g','g':'c'}
    letters = list(sequence)
    letters =[basecompliment[base] for base in letters]
    return ''.join(letters)

def revComp(sequence):
    """ Returns reverse compliment of sequence"""
    sequence =reverse_string(sequence)
    sequence =compliment(sequence)
    return sequence

def revcomp(dna_seq):
    return dna_seq[::-1].translate(maketrans("ATGC","TACG"))

def orfs(dna):
    return max(re.findall(r'ATG(?:(?!TAA|TAG|TGA)...)*(?:TAA|TAG|TGA)',dna), key = len)



def has_stop_codon(sequence, frame):
    """ returns boolean for presence of stop codon"""
    stop_codon_found =False
    stop_codon = ['tga', 'tag', 'taa']
    for i in range(frame,len(sequence),3):
        codon = sequence[i:i+3].lower()
        if codon in stop_codon:
            stop_codon_found =True
            break
    return stop_codon_found


def has_start_codon(sequence, frame):
    """ returns boolean for presence of start codon"""
    start_codon_found =False
    for i in range(frame,len(sequence),3):
        codon = sequence[i:i+3].lower()
        if codon == 'atg':
            start_codon_found =True
            break
    return start_codon_found

def getting_rf(dna_seq,f):
    return dna_seq[f:]



#################################################################

length_dict={}



for k, v in count_seq(f).iteritems():
    v = getting_rf(v, 0)
    if has_start_codon(v, 0):
        if has_stop_codon(v, 0):
            #print len(v)
            print (orfs(v))
    length_dict.update({k: len(v)})
    print "Lenght : %d" % len(length_dict)


for k, v in length_dict.iteritems():
    print k, v





##############################################################
v_max = length_dict[max(length_dict, key=length_dict.get)]
k_max = max(length_dict, key=length_dict.get)
print "Max length seqid %s and length is $d:" %  k_max,v_max

v_min = length_dict[min(length_dict, key=length_dict.get)]
k_min = min(length_dict, key=length_dict.get)
print "Min length seqid %s and length is $d:" %  k_min,v_min

uniqueValues = set(length_dict.values())
if v_max in uniqueValues :
    print "Maximum value is unique!!!"
else:
    print "Maximum value is not unique!!!"# for key, value in seq.items()}

if v_min in uniqueValues :
    print "Minimum value is unique!!!"
else:
    print "Minimum value is not unique!!!"# for key, value in seq.items()}


for k in rt_key(length_dict, v_max):
    print "Seq Name of longest seq : %s" % k

for k in rt_key(length_dict, v_min):
    print "Seq Name of shortest seq : %s" % k
