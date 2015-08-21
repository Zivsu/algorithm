
'''
    quick sort
'''


def sort(seq):

    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    left, right = [], []
    for x in seq[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort(left) + [pivot] + sort(right)

def sort_concise(seq):
    if len(seq) <= 1:
        return seq
    return sort_concise([x for x in seq[1:] if x <= seq[0]]) + [seq[0]] + \
            sort_concise([x for x in seq[1:] if x > seq[0]])



if __name__ == '__main__':
    seq = [1,3,4,2,3,1]
    # print sort(seq)
    print sort_concise(seq)