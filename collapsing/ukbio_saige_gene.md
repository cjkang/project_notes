# Replication at UKB with saige gene
## SAIGE gene (https://github.com/weizhouUMICH/SAIGE/wiki/Genetic-association-tests-using-SAIGE)
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
  - Use step 0 GRM output
  - For gene based test, plink file with rare variants needed. 
  - More variants than number of samples are needed (>200K) (https://github.com/weizhouUMICH/SAIGE/issues/92)
  - At least 100 variants per MAC are needed.
  - Test with chr1 genotype data - killed (memory error?)
  - Test with chr22
   ```
   step1_fitNULLGLMM.R     \
        --plinkFile=./ukb.array_all_sites.chr.1 \
        --phenoFile=/gscmnt/gc2802/halllab/ckang/CCDG/UKBIOBANK/gwas/ukb.white_only.norel.cvd01.ped \
        --phenoCol=CVD \
        --covarColList=SEX,PC1 \
        --sampleIDColinphenoFile=IND_ID \
        --traitType=binary        \
        --outputPrefix=./step1/ukb.chr1.cvd \
	--outputPrefix_varRatio=./step1/ukb.chr1.varratio	\
	--sparseGRMFile=./step0/merged.common.ped_samples_only.step0_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx    \
        --sparseGRMSampleIDFile=./step0/merged.common.ped_samples_only.step0_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt  \
        --nThreads=4 \
        --LOCO=FALSE \
	--skipModelFitting=FALSE \
        --IsSparseKin=TRUE      \
        --isCateVarianceRatio=TRUE
        ```

- 
