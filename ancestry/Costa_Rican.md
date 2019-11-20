#Local Ancestry for Costa Rican
- 

# Reference populations for RFMix
- Costa Rican is an admixed population from African, (Southern?) European and native American.
- From HapMap3
  - AMR : CLM (Colombian : 94), MXL (Mexican ancestry in LA : 85), PEL (Peruvian : 85), Pur (Puerto Rican : 104)
  - AFR : ACB (African Carribbean in Barbados : 96), ASW (African Ancestry Southwest US :  61), ESN (Esan in Nigeria : 99), GWD (Gambian : 113), LWK (Luhya in Kenya : 99), MSL (Mende : 85), YRI (Yoruba in Nigeria : 108)
  - EUR : IBS (Iberian in Spain : 107), TSI (Toscani : 107) <- Southern EUR only
  
  - Other paper : 
    - Admixture Mapping Identifies an Amerindian Ancestry Locus Associated with Albuminuria in Hispanics in the United States
      - European/West African/Amerindian ancestry
    - Local Ancestry Inference in a Large US-Based Hispanic/Latino Study: Hispanic Community Health Study/Study of Latinos
      - European/West African/Amerindian ancestry
    - Reconstructing Native American Population History
    -Latin Americans show wide-spread Converso ancestry and imprint of local Native ancestry on physical appearance
      - YRI, IBS and native american?
- Run ADMIXTURE or STRUCTURE on AMR/CEU/YRI then pick samples on the distint cluster.
  - create PLINK file with AMR,YRI,CEU,IBS (+ EAS as an outgroup?)
    - 1000G phase3 - 
  - Run ADMIXTURE
    - try k=3 or 4?
