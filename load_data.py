import os
import sys

import torch
import torchvision


imagenet_data = torchvision.datasets.ImageNet('/data/ImageNet', split='val', download=False)
