def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


b = unpickle("../fileAll/data/data_batch_1")

print(type(b))

for value in b.values():
    print(value)
