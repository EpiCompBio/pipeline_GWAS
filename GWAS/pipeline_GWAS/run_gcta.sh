#!/usr/bin/env bash


##########################
# Example from:
# https://cnsgenomics.com/software/gcta/#fastGWA
##########################


##########################
# Set bash script options

# exit when a command fails
set -o errexit

# exit if any pipe commands fail
set -o pipefail

# exit when your script tries to use undeclared variables
set -o nounset

# trace what gets executed
set -o xtrace

set -o errtrace
###########################


###########################
# Variables to substitute:
GCTA_COMMAND=gcta_1.93.0beta
INFILE=geno_chrs.txt
THREADS=10
GRM_FILE=geno_grm
SPARSE_GRM=sp_grm
SPARSENESS=0.05
SPARSE_CUT=0.05
PHENO_FILE=test.phen
QUANT_COVAR_FILE=test.qcovar
COVAR_FILE=test.cat_covar
OUTFILE=geno_assoc
###########################


###########################
# Run commands:
# Generate a sparse GRM from SNP data
# geno_chrs.txt is a text file containing file paths to the SNP data of each chromosome
${GCTA_COMMAND} --mbfile ${INFILE} --make-grm --thread-num ${THREADS} --out ${GRM_FILE}
${GCTA_COMMAND} --grm ${GRM_FILE} --make-bK-sparse ${SPARSENESS} --out ${SPARSE_GRM}

# The two steps above can be merge into one if you don't have enough disk space to store the full dense GRM
#${GCTA_COMMAND} --mbfile ${INFILE} --make-grm --sparse-cutoff ${SPARSE_CUT} --threads ${THREADS} --out ${SPARSE_GRM}

# fastGWA mixed model (based on the sparse GRM generated above)
${GCTA_COMMAND} --mbfile ${INFILE} --grm-sparse ${SPARSE_GRM} --fastGWA-mlm --pheno ${PHENO_FILE} --qcovar ${QUANT_COVAR_FILE} --covar ${COVAR_FILE} --threads ${THREADS} --out ${OUTFILE}

# fastGWA linear regression
${GCTA_COMMAND} --mbfile ${INFILE} --fastGWA-lr --pheno ${PHENO_FILE} --qcovar ${QUANT_COVAR_FILE} --covar ${COVAR_FILE} --threads ${THREADS} --out ${OUTFILE}

echo 'Done executing fastGWA pipeline'
###########################


