## Prep data for collapsing test
- SKAT test with hail
  - one gene/region per marker
  - No overlapping gene/region
  
- Region based test
  - 4kb windows, 2kb step size
  - prep a matrix table with 2 annotations - region1 / region2
    - biallelic only
  - region1 starting at 0, region2 starting at 2000
  - apply SKAT separately then merge the results
    - Need to apply variant/sample filters later
      - MAF, PASS etc.
  - Try SKAT-O
    - Prep data
      - plink bed
    - Run SKAT script
    
- Gene based test
  - filter `HIGH` and `MODERATE` at VEP's `IMPACT` field
  - HGNC genes only
  - create EPACTS grp files by impacts and CADD score
    - high, high+mod (CADD > 20, 13.2 or all)
