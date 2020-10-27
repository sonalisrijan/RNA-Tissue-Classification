import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import re
import sys

orderedClasses =   ['flower', 'leaf', 'root', 'seed', 'seedling', 'shoot', 'silique','stem']

def prepare_data(species_universal_SCG, tissue_info, expn_data_file, fig_name):
    """Params: 
    1. species_universal_SCG file: str path to file containing names of all single copy genes for current species (separator=" ")
    2. tissue_info: str path to file with sra and corresp tissue written on each line; SEPARATOR bw sra and tissue MUST BE " "
    3. expn_data_file: str path to expression data (tab separated) file
    4. fig_name: str path+name for distribution plot to be saved
    Function:
    Prepares data: Extracts only Universal single genes, orderedClasses from data; 
    1. Returns the X, Y, (sra>>tissue) mapping dictionary, sra list in order of appearance in X,Y file
    2. Shows the distribution barplot for data for orderedClasses
    """
    orderedClasses =   ['flower', 'leaf', 'root', 'seed', 'seedling', 'shoot', 'silique','stem']
    singe_copy_genes = open(species_universal_SCG, 'r')
    tissue_info = open(tissue_info, 'r')
    data_file = pd.read_csv(expn_data_file, sep="\t")
    expn_data_file = data_file.replace(float('-inf'), 0)
    sample_ids_ordered = list(expn_data_file.columns)
    
#     print ("Expn_data_file shape:")
    print (expn_data_file.shape)
    print ("Length of sample_ids_ordered: %d" %(len(sample_ids_ordered)))
    
    for line in singe_copy_genes:
        universal_genes_list = line.split()
    print ("Number of universal single-copy genes is %d" %(len(universal_genes_list)))
    
    #----- Making the mapping dictionary
    tissues_to_sample_ids={}
    for line in tissue_info:
        sra=line.split()[0]
        tissue=line.split()[1]
        tissues_to_sample_ids[sra]=tissue
#     print ("Mapping dictionary length is %d" %(len(tissues_to_sample_ids)))
    
    #----- Getting sra_ids from tissues of interest
    needed_labels = orderedClasses
    req_sra_ids = []
    req_labels = []
    for item in sample_ids_ordered:
        label = tissues_to_sample_ids[item]
        if label in needed_labels:
            req_sra_ids.append(item)
            req_labels.append(label)
#     print ("Len of req_sra_ids is %d and len of req_labels is %d" %(len(req_sra_ids), len(req_labels))) 
    
    #----- Extracting tissues of interest expn data
    req_df = pd.DataFrame()
    for item in req_sra_ids:
        req_df[item] = expn_data_file[item]
    
    #----- Extracting info from genes of interest
    req_df_transposed = req_df.transpose()
    df = pd.DataFrame()
    for item in universal_genes_list: # for every universal SCG
        for gen in req_df_transposed.columns: # these are genes
            if item==gen:
                df[item] = req_df_transposed[item]
    df = df.to_numpy()
    
    #----- Making distribution barplot
    distrib_dict={}
    for item in orderedClasses:
        distrib_dict[item]=0   
    for item in req_labels:
        distrib_dict[item]+=1
    keys = list(distrib_dict.keys())
    values = list(distrib_dict.values())
    plt.barh(keys, values)
    for index, value in enumerate(values):
        plt.text(value, index, str(value))
    plt.show()

    return (tissues_to_sample_ids, df, req_labels, req_sra_ids)
