# RNA-Tissue-Classification

Classification of RNA-Seq data (having a set of single copy ortholog genes) of a plant sample into different tissue types

RNA-Seq is a popular method that makes use of Next Generation Sequencing (NGS) to reveal qualitative and quantitative information about the transcriptome. Parsing RNA-Seq data is dependent on correct annotation of samples/experiments. Most methods of sample annotation are still manual/forensic. With the ever-growing numbers of RNA-Seq data, it is required to develop computational methods to annotate tissue types from RNA-Seq profile.

This project aims at developing a model that can correctly annotate transcriptome data (RNA-Seq) into tissues (where the experiment sample was prepared from; Eg: leaf, root, seed etc). Our ultimate goal is to develop a universal model that can classify the tissue of a (non-Arabidopsis). We, however, intend to train the model using only Arabidopsis data.

A central assumption in this project is that most ortholog genes common across the plant species perform similar functions, and hence have similar expression profiles. Orthologs are genes in different species that have evolved through speciation events only. Thus, training the tissue classifier model using only ortholog gene expression data from Arabidopsis, it is plausible to predict tissue in other plant species as well.
