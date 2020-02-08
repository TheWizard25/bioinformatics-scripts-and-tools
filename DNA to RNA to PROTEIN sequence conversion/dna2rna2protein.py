import sys
dna_seq_input_file = sys.argv[2]							#INPUT FILE
protein_seq_output_file=sys.argv[4]							#OUTPUT FILE

rna_seq=""
with open(dna_seq_input_file, mode='r') as thisfile:
	content=thisfile.readlines()

count=0
for line in content:
	count+=1
	if(count>1):
		for letter in line:		
			if(letter=='A'):
				rna_seq+='U'
			elif(letter=='T'):								#DNA to RNA Conversion
				rna_seq+='A'
			elif(letter=='C'):
				rna_seq+='G'
			elif(letter=='G'):
				rna_seq+='C'
			else:
				rna_seq+='\n'


rna_seq=rna_seq.replace('\n','')

sequence=rna_seq
length=len(sequence)
numcodons=int(length/3)
start=['AUG']
stop=['UAA','UAG','UGA']
Ala= ['GCU', 'GCC', 'GCA', 'GCG']
Arg=['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
Asn=['AAU', 'AAC']
Asp=['GAU', 'GAC']	
Cys=['UGU', 'UGC']
Gln=['CAA', 'CAG']
Glu=['GAA', 'GAG']
Gly=['GGU', 'GGC', 'GGA', 'GGG']
His=['CAU', 'CAC']
Ile=['AUU', 'AUC', 'AUA']															#Assigning Codons to respective Amino Acids
Leu=['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
Lys=['AAA', 'AAG']
Met=['AUG']
Phe=['UUU', 'UUC']
Pro=['CCU', 'CCC', 'CCA', 'CCG']
Ser=['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
Thr=['ACU', 'ACC', 'ACA', 'ACG']
Trp=['UGG']
Tyr=['UAU', 'UAC']
Val=['GUU', 'GUC', 'GUA', 'GUG']

count=0
a=0
flag=0
protein_seq=""
for i in range(0,numcodons):
	codon=sequence[a]+sequence[a+1]+sequence[a+2]
	if codon in start:
		flag=1
	elif codon in stop:
		if(flag==1):
			break
	
	if(flag==1):
		if codon in Ala:
			protein_seq=protein_seq+'A'
			
		elif codon in Arg:
			protein_seq=protein_seq+'R'
			
		elif codon in Asn:
			protein_seq=protein_seq+'N'
			
		elif codon in Asp:
			protein_seq=protein_seq+'D'
			
		elif codon in Cys:
			protein_seq=protein_seq+'C'
			
		elif codon in Gln:
			protein_seq=protein_seq+'Q'
			
		elif codon in Glu:
			protein_seq=protein_seq+'E'
																						#Assigning corresponding protein code for the codon
		elif codon in Gly:
			protein_seq=protein_seq+'G'
			
		elif codon in His:
			protein_seq=protein_seq+'H'
			
		elif codon in Ile:
			protein_seq=protein_seq+'I'
			
		elif codon in Leu:
			protein_seq=protein_seq+'L'
			
		elif codon in Lys:
			protein_seq=protein_seq+'K'
			
		elif codon in Phe:
			protein_seq=protein_seq+'F'
			
		elif codon in Pro:
			protein_seq=protein_seq+'P'
			
		elif codon in Ser:
			protein_seq=protein_seq+'S'
			
		elif codon in Thr:
			protein_seq=protein_seq+'T'
			
		elif codon in Trp:
			protein_seq=protein_seq+'W'
			
		elif codon in Tyr:
			protein_seq=protein_seq+'Y'
			
		elif codon in Val:
			protein_seq=protein_seq+'V'
			
		elif codon in start:
			protein_seq=protein_seq+'M'
			
	a+=3


with open("SAMPLE_OUTPUT.fa", mode='w') as thisfile:											#Writing to an output file
	print("DNA sequence input:\n",content, file=thisfile)
	print("\n >RNA SQUENCE\n*************\n",rna_seq,"\n\n", file=thisfile)
	print("\n >Protein SQUENCE\n*****************\n",protein_seq, file=thisfile)


