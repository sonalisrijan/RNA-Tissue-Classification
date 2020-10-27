# Code to train neural network
from joblib import load, dump
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import re
import seaborn as sns
import sys
from sklearn.preprocessing import label_binarize 
from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split, learning_curve
from sklearn.metrics import accuracy_score, confusion_matrix, multilabel_confusion_matrix, plot_confusion_matrix, classification_report, precision_score, recall_score
import torch
from torch import optim
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset

from prepare_data import prepare_data
from calculate_metrics import calculate_metrics
from neural_network_model import Enum
from neural_network_model import NN

arab_mapping, X_arab, Y_arab, arab_req_sra_ids = prepare_data("../../data/ml_files/Arabidopsis/arab_universal_singe_copy_genes.txt", "../../data/ml_files/Arabidopsis/trianing_samples.txt", "../../data/ml_files/Arabidopsis/Training_data1.txt", "../../data/arab_data_distribution.png")
arab_test_mapping, X_arab_test, Y_arab_test, arab_test_sra_ids = prepare_data("../../data/ml_files/Arabidopsis/arab_universal_singe_copy_genes.txt", "../../data/ml_files/Arabidopsis/testing_samples.txt", "../../data/ml_files/Arabidopsis/Testing_data.txt", "../../data/arab_data_distribution.png")
X_train, X_validation, Y_train, Y_validation = train_test_split(X_arab, Y_arab, test_size=0.1, random_state=42, stratify=Y_arab)

train_dataset = Enum(X_train, Y_train)
val_dataset = Enum(X_validation, Y_validation)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32,shuffle=True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=32,shuffle=True)

## Defining loss function and optimizer
loss_function = nn.CrossEntropyLoss()
# optimizer = optim.SGD(model.parameters(), lr=0.0001, weight_decay= 1e-6, momentum = 0.9, nesterov = True)
optimizer = optim.Adam(model.parameters(), lr=0.0001, weight_decay=1e-6)

epoch_train_losses, epoch_val_losses = [], []
epoch_train_micro, epoch_val_micro = [], []
epoch_train_macro, epoch_val_macro = [], []

for epoch in range(30): ## run the model for 30 epochs
    train_loss, valid_loss = [], []
    train_micro, val_micro = [], []
    train_macro, val_macro = [], []
    
    for data, target in train_loader:
        optimizer.zero_grad()
        output = model(data.float())
        loss = loss_function(output, target)
        loss.backward()
        optimizer.step()
        train_loss.append(loss.item())
        predicted_classes = torch.argmax(output, dim=1) 
        micro = precision_score(predicted_classes, target, average='micro') 
        macro = precision_score(predicted_classes, target, average='macro') 
        train_micro.append(micro.item())
        train_macro.append(macro.item())
        
    ## evaluation part 
    model.eval()
    for data, target in val_loader:
        output = model(data.float())
        loss = loss_function(output, target)
        valid_loss.append(loss.item())

        predicted_classes = torch.argmax(output, dim=1) 
        micro = precision_score(predicted_classes, target, average='micro') 
        macro = precision_score(predicted_classes, target, average='macro') 
        val_micro.append(micro.item())
        val_macro.append(macro.item())
    
    epoch_train_losses.append(np.mean(train_loss))
    epoch_val_losses.append(np.mean(valid_loss))
    
    epoch_train_micro.append(np.mean(train_micro))
    epoch_val_micro.append(np.mean(val_micro))
    
    epoch_train_macro.append(np.mean(train_macro))
    epoch_val_macro.append(np.mean(val_macro))

# Plotting results
plt.plot(e, epoch_train_losses)
plt.plot(e, epoch_val_losses)
plt.title('Loss curve')
plt.legend(['Train', 'Val'], loc='upper right')
    
plt.plot(e, epoch_train_micro)
plt.plot(e, epoch_val_micro)
plt.title('Micro-precision evolution during training')
plt.legend(['Train', 'Val'], loc='lower right')
plt.savefig('./micro_curve.png')

plt.plot(e, epoch_train_macro)
plt.plot(e, epoch_val_macro)
plt.title('Macro-precision evolution during training')
plt.legend(['Train', 'Val'], loc='lower right')
plt.savefig('./macro_curve.png')

# Saving model
torch.save(model.state_dict(), './pytorch_nn.sav')

# # Testing on rice data
# rice_mapping, X, Y, rice_req_sra_ids = prepare_data("../../data/ml_files/Rice/rice_universal_singe_copy_genes.txt", "../../data/ml_files/Rice/final_mapping.txt", "../../data/ml_files/Rice/combined_files_Norm.Log2.txt", "../../data/rice_data_distribution.png")
# test_input = (torch.tensor(X)).float()
# print (type(test_input))
# test_output = model(test_input)

# reverse_ordered =  {0:'flower', 1:'leaf', 2:'root', 3:'seed', 4:'seedling', 5:'shoot', 6:'silique', 7:'stem'}
# predictions = []
# for a in range(len(test_output)):
#     idx=np.argmax(test_output.data.numpy()[a]) 
#     predictions.append(reverse_ordered[idx])
    

