import torchvision
from learnergy.models.rbm import RBM
from torch.utils.data import DataLoader

if __name__ == '__main__':
    # Creating training and testing dataset
    train = torchvision.datasets.MNIST(
        root='./data', train=True, download=True, transform=torchvision.transforms.ToTensor())
    test = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=torchvision.transforms.ToTensor())

    # Creating training and testing batches
    train_batches = DataLoader(train, batch_size=128, shuffle=True, num_workers=1)
    test_batches = DataLoader(test, batch_size=10000, shuffle=True, num_workers=1)

    # Creating an RBM
    model = RBM(n_visible=784, n_hidden=4096, steps=1,
                learning_rate=0.1, momentum=0, decay=0, temperature=1, use_gpu=True)    

    # Training an RBM
    mse, pl = model.fit(train_batches, epochs=5)

    # Reconstructing test set
    rec_mse, v = model.reconstruct(test_batches)

    # Checking the model's history
    # print(model.history)
