## Prep data for collapsing test
- SKAT test with hail
  - one gene/region per marker
  - No overlapping gene/region
  
- Region based test
  - prep two hail matrix tables 
  - Per one matrix table, there's no overlap but overlap with the other table
  - 4kb window
  - one table starting at 0, the other one starting at 2000
  
- Gene based test
  - filter `HIGH` and `MODERATE` at VEP's `IMPACT` field
  - HGNC genes only
  - create EPACTS grp files by impacts and CADD score
    - high, high+mod (CADD > 20, 13.2 or all)
