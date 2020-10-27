# Dtd Jun 10, 2020
# Author: Sonali Srijan
# Varala Lab, Purdue
# This file outputs txt files that hold single-copy ortholog genes that belong to Ortholog groups common to Arabidopsis, Maize, Tomato, Rice
# You should have input file: Orthogroups.txt 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ## To check single copy orthologs in Arabidopsis thaliana and Solanum lycopersicum
# ### For that, in all selected lines, there should be only one gene in Arabidopsis and only gene in Solanum 
# Note: There are 75026 lines (ortho-groups) in the file Orthogroups.txt

## Step 1: Filter and store all those lines where there is only one gene of Arabidopsis. This will be an important file named 'single_orthologs_arabidopsis.txt'. Since we're not considering Amborella trichopoda plant, we'll discard all the items starting with Ambtr in this saved file
## Step 2: From the above created file 'single_orthologs_arabidopsis.txt', we'll check which lines have Solanum genes occurring only once. We'll now save these lines in a final file named 'arab_sol_single_orthologs.txt'. 
## Step 3: From 'arab_sol_single_orthologs.txt' we'll extract the gene IDs and store them in separate files. 


# ## Step 1: Filter and store all those lines where there is only one gene of Arabidopsis. This will be an important file named 'single_orthologs_arabidopsis.txt'.

# single_orthologs_arabidopsis = open("./single_orthologs_arabidopsis.txt", "w")
# with open("../data/Orthogroups.txt", 'r') as ortho_data:
#     for line in ortho_data:
#         current_list = line.split()
#         print ("Current orthogroup is %s" %current_list[0])
        
#         for i in range (len(current_list)):
#             if 'Arath' in current_list[i]:
#                 if 'Arath' in current_list[i+1]:
#                     print ("No single copy ortholog genes of Arabidopsis")
#                     print ("\n")
#                     break
#                 else:
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     single_orthologs_arabidopsis.writelines(current_list)
#                     single_orthologs_arabidopsis.write("\n")
#                     print ("Written SCO genes to file")
#                     print ("\n")
# single_orthologs_arabidopsis.close()   
# count = 0
# with open('./single_orthologs_arabidopsis.txt', 'r') as f:
#     for line in f:
#         count += 1
# print("Total number of lines is: %d" %count)
# Total number of single ortholog genes in Arabidopsis is 7027.


# ---- TOMATO and ARABIDOPSIS
# arab_sol_single_orthologs = open("./arab_sol_single_orthologs.txt", "w")
# with open("./single_orthologs_arabidopsis.txt", 'r') as arabidopsis:
#     for line in arabidopsis:
#         current_list = line.split()
#         print ("Current orthogroup is %s" %current_list[0])
#         for i in range (len(current_list)): # all but the last element...  i = 0 to L-1
#             if i< len(current_list)-1:
#                 if (('Sol' in current_list[i]) and ('Sol' in current_list[i+1])):
#                     print ("Found multiple copies of ortholog genes for Sol")
#                     print ("\n")
#                     break
#                 elif (('Sol' in current_list[i]) and ('Sol' not in current_list[i+1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Sol found: Written SCO genes to file")
#                     print ("\n")
#                     arab_sol_single_orthologs.writelines(current_list)
#                     arab_sol_single_orthologs.write("\n")
#                     break                  
#             if i== len(current_list)-1: # last element
#                 if (('Sol' in current_list[i]) and ('Sol' in current_list[i-1])):
#                     print ("Found multiple copies of ortholog genes for Sol")
#                     print ("\n")
#                     break
#                 elif (('Sol' in current_list[i]) and ('Sol' not in current_list[i-1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Sol found: Written SCO genes to file")
#                     print ("\n")
#                     arab_sol_single_orthologs.writelines(current_list)
#                     arab_sol_single_orthologs.write("\n")
#                     break                         
# arab_sol_single_orthologs.close() 
# count = 0
# with open('./arab_sol_single_orthologs.txt', 'r') as f:
#     for line in f:
#         count += 1
# print("Total number of lines is: %d" %count)
# ##Total number of lines is: 5239


# ---- MAIZE and ARABIDOPSIS
# arab_zea_single_orthologs = open("./arab_zea_single_orthologs.txt", "w")
# with open("./single_orthologs_arabidopsis.txt", 'r') as arabidopsis:
#     for line in arabidopsis:
#         current_list = line.split()
#         print ("Current orthogroup is %s" %current_list[0])
#         for i in range (len(current_list)): # all but the last element...  i = 0 to L-1
#             if i< len(current_list)-1:
#                 if (('Zea' in current_list[i]) and ('Zea' in current_list[i+1])):
#                     print ("Found multiple copies of ortholog genes for Zea")
#                     print ("\n")
#                     break
#                 elif (('Zea' in current_list[i]) and ('Zea' not in current_list[i+1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Zea found: Written SCO genes to file")
#                     print ("\n")
#                     arab_zea_single_orthologs.writelines(current_list)
#                     arab_zea_single_orthologs.write("\n")
#                     break                  
#             if i== len(current_list)-1: # last element
#                 if (('Zea' in current_list[i]) and ('Zea' in current_list[i-1])):
#                     print ("Found multiple copies of ortholog genes for Zea")
#                     print ("\n")
#                     break
#                 elif (('Zea' in current_list[i]) and ('Zea' not in current_list[i-1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Zea found: Written SCO genes to file")
#                     print ("\n")
#                     arab_zea_single_orthologs.writelines(current_list)
#                     arab_zea_single_orthologs.write("\n")
#                     break            
# arab_zea_single_orthologs.close()          
# count = 0
# with open('./arab_zea_single_orthologs.txt', 'r') as f:
#     for line in f:
#         count += 1
# print("Total number of lines is: %d" %count)
# # Total number of lines is: 4074


# ---- RICE and ARABIDOPSIS
# arab_ory_single_orthologs = open("./arab_ory_single_orthologs.txt", "w")
# with open("./single_orthologs_arabidopsis.txt", 'r') as arabidopsis:
#     for line in arabidopsis:
#         current_list = line.split()
#         print ("Current orthogroup is %s" %current_list[0])       
#         for i in range (len(current_list)): # all but the last element...  i = 0 to L-1
#             if i< len(current_list)-1:
#                 if (('Ory' in current_list[i]) and ('Ory' in current_list[i+1])):
#                     print ("Found multiple copies of ortholog genes for Rice")
#                     print ("\n")
#                     break
#                 elif (('Ory' in current_list[i]) and ('Ory' not in current_list[i+1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Rice found: Written SCO genes to file")
#                     print ("\n")
#                     arab_ory_single_orthologs.writelines(current_list)
#                     arab_ory_single_orthologs.write("\n")
#                     break                  
#             if i== len(current_list)-1: # last element
#                 if (('Ory' in current_list[i]) and ('Ory' in current_list[i-1])):
#                     print ("Found multiple copies of ortholog genes for Rice")
#                     print ("\n")
#                     break
#                 elif (('Ory' in current_list[i]) and ('Ory' not in current_list[i-1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Rice found: Written SCO genes to file")
#                     print ("\n")
#                     arab_ory_single_orthologs.writelines(current_list)
#                     arab_ory_single_orthologs.write("\n")
#                     break                    
# arab_ory_single_orthologs.close()        
# count = 0
# with open('./arab_ory_single_orthologs.txt', 'r') as f:
#     for line in f:
#         count += 1
# print("Total number of lines is: %d" %count)
# # Total number of lines is: 4946


# ---- Getting the common Single Copy Orthologs for Arabidopsis, ZeaMaize, Sol(Tomato), Orysa(Rice)
# From the files created in above steps, th following are the sizes of the files:
# Tomato, Arabidopsis: 5239
# Maize, Arabidopsis: 4074
# Rice, Arabidopsis: 4946
# Since Maize, Arabidopsis file is the samallest, I'll use that file (arab_zea_single_orthologs.txt) to extract the Common SCO genes.  

# # zea and arabidopsis done; sol and orysa remaining
# # arab_zea_single_orthologs = open('./arab_zea_single_orthologs.txt', 'r')
# # Doing rice (orysa) first

# ARAB_ZEA_ORY_single_orthologs = open("./ARAB_ZEA_ORY_single_orthologs.txt", "w")
# with open("./arab_zea_single_orthologs.txt", 'r') as file:
#     for line in file:
#         current_list = line.split()
#         print ("Current orthogroup is %s" %current_list[0])
        
#         for i in range (len(current_list)): # all but the last element...  i = 0 to L-1
#             if i< len(current_list)-1:
#                 if (('Ory' in current_list[i]) and ('Ory' in current_list[i+1])):
#                     print ("Found multiple copies of ortholog genes for Rice")
#                     print ("\n")
#                     break
#                 elif (('Ory' in current_list[i]) and ('Ory' not in current_list[i+1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Rice found: Written SCO genes to file")
#                     print ("\n")
#                     ARAB_ZEA_ORY_single_orthologs.writelines(current_list)
#                     ARAB_ZEA_ORY_single_orthologs.write("\n")
#                     break                  
#             if i== len(current_list)-1: # last element
#                 if (('Ory' in current_list[i]) and ('Ory' in current_list[i-1])):
#                     print ("Found multiple copies of ortholog genes for Rice")
#                     print ("\n")
#                     break
#                 elif (('Ory' in current_list[i]) and ('Ory' not in current_list[i-1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Rice found: Written SCO genes to file")
#                     print ("\n")
#                     ARAB_ZEA_ORY_single_orthologs.writelines(current_list)
#                     ARAB_ZEA_ORY_single_orthologs.write("\n")
#                     break            
# ARAB_ZEA_ORY_single_orthologs.close() 
# count = 0
# with open('./ARAB_ZEA_ORY_single_orthologs.txt', 'r') as f:
#     for line in f:
#         count += 1
# print("Total number of lines is: %d" %count)
# # Total number of lines is: 3454


# # ARAB_ZEA_ORY_single_orthologs.txt file contains SCO genes for Arab, Zea, Orysa. Now, only Sol (Tomato) remaining
# # Doing tomato (Sol) now

# ARAB_ZEA_ORY_SOL_single_orthologs = open("./ARAB_ZEA_ORY_SOL_single_orthologs.txt", "w")

# with open("./ARAB_ZEA_ORY_single_orthologs.txt", 'r') as file:
#     for line in file:
#         current_list = line.split()
#         print ("Current orthogroup is %s" %current_list[0])
        
#         for i in range (len(current_list)): # all but the last element...  i = 0 to L-1
#             if i< len(current_list)-1:
#                 if (('Sol' in current_list[i]) and ('Sol' in current_list[i+1])):
#                     print ("Found multiple copies of ortholog genes for Sol")
#                     print ("\n")
#                     break
#                 elif (('Sol' in current_list[i]) and ('Sol' not in current_list[i+1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Sol found: Written SCO genes to file")
#                     print ("\n")
#                     ARAB_ZEA_ORY_SOL_single_orthologs.writelines(current_list)
#                     ARAB_ZEA_ORY_SOL_single_orthologs.write("\n")
#                     break                  
#             if i== len(current_list)-1: # last element
#                 if (('Sol' in current_list[i]) and ('Sol' in current_list[i-1])):
#                     print ("Found multiple copies of ortholog genes for Sol")
#                     print ("\n")
#                     break
#                 elif (('Sol' in current_list[i]) and ('Sol' not in current_list[i-1])): 
#                     current_list= list(map(lambda x:x+' ', current_list))
#                     print ("Single gene for Sol found: Written SCO genes to file")
#                     print ("\n")
#                     ARAB_ZEA_ORY_SOL_single_orthologs.writelines(current_list)
#                     ARAB_ZEA_ORY_SOL_single_orthologs.write("\n")
#                     break                    
        
        
# ARAB_ZEA_ORY_SOL_single_orthologs.close() 
         
# count = 0
# with open('./ARAB_ZEA_ORY_SOL_single_orthologs.txt', 'r') as f:
#     for line in f:
#         count += 1
# print("Total number of lines is: %d" %count)
# ##Total number of lines is: 2898

