import torch
import torchvision

from learnergy.models.drbm import DRBM

# Creating training and testing dataset
train = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=torchvision.transforms.ToTensor())
test = torchvision.datasets.MNIST(
    root='./data', train=False, download=True, transform=torchvision.transforms.ToTensor())

# Creating a DRBM
model = DRBM(n_visible=784, n_hidden=500, n_class=10, steps=1, learning_rate=0.05,
            momentum=0, decay=0, temperature=1, use_gpu=True)

# Training a DRBM
mse, pl = model.fit(train, batch_size=128, epochs=50)

# # Reconstructing test set
# rec_mse, v = model.reconstruct(test)

# # Saving model
# torch.save(model, 'model.pth')

# # Checking the model's history
# print(model.history)