# To make tsne plot, ensure that you have the singe_copy_genes files (produced by find_arabidopsis_pairwise_orthologs.py) for each plant that you're plotting. 

from joblib import load, dump
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
from scipy import linalg
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from sklearn import preprocessing 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.manifold.t_sne import _joint_probabilities
from sklearn.manifold import TSNE
from sklearn.metrics import pairwise_distances
import sys

from prepare_data import prepare_data

sns.set(rc={'figure.figsize':(11.7,8.27)})
palette = sns.color_palette("bright", 31) # here, 31 = total #classes
# Arabidopsis: 8; Rice: 7; Maize: 8; Tomato: 8;  >> Total=31 classes
orderedClasses =  ['flower', 'leaf', 'root', 'seed', 'seedling', 'shoot', 'silique','stem']

# Reading all expression data
arab_mapping, X_arab, Y_arab, arab_req_sra_ids = prepare_data("../../data/ml_files/Arabidopsis/arab_universal_singe_copy_genes.txt", "../../data/ml_files/Arabidopsis/trianing_samples.txt", "../../data/ml_files/Arabidopsis/Training_data1.txt", './fig')
print ("Read Arabidopsis training data")
rice_mapping, X_rice, Y_rice, rice_req_sra_ids = prepare_data("../../data/ml_files/Rice/rice_universal_singe_copy_genes.txt", "../../data/ml_files/Rice/final_mapping.txt", "../../data/ml_files/Rice/combined_files_Norm.Log2.txt", "fig_name")
print ("Read Rice data")
maize_mapping, X_maize, Y_maize, maize_req_sra_ids = prepare_data("../../data/ml_files/Maize/maize_universal_singe_copy_genes.txt", "../../data/ml_files/Maize/final_mapping.txt", "../../data/ml_files/Maize/combined_files_Norm.Log2.txt", "fig_name")
print ("Read Maize data")
tomato_mapping, X_tomato, Y_tomato, tomato_req_sra_ids = prepare_data("../../data/ml_files/Tomato/tomato_universal_singe_copy_genes.txt", "../../data/ml_files/Tomato/final_mapping.txt", "../../data/ml_files/Tomato/combined_files_Norm.Log2.txt", "fig_name")
print ("Read Tomato data")


# Preparing a mega X for combined tSNE plot: Trying different marker shapes 

def append_speacies_tag(Y, name):
    """name is a string indicating species of the input Y"""
    new_Y = []
    for item in Y:
        new_Y.append(item + "_" + name)
    return new_Y

new_X = np.concatenate((X_arab, X_rice, X_tomato, X_maize))
arab_classes = append_speacies_tag(Y_arab, "arab")
rice_classes = append_speacies_tag(Y_rice, "rice")
tomato_classes = append_speacies_tag(Y_tomato, "tomato")
maize_classes = append_speacies_tag(Y_maize, "maize")

Y = []
Y.extend(arab_classes)
print (len(Y))
Y.extend(rice_classes)
print (len(Y))
Y.extend(tomato_classes)
print (len(Y))
Y.extend(maize_classes)
print (len(Y))

np.save('./X_all_for_tSNE', new_X)
np.save('./Y_all_for_tSNE', Y)


a4_dims = (20, 15)
fig, ax = plt.subplots(figsize=a4_dims)
markers = {'flower_arab':'s', 'flower_rice':'X', 'flower_tomato':'o', 'flower_maize':'^',
           'leaf_arab':'s', 'leaf_rice':'X', 'leaf_tomato':'o', 'leaf_maize':'^',
           'root_arab':'s', 'root_rice':'X', 'root_tomato':'o', 'root_maize':'^',
           'seed_arab':'s', 'seed_rice':'X', 'seed_tomato':'o', 'seed_maize':'^',
           'seedling_arab':'s', 'seedling_rice':'X', 'seedling_tomato':'o', 'seedling_maize':'^',
           'silique_arab':'s', 'silique_tomato':'o', 'silique_maize':'^',
           'shoot_arab':'s', 'shoot_rice':'X', 'shoot_tomato':'o', 'shoot_maize':'^',
           'stem_arab':'s', 'stem_rice':'X', 'stem_tomato':'o', 'stem_maize':'^'}

sns.scatterplot(x="first_axis", y="second_axis", data=new_df, hue='tissue', ax=ax,  legend="full", markers=markers, style="tissue",
                palette=dict(flower_arab='#ff3300', flower_rice='#ff3300', flower_tomato='#ff3300', flower_maize='#ff3300',
                            leaf_arab='#50CD37', leaf_rice='#50CD37', leaf_tomato='#50CD37', leaf_maize='#50CD37',
                            root_arab='#A56B2B', root_rice='#A56B2B', root_tomato='#A56B2B', root_maize='#A56B2B',
                            seed_arab='#000000', seed_rice='#000000', seed_tomato='#000000', seed_maize='#000000',
                            seedling_arab='#0730C9', seedling_rice='#0730C9', seedling_tomato='#0730C9', seedling_maize='#0730C9',
                            silique_arab='#E78AF9', silique_tomato='#E78AF9', silique_maize='#E78AF9',
                            shoot_arab='#3AC0FF', shoot_rice='#3AC0FF', shoot_tomato='#3AC0FF', shoot_maize='#3AC0FF',
                            stem_arab='#E2EB2C', stem_rice='#E2EB2C', stem_tomato='#E2EB2C', stem_maize='#E2EB2C'))                  
ax.set_xlabel("tSNE-1")
ax.set_ylabel("tSNE-2")
plt.title("Arabidopsis, Rice, Tomato and Maize Dataset: tSNE")

