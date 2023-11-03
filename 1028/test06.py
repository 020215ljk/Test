import pickle
import matplotlib.pyplot as plt


def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data


data_dir = '../fileAll/data/'

batch_1 = unpickle(data_dir + 'data_batch_1')

data = batch_1[b'data']
labels = batch_1[b'labels']

print(type(data))
print(type(labels))

for i in range(10):
    image = data[i].reshape(3, 32, 32).transpose(1, 2, 0)
    label = labels[i]

    plt.subplot(2, 5, i + 1)
    plt.imshow(image)
    plt.title(f'Label: {label}')

plt.show()
