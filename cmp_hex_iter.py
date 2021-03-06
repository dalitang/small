# iteratively compare two bytes (in hex mode) from two files
# and print the number of diff counts

def compare_binary_iter(f1, f2):
    """"""
    from itertools import izip # for python 2, if python 3, use zip
    counter = 0
    with open(f1, 'rb') as a, open(f2, 'rb') as b:
        for byte1, byte2 in izip(a.read(), b.read()):
            cmp1 = hex(ord(byte1))
            cmp2 = hex(ord(byte2))
            if not cmp1 == cmp2:
                counter += 1
