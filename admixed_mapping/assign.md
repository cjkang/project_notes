# Assign (or infer) ancestry for non overlapping markers
- Based on the segments between two overlapping markers
- Case 1: two haplotype segments on the same ancestry
  - Just assign that ancestry (easy!)
- Case 2: two different ancestry
  - Figure out phasing info of the overlapping markers and non overlapping ones
  - Assign ancestry based on nearest overlapping one on the same haplotype
- Case 3: "mosaic" ancestry on one of the haplotype segment
  - Figure out phasing info of the overlapping markers and non overlapping ones
  - Assign ancestry based on the distance?
- Case 4: "mosaic" ancestry on both haplotype segments
- Case 5: ancestry phasing and variant phasing not matching (due to RFMix rephasing or separate phasing)
- Case 6: two different ancesty or mosaic but non polymorphic at overlapping markers
  - check wider segments
  
- For case 2-6, assign the nearest overlapping HET's ancestry  

# Prep ancestry info
- From RFMix output (Viterbi and allelesRephased0), create a single bed file
- Row : segment
- Col : hap? or sample?
- Needs allele info and ancestry info

# Infer ancestry
- From phased VCF
- Move segment by segment


### USE RFMIX TRIOPHASE
- There will be no "correct phase" on triophase
- from the phased vcf (chunk), run rfmix separately


# in detail process
1) copy phased files `/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/phase/out/*vcf.gz` to google cloud `gs://wustl-gatk4-call-set-20190614-analysis/users/cjkang/ancestry/phased_vcf/`
2) filter overlapping sites (vcf + ref tsv) `gs://wustl-gatk4-call-set-20190614-analysis/users/cjkang/ancestry/phased_vcf/*filtered*
3) copy to MGI cluster `/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/ancestry_gwas/phased`
4) create rfmix infiles with `/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/ancestry_gwas/rfmix/makeinfiles.py [chrom]`
5) Run rfmix with `/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/ancestry_gwas/rfmix/run.py [chrom]`
6) Make a single ancestry file `/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/ancestry_gwas/rfmix/sum.py [segment]`
