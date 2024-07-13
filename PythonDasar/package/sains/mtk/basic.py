def add(*args):
    hasil = 0
    for data in args:
        hasil += data

    return hasil

def times(*args):
    hasil = 1
    for data in args:
        hasil *= data

    return hasil