# Defining the neural network

from joblib import load, dump
import os
import sys
import torch
from torch import optim
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset

# Making Dataloader
orderedClasses =  {'flower':0, 'leaf':1, 'root':2, 'seed':3, 'seedling':4, 'shoot':5, 'silique':6,'stem':7}
class Enum(Dataset):
    def __init__(self, X_file, Y_file):
        self.X_file = X_file
        self.Y_file = Y_file

    def __len__(self):
        return len(self.X_file)
        
    def __getitem__(self, idx):
        sample = (self.X_file[idx], orderedClasses[self.Y_file[idx]])
        return sample 

class NN(nn.Module):
    def __init__(self):
        super().__init__()        
        self.fc1 = nn.Linear(2898, 1000)
        self.fc2 = nn.Linear(1000, 500)
        self.fc3 = nn.Linear(500, 8) # considering there are 8 classes
        
    def forward(self, X):
        x = F.leaky_relu(self.fc1(X)) # X is of dim = 2898 gene exp values
        x = F.leaky_relu(self.fc2(x))
        x = self.fc3(x)
#         print (x.shape)
        return x

