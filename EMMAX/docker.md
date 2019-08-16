## Run EMMAX with DOCKER
- For EOCAD 2019 callset, create LD pruned VCF (~585K)
- Run EPACTS to create kinship matrix file

## INPUT VCF
- `/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/emmax/pruned.vcf.bgz`
- Should `chr` prefix be removed?


## EPACTS + docker
- Try Dave's old docker image
  ```
  LSF_DOCKER_PRESERVE_ENVIRONMENT=false bsub -Is -q ccdg -a 'docker(ernfrid/epacts:v1)' /bin/bash
  /opt/ccdg/epacts/bin/epacts make-kin -vcf pruned.vcf.bgz -out test -run 1
  FATAL ERROR -
  Failed to load the index file

  terminate called after throwing an instance of 'pException'
    what():  Exception was thrown
  make: *** [test.1.1.10000000.kin] Aborted (core dumped)
  /opt/ccdg/epacts/bin/pEmmax gen-kin --vcf pruned.vcf.bgz  --region 1:1-10000000 --field GT --minMAF 0.01 --minCallRate 0.95 --out-kinf test.1.1.10000000.kin --raw --ignoreFilter
   test.Makefile:9: recipe for target 'test.1.1.10000000.kin' failed
   ```
