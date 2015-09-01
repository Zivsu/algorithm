
'''select sort
'''

def sort(seq):
	for i in range(len(seq)):
		min = i
		for j in range(i, len(seq)):
			if seq[j] < seq[min]:
				min = j
		if i != min:		
			seq[i], seq[min] = seq[min], seq[i]
	return seq
	
if __name__ == '__main__':
	seq = [1,3,4,2,3,1]
	print sort(seq)
