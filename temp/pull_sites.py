import hail as hl
hl.init("default_reference=GRCh38")

# pull EOCAD sites


# pull Fin sites
for x in chroms:
  mt = hl.read_matrix_table("wustl-gatk4-final-call-set-20190319/merged_mt"+x)
  # filter snp
  mt = mt.filter_rows(hl.is_snp(mt.alleles))
  # filter first sample
  mt = mt.filter_cols(hl.s=)
  #export to vcf
  hl.export_vcf(mt,"")
  
