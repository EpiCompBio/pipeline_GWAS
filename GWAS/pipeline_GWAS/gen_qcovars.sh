
# Steps to generate some covariate files for fastGWA analysis:

# Get some continuous numbers with the same IID and FID as the pheno file:
cp test.phen test.qcovar

# Get the IID and FID for the discrete covariates files:
cp test.phen test.cat_covar

# Change otherwise will give null results in regression, reverse sort:
cut -d' ' -f3 test.qcovar | sort -rn - > qcovar1.txt

# Random sort:
cut -d' ' -f3 test.qcovar | sort -R - > qcovar2.txt

# Generate new file with space as delimiter:
paste -d' ' qcovar1.txt qcovar2.txt > qcovars.txt

# Put into required format for gcta:
paste -d' ' test.qcovar qcovars.txt > test.qcovar2
cut -d' ' -f1,2,4,5 test.qcovar2 > test.qcovar

# Get rid of intermediate files:
rm -f qcovar1.txt qcovar2.txt test.qcovar2 qcovars.txt 


# Generate categorical/discrete covariates file:
shuf -ri 0-1 -n 3925 > cat_covar1.txt
shuf -re F M -n 3925 > cat_covar2.txt
paste -d' ' test.cat_covar cat_covar1.txt cat_covar2.txt > test.cat_covar2
cut -d' ' -f1,2,4,5 test.cat_covar2 > test.cat_covar
rm -f cat_covar* test.cat_covar2
