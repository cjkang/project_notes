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
6) Make a single ancestry file as a bed format`/gscmnt/gc2802/halllab/ckang/CCDG/EOCAD_AA_2019/ancestry_gwas/rfmix/sum.py [segment]` 


# check ancestry
- AF check at AFR/AFR, at AFR haplotypes on AFR/EUR, at EUR haplotypes on AFR/EUR, at EUR/EUR
- Cross check with gnomad
