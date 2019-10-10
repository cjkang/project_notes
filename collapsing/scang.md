- Paper : https://www.sciencedirect.com/science/article/pii/S0002929719300989?via%3Dihub
- Source : https://github.com/zilinli1988/SCANG
  - R package

- Input 
  - (n,m) genotype matrix (n samples, m sites)
    - Single input for whole genome (not per chr analysis)
    - dosage
  - Phenotype 
  - Covariates
  
- Output
  - $SCANG_O_res : A matrix that summarized the significant region detected by SCANG-O
    - -log(pval) of the region, start, end, family-wise/genome-wide error rate of the detected region
  - $SCANG_O_thres : Empirical threshold of SCANG-O for controlling the family-wise type I error at alpha level.

- Run
  - Run `fit_null_glm` or `fit_null_glmkin`
    - Ex) `obj_null <- fit_null_glmkin(CVD~PC1, data=pheno, id = "IND_ID", family = binomial(link="logit"))`
    
  - Run `SCANG`
    - genotype data
    - min/max number of variants in search window
    - MAF cutoff
    - And other options - alpha, filter, f, steplength
    - Ex) `scang_out <- SCANG(genotype, obj_null, lmin = 50, lmax = 500, rare_maf_cutoff=0.05)`
    

- Run on MGI cluster
```
bsub -Is -q docker-interactive -M 5000000 -R 'rusage[mem=5000,gtmp=1] select[gtmp>1]' -a 'docker(halllab/r-351:v2)' /bin/bash -l
WORKSPACE=/gscmnt/gc2802/halllab/ckang/CCDG/temp/
export R_LIBS=${WORKSPACE}/r-libs
export PATH=/gscuser/ckang/.pyenv/shims:/gscuser/ckang/.pyenv/bin:/opt/lsf9/9.1/linux2.6-glibc2.3-x86_64/etc:/opt/lsf9/9.1/linux2.6-glibc2.3-x86_64/bin:/usr/local/bin:/usr/bin:/bin
/
unset LD_LIBRARY_PATH
/opt/hall-lab/R-3.5.1/bin/R
library(SCANG)
```
