# This code trains and saves four models: SVM, XGB, KNN, Linear model

from joblib import load, dump
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import re
import seaborn as sns
from sklearn import preprocessing 
from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split, learning_curve
from sklearn.ensemble import VotingClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC  
from sklearn import linear_model
from sklearn.metrics import accuracy_score, confusion_matrix, multilabel_confusion_matrix, plot_confusion_matrix, classification_report, precision_score, recall_score
from sklearn.preprocessing import label_binarize 
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.multiclass import OneVsRestClassifier # We use OneVsRestClassifier for multi-label prediction
import sys
from xgboost import XGBClassifier

from prepare_data import prepare_data
from calculate_metrics import calculate_metrics

orderedClasses =  ['flower', 'leaf', 'root', 'seed', 'seedling', 'shoot', 'silique', 'stem']

arab_mapping, X, Y, arab_req_sra_ids = prepare_data("../../data/ml_files/Arabidopsis/arab_universal_singe_copy_genes.txt", "../../data/ml_files/Arabidopsis/trianing_samples.txt", "../../data/ml_files/Arabidopsis/Training_data1.txt", "../../data/arab_training_data_distribution.png")
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.1, random_state=42, stratify=Y)

# Train SVM and XGB
svm_classifier = SVC(random_state=42, kernel='poly', probability=True)
xgb_classifier = XGBClassifier(max_depth=3, objective='multi:softprob')
print ("Beginninng training SVM")
svm_classifier.fit(X_train, Y_train)
print ("Beginninng training XGB")
xgb_classifier.fit(X_train, Y_train)
print ("Training complete")
dump(svm_classifier, './proba_svm_model.sav')
dump(xgb_classifier, './proba_xgb_model.sav')

# Train KNN and Linear
binarized_Y = label_binarize(Y, orderedClasses)
X_train_bin, X_validation_bin, Y_train_bin, Y_validation_bin = train_test_split(X, binarized_Y, test_size=0.1, random_state=42, stratify=Y)
knn_classifier = KNeighborsClassifier(n_neighbors=3)
linear_classifier = OneVsRestClassifier(linear_model.LinearRegression())
print ("Beginninng training KNN")
knn_classifier.fit(X_train_bin, Y_train_bin)
print ("Beginninng training Linear")
linear_classifier.fit(X_train_bin, Y_train_bin)
print ("Training complete")
dump(knn_classifier, './proba_knn_model.sav')
dump(linear_classifier, './proba_linear_model.sav')

