## Local ancestry with RFMIX2
- Test with a single sample, 1k variants case *, 2 sites ref
```
bsub -Is -q ccdg -a 'docker(halllab/rfmix203r0:v2)' -M 64000000 /bin/bash
unset LD_LIBRARY_PATH
/opt/hall-lab/rfmix-2.03r0/bin/rfmix -f small.vcf -r ref.3.vcf -m sample.map -g genetic_map_hg38_withX.rfmix.chr.txt -o test --chromosome=chr21 --crf-weight=1
```
  - working

- Test with whole ref 21
```
Loading genetic map for chromosome chr21 ...  done
Mapping samples ... 208 samples combined
Scanning input VCFs for common SNPs on chromosome chr21 ...   999 SNPs
Loading haplotypes...
Warning: ref.21.vcf - 999 unphased genotypes treated as phased
done
Defining and initializing conditional random field...
   setting up CRF points and random forest windows...
   computing random forest window spacing overlay...
   initializing apriori reference subpop across CRF...
   setting up random forest probability estimation arrays... done
Defining and initializing conditional random field...   done
33168 (8.0%) variant alleles	1998 (0.5%) missing alleles


Killed
```
