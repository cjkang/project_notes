# Replication at UKB with saige gene
# SAIGE gene (https://github.com/weizhouUMICH/SAIGE/wiki/Genetic-association-tests-using-SAIGE)
- PED

- STEP 0 : creating a sparse GRM
  - having troubles with ukb plink file
    - tried : single chr, single chr pruned, merged, merged pruned...
    - no problem with sample ped
    - might be related with the sample size not marker size
    - don't need rare variants
    - create a subset of merged/pruned plink only with filtered samples (200K)
      - working
 - STEP 1:
