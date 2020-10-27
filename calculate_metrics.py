import pickle
import sys
import re
from joblib import load, dump
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score, train_test_split, learning_curve
from sklearn.metrics import accuracy_score, confusion_matrix, multilabel_confusion_matrix, plot_confusion_matrix, classification_report, precision_score, recall_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_fscore_support

# orderedClasses =  ['flower', 'leaf', 'root', 'seed', 'seedling', 'shoot', 'silique', 'stem']

def calculate_metrics(Y_pred, Y_true, metrics_fig_name, confusion_matrix_fig_name, orderedClasses):
    """Params:
    1. classifier: str path to Trained and saved classifier 
    2. X: expression matrix corresp to Y_true
    3. Y_true: gorund truth of data 
    4. metrics_fig_name: str path+name of class-wise metrics fig to be saved
    5. confusion_matrix_fig_name: str path+name of confusion matrix fig to be saved
    6. orderedClasses: array of class names 
    Function: 
    1. Predicts (and returns) Y_pred using trained model
    2. Outputs class-wise and overall metrics
    3. Saves class-wise metrics barplot, confusion matrix
    """
    micro_precision = precision_score(Y_true, Y_pred, average='micro') 
    macro_precision = precision_score(Y_true, Y_pred, average='macro') 
    class_wise_precision = precision_score(Y_true, Y_pred, average=None)
    class_wise_recall = recall_score(Y_true, Y_pred, average=None)
    
    print ("Accuracy is: %.3f" %micro_precision)
    print ("Macro precision is: %.3f" %macro_precision)
    print ("Class wise Precision:")
    print (class_wise_precision)
    print ("Class wise recall")
    print (class_wise_recall)

    #---- Precision Recall barplot
    indices = [1, 2, 3, 4, 5, 6, 7, 8]
    width = np.min(np.diff(indices))/3 # Calculate optimal width
    tick_label = orderedClasses
    fig = plt.figure()
    plt.title('Precision and Recall values for each class') 
    ax = fig.add_subplot(111)
    ax.bar(indices-width, class_wise_precision, width,color='b', label='Precision', tick_label=tick_label)
    ax.bar(indices, class_wise_recall, width,color='r',label='Recall', tick_label=tick_label)
    plt.xlabel('Classes') 
    plt.ylabel('Score') 
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='upper left',
               ncol=2, mode="expand", borderaxespad=0.)
    plt.grid()
#     plt.savefig(metrics_fig_name)
    plt.show()
    
    #---- Confusion matrix plot
    cf_matrix = confusion_matrix(Y_true, Y_pred, labels=orderedClasses)
    ax = sns.heatmap(cf_matrix, annot=True, fmt='g',cmap='Blues', 
                xticklabels=orderedClasses,
               yticklabels = orderedClasses)
    ax.set_title('Confusion Matrix')
    plt.xlabel('Predicted Labels', fontsize = 10)  
    plt.ylabel('True Labels', fontsize = 10) 
#     plt.savefig(confusion_matrix_fig_name)
    plt.show()
    
#     return Y_pred
    