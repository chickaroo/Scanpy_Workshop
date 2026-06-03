# Scanpy Workshop

CompBioSoc 2026 ScanPy scnRNA-Seq Data Analysis Workshop Contents

Part 1: Thursday 28 May 6-8pm, Huxley 311
Part 2: Thursday 4 May 6-8pm, Huxley 311

## Part 1 — Introduction to Scanpy
- [`Part1_ScanpyNotebook.ipynb`](Part1_ScanpyNotebook.ipynb)  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chickaroo/Scanpy_Workshop/blob/main/Part1_ScanpyNotebook.ipynb)
- **Note:** For more in-depth learning about dimensionality reduction which we covered in Part 1, have a look at Synthetic Biology Society's workshop on Tuesday 2 June from 6pm. 


## Part 2 - Clustering, Cell Types, and Downstream Analysis
- **Stand alone!** No need to have come to Part 1 or worked through the complete Part 1 notebook (this is recommended). 
- [`Part2_ScanpyNotebook.ipynb`](Part2_ScanpyNotebook.ipynb)  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chickaroo/Scanpy_Workshop/blob/main/Part2_ScanpyNotebook.ipynb)

## Data access: 
Download the `anndata` file from [here](https://drive.google.com/file/d/1HcbamRHxf7s7Qmcbpc-bfBfKnIorsE4j/view?usp=drive_link) and save it in the folder `data/` if running locally, or simply run the code cell to download the data automatically in the Colab notebook. 

Download the preprocessed `anndata` file from [here](https://drive.google.com/file/d/1p3hMKbg7S04Ufzpmc8v2WKDY5z3SduxR/view?usp=sharing) and save it in the same `data/` folder. 


## Environment set up to run locally: 

Use the `.yml` file for installation of the minimal requirement
```bash
conda env create -f scanpy_env.yml
conda activate scanpy_basic
```

Or simply run

```bash
conda create -n scanpy_basic -c conda-forge python=3.12 numpy pandas scanpy jupyter scikit-image
```

Note for Part 2 you'll need some aditional packages: `celltypist`, `pydeseq2`, `igraph`, `leidenalg`