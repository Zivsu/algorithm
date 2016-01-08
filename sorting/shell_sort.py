# !/usr/bin/python
# coding:utf8

"""shell sort"""

def sort(seq):
	length = len(seq)
	gap = length // 2
	while gap:
		for i in range(gap, length):
			while seq[i] < seq[i-gap] and i >= gap:
				seq[i], seq[i-gap] = seq[i-gap], seq[i]
				i -= gap
		gap = gap // 2
	return seq

if __name__ == '__main__':
	seq = [1,3,4,2,3,1]
	print sort(seq)
