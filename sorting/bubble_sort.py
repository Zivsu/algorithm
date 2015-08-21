
'''
	bubble sort
'''

def sort(seq):
    length = len(seq)
    swap = False
    for _ in range(length):
        for n in range(1, length):
            if seq[n] < seq[n - 1]:
                seq[n - 1], seq[n] = seq[n], seq[n - 1]
                swap = True
        if not swap:
        	break
    return seq


def sort_concise(seq):
	for _ in range(len(seq)):
		for n in range(1, len(seq)):
		    if seq[n - 1] > seq[n]:
		    	seq[n - 1], seq[n] = seq[n], seq[n - 1]
	return seq
	

if __name__ == '__main__':
	# seq = [1,3,4,2,3,1]
	seq = []
	print sort(seq)
	print sort_concise(seq)



    