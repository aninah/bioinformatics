#make a function that takes in a string
#and returns all the kmers in the string in alphabetical order
def string_comp(dna_str,k):
	final = []
	final_str = ""
	for i in range(len(dna_str)-k+1):
		final.append(dna_str[i:i+k])
	a = sorted(final)
	for i in a:
		final_str+=i+"\n"
	return final_str

b=string_comp("AGCCAAACCAGATCCCCTCAACTCTGCCTTCTGGGCCTAAACCCAGAAATTAGTCTCTTAGTAGTTAAAAGCGTTGTGACGCGCCCGGGTATGCGTATCGCCCAGAAGAGGGTTAAGCAGGTTCGCTCCAACGACGCTGTTGAAGTCGTCCATGCCCAGTCCCGACTAAGCCGAAGATCGGAGCAAGAAAGTCGCTGCACGAGGCGTAGGTGTGAAGCCTAACAGTGGCCTTATGGGGATGTCGGGCCCTATGGTCTACAGAAGCATGCTCGCCATATCCCGCTTCCTTGAGGCCACCCAAAGACGCTTAAGTTGGGTGAGGAAGAGTCCCTATCTTTGCAAAGATGCACCCTTCGGGCTGTGAATTTCGTTATTGCAAGCCGGTGCGCTGTGACCATCCATGTTATTGGCGTTGCGTTCCAGTAGGATTACCCCTAGCTCACAGCGAAAAGTGGGATGCGGAAGTAGTCTGAACACAGTGTTCTGCTGCCTCTAGATGCTGAACAACGGGCGACCGGAACCTGGAATGGAAATAAAAGCTACTAGGATATACGATAACCAGGGGTTTCCTTTGGCGGAATACCTCATCCGCAGCTAAGTGCAGTTAGCGAGCATATAGCTAAGGTCTACGGCGATGTACTATACCGCGGCCCGATCATGTGTCGCTAGTGGTGATCGGTAGATTGTCCATGTAATTGCCATGAACAGTAGTAGGTCTGTGAAACTCGCAACTACCCTGCACGCCAAAGTAGATACGCCCGTGTAGTACTCCGGCGTTATTACTTCGATGACGTCCTCTTGCGCCCGGATTATGAGGGCACCGGGTTATAGTGTAACGGAATGTACAAACAGTTTCCCGAATCAACGGTTGCGACTGTACCCCCCGACAACTCGCTTTGACGTGTTTAGGCGATTCTATCAAAGCCAGGTGGCCCGAGCCTGGTTTACCAATTCTTGCTTAGATAGAGATGGCGGCATAGAAACTGGGTTAACGGCTCTTTACGGCGTACACAGGCAAAGTGGCGGGCAGATTAATGATGGGCGATACCTCTCTACGTTAACCATGACCCTACTCCAGTTTTTTAAATAGATCTGAGGTGACGTAAATCATTTACGGAGATGACGTCGGCCTTCTCGAGCGATATTTCGTATGTCTCATGTAAGGTAATGGTATACTCGGAAACATATTTGCACAGTGATCGTGCGACGTTCGAAACCCTCTGCGTAGTAACGTGCGCGATGCATACATATCTCCTCTTGTATTTCACCACAGAAGCTTCGGCTAACTGAACATCCAGGCCAATTAATCCGGAAAGACTTCTAGCCATGAGTCCTGGTAAGGCCACCTCATAAGCAAGCAGAGCGCTCGTCACGATTAGTTGGGCGTTAGCGCGCCTTCAGAGCGACAACTCTCATTCCAGCCTATACTGTATAACCCTATAACACTGAAAAAGGGCCATGCGAGGCCCCCTATATTGCCCTTAGCGAAATGCCGAGATTTAAAAGTCAGATACCCCGACATTTTACTGGGTGACTTAGTTCTCTTGCAGTAATGAACTCGTACTACGGATTAGTAGCAAAACCTATGGTGTCTGTGTGACGCGCTGCCAGAACTAGCTCCACGAGAGAGGCGGGAACTTTCTATATCAGCAGCACCCGCGCTTGGTGAAGTATTTAGGAGATGGGGTGTTTCGACAGTTGTACAGGTAACTATTGATCCTCTATGTGGTACACACCCGTTTTGCATACGGACTACTGAGTAGGCCCTGCACACTCGCTTGACTCGTACAGCCCGATATGGACCAGCTGATACTTAATGGATTCGGACATGGGCCGCGTTATGCTTGGGGCGTCGTACTACAAGACCTGACTTAGGAGGAATTATCCAGGAAGAACTTAACCCCTTTCACACGGCTCAGCCAAGTAGACCTGTGACTCCTCCCCCGCTACGTTCGACCGAGCGTGTGATAACATTCGGAGCGCGGGCTGCGTCATAAGTGGCGGCATCGTTAGTCCAGTAGCACTCCAGGCGCGACGCTGCATCTACAGATTACTATCATGGGTGATAGATTCCTCGGAACATTGCTATATCAAACGGACAGGTTCACGGCTTATGTGCATTTTACTAGCAGCCTACCCAATCGGTAAGAGCCGTCTGAAACCTCGGTAATATGTTTCTCTATATACGAGAATAGAAGAAGTGTCTCGTGAAAAGCTCAATAGTTCGAGCGTGAATGCTAAGTCTCGAATATGGAGAAGTCATCTAGCTAGGCTGATGATAGGATTTCGTGTTCTCGTTTTATGATGTTTCGGTACTCTTACCTCTCGTGGACCCGAAAGTGGCTGAAAACCCAACCAGACACCGATAATTCTGAACATGTCGCATTCAAAAGGCGACATTCGTGGGATACGTGAGGTGCTCTAACGAGTGCTCGTATTGTTGTCTAGCTGATACAACCGAGCTTACTTCCTCATCCACCAGCTTATACTAAGGTGGGGGCTTACGTCACCAACCCGCTGATCAGTATAGAGCTCCACTAATAGCAATCGGGTAGGACTTTAGAAACAAGGTATAGTTTTTGCGGTACCTTCGAAGTATTTTCTCACGTAACATTTCTAATAATACCACTTGCTTCCTCTCCGTCCGTGTGTAGGTATACACGTTGGCGCATACGCTCCACGTTGCAAGTACAAACGGTTTCTTAGTGTTTTTGCGGATTTATTTTACCGCAGTTTACTTCGGCCCCCTGAATGAAGGATGAGTCTGCTGCGTTATGACTAGCCCAGGTATCTGATCCACCCCCTCGGGTAGGCCTTGACAACCTAATACAAAGCTCCAGCTCGCGAGCTACCGCTAACTATGTATCCAAGGACACGCGACAGGTTCTTGCCACTGGGTGTCGCGGGGAAAATAGAGACGGACGCATCGTTACTGATGAGAAAGTACAGTGCAAGGTTAAAGACTGCGCGTTCGGCCGCCACATAATCAGAGAAAATCGTCAATGACCTGTTGAAAGAGCATCTTCTAGTCTACACCGGTTTGGCCGTTGTGTAAAGACGTCTCTTCCCTCATGATCAGGTCTCTAGCTACTGCTCACCACTGGGAGTAGATGTACCAGGTGTGAATGACTTATAAGCTTGGGTCTTGCGCGCCCCGATCTAAGAGCTGTCGACCTAACGTGGAGCGGAAACCGCTTTTACAAAAAAACCCCAAAGGGACCACACTACGGCCTTCGCAATAACGTACTCCCCAAACAAGGGACTACAGAAGTTAGTCCCCGCGGCGCCGCTGCTGTTGAGGGTAGGGCTACGTCCTATGGCGGGAGTGCCCTTGCATCGGGGTATAAAACGAAAACAGAACTTGAGGCGCTCGAGCGTATCTCAACACCCTATGTACGGCCAGGCGTATCCCATCGAATCGTTTGGCCCAATGAATGACGGACTGTGATGGGACGAGACCGCGTCCGGCATCTTCAACTGAATCACCTCGGCACTGAATCACCACCAAACGTAAGCCCAGGGAGGTAAGTTGATAACTTAGCCTGGGAAATAATCGCGGTCGACTAGTAAATGGCTCAACCATCGTGAACGGGCCGCTAGGCTCTGAGCCTTTACCCAGCCACGTAATTGTTGGCTGTGTTAACGCGGTCGGGCTTCAGATATCGTTTTCCTTACGATCCACCCATCTATATCAGAAGCGAATTTTCGACTGTTAGGCCTTGTTCAGGGGGCATTGTACGCTAAGCACAAACTCTGTCCGGTAATAGCCTACACGACGTACATAAGAATCCTCGGCCTGCAAGGTTTTTTGCTTGACATCGGGAACTAACTCTGTCGCTTCACCCTCTCTAGCACATGTCGACATACCATTAGTTACAAACGCGGGCGATGTCAGTCTTTTACCGTCCCTATTGGGTGGCTAGCTTCCAGTATTCCAGTGCCTATCCAAACGCTGACCTTACAACGCGGGTGGATGGGATATACGACTCCTATGTAACTCGTCGAAGTAGGGTGCTCGTCTTAACTGTTGGAGTGGTCCGGTTGGATCACATGCGCACCTCCGTGAATCCGGAGCGGGGGTCGCTACCCTTTAGTTCGCCAAAAATTCCCTCTGTTACGTTCAAAGCTATAGTGACGAATTGTGGCACTTTACATTAAGATGTCTGCACCTTAGGTCGATATTAGCGACCACAACACGGACGGGGAATTGACAGCAGACATGCTCCTTAATGGGACGCGTAATGTGTTACAGTCTGCAGTCTCAGTTATCTTTCGGCAACATCAGAAATTTGACAGGGACGGACGGAGGCTCCGTCGATGCACGTAAGGGGCTTCGAAACCACCAGGTCACGCGCTGCAGGGGGAGACTTTGTTACCCATGATGACGCGGACCCCACCTTGCGCCCCCGAGTATTGGAAACATTACCTGTTTCGAAATGTACAGAGGTCCAGGAGCCACACTAAGAAAGGGGATCTATGTCCCCGGGATTTCCCTCGGGCGTCACGGGTAAGTCGACATGGCCGCGCGTTCTGCCCGTACGGCCGTCACCGTACCTCTACACCTCGTCTTTGGAGTCCGCCACCACGGTGGTAGGGTTCCGCTGAGAATCTAACCACGTGTCCACAAGTTGTGCAGAACCGCATCAGTTAGATCACGCTCGCACGTGTTCATATCAGGAAGAGGCGGAGTAGTTGGTCCCCATTCGAGGGGTTGCCGGCGAGTGTTTCCCCGCGTATGCACGGATGCAGATAGAAGAGTAGAGGTTCATCGGAGAGATAAGACTGGTGTATAATTGGTAGACAAGGATGTGATCTGTAAAGGTTGATAAGACGCGAAGGAGAGATCGTACTAGATAATATTGTCCAAGAGGTATCCGTCTGGGACCTAACGCACGCGCACGGTCAACGTCTCCTGACATCTACATTAAAAAAGATATGTGGTTATTCAGTCTGGGGATTAAATATCTCGACACAACGCCGGGTTCACGGAGAATAACGTC",100)
print b
