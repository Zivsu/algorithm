'''
	insert sort
'''




def sort(seq):
    for i in range(1, len(seq)):
        item = seq[i]
        idx = i
        while idx > 0 and seq[idx - 1] > item:
            seq[idx] = seq[idx - 1]
            idx = idx - 1
        seq[idx] = item
    return seq
    

def sort_concise(seq):
	for i in range(1, len(seq)):
		while seq[i] < seq[i-1] and i > 0:
			seq[i], seq[i-1] = seq[i-1], seq[i]
			i -= 1			
	return seq


if __name__ == '__main__':
	seq = [1,3,4,2,3,1]
	print sort(seq)	
