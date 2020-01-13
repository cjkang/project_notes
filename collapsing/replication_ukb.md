# Gene / window based collapsing signal replication at UKB
- data : ukb imputed data
- test : burden / SKAT with SAIGE https://github.com/weizhouUMICH/SAIGE/wiki/Genetic-association-tests-using-SAIGE

# Run SAIGE
- step 0: creating a sparse GRM
  - input : plink file
 
- step 1: fitting the null model
  - input : bed file with rare variants
    - thinning UKB array data without maf threshold?
  
- step 2: association test
  - input : bgen file, phenotype data, group file
    - group file?
