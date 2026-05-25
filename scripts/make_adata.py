import pandas as pd 
import numpy as np 
import scanpy as sc

adata = sc.read_10x_mtx(
    "../data/",
    var_names="gene_symbols",   # use gene names (not Ensembl IDs) as var index
    cache=True                  # caches a .h5ad for faster reloading
)

# read in columns from metadata excel 

metadata = pd.read_csv("../data/table_s1.csv")
metadata = metadata.dropna(subset=["GEO upload info"])

# merge metadata with adata.obs 
# first parse obs index to get sample id from the last numerical part of the index
adata.obs["sample_id"] = adata.obs.index.str.split("-").str[-1]
adata.obs["sample_id"] = adata.obs["sample_id"].astype(int)

# now parse the column GEO upload info by this rule to get the numerical sample id: 

sample_id_map = {
'1': 'nCoV 1 scRNA-seq',
'2': 'nCoV 2 scRNA-seq',
'3': 'Flu 1 scRNA-seq',
'4': 'Flu 2 scRNA-seq',
'5': 'Normal 1 scRNA-seq',
'6': 'Flu 3 scRNA-seq',
'7': 'Flu 4 scRNA-seq',
'8': 'Flu 5 scRNA-seq',
'9': 'nCoV 3 scRNA-seq',
'10': 'nCoV 4 scRNA-seq',
'11': 'nCoV 5 scRNA-seq',
'12': 'nCoV 6 scRNA-seq',
'13': 'Normal 2 scRNA-seq',
'14': 'Normal 3 scRNA-seq',
'15': 'nCoV 7 scRNA-seq',
'16': 'nCoV 8 scRNA-seq',
'17': 'nCoV 9 scRNA-seq',
'18': 'nCoV 10 scRNA-seq',
'19': 'Normal 4 scRNA-seq',
'20': 'nCoV 11 scRNA-seq'
}

def parse_sample_id(geo_info):
    for key, value in sample_id_map.items():
        if value in geo_info:
            return int(key)
    return None

metadata["sample_id"] = metadata["GEO upload info"].apply(parse_sample_id)
metadata["sample_id"] = metadata["sample_id"].astype(int)

# merge metadata with adata.obs on sample_id
adata.obs = adata.obs.merge(metadata, on="sample_id", how="left")

# clean up adata.obs
# drop Patient ID and GEO upload info columns
adata.obs = adata.obs.drop(columns=["GEO upload info", "Patient ID"])
# rename columns to concise names, no white spaces
adata.obs = adata.obs.rename(columns={
    "Disease group": "disease_state",
    "Age": "age",
    "sample_id": "sample_number",
    "Sample ID": "sample_id",
    "Sex": "sex",
    "Experimental\nbatch": "batch"
})
# remove anny '\n' characters from column values in disease_state 
adata.obs["disease_state"] = adata.obs["disease_state"].str.replace("\n", " ", regex=True)
# cast any column types that are objects to categorical
for col in adata.obs.columns:
    if adata.obs[col].dtype == "object":
        adata.obs[col] = adata.obs[col].astype("category")
adata.obs['batch'] = adata.obs['batch'].astype('category')

# subset to remove influenza patients, simplify for the workshop
adata = adata[adata.obs["disease_state"] != "severe influenza"]

# write to h5ad file for faster loading in the future
adata.write("../data/adata_raw.h5ad")

