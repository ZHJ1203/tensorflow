

import os


def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")

    f.close()
    o.close()
    l.close()


path = os.path.join(os.path.abspath(os.getcwd()))

mnist_train_images = os.path.join(path, "train-images.idx3-ubyte")
mnist_train_labels = os.path.join(path, "train-labels.idx1-ubyte")
mnist_test_images = os.path.join(path, "t10k-images.idx3-ubyte")
mnist_test_labels = os.path.join(path, "t10k-labels.idx1-ubyte")

convert(mnist_train_images, mnist_train_labels, "mnist_train.csv", 60000)
convert(mnist_test_images, mnist_test_labels, "mnist_test.csv", 10000)
