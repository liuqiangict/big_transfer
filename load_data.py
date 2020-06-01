import os
import sys

import torch
import torchvision


imagenet_data = torchvision.datasets.ImageNet('./data/', split='val', download=True)
#imagenet_data = torchvision.datasets.ImageNet('/data/ImageNet', split='train', download=False)
print(imagenet_data)
