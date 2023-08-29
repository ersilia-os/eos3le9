# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar)
Upon 5-fold crossvalidation on train test splits (80-20%) with balanced classes, we obtain the following performance:


| **Model**       | **Data** | **Frac Actives (%)** | **Fingerprints** | **AUROC ± STDev** |
|-----------------|----------|------------------|------------------|-------------------|
| ic50_hepg2_72h_5uM         | 1335   | 7.79   | Eosce   | 0.821 ± 0.067 |
| ic50_hepg2_72h_5uM         | 1335   | 7.79   | Morgan   | 0.767 ± 0.083 |
| ic50_hepg2_72h_10uM         | 1335   | 55.88   | Eosce   | 0.737 ± 0.034 |
| ic50_hepg2_72h_10uM         | 1335   | 55.88   | Morgan   | 0.762 ± 0.027 |

Upon request we are happy to provide full models developed with [ZairaChem](https://github.com/ersilia-os/zaira-chem) as a downloadable. Please note that running these require installation of the Ersilia and the ZairaChem software

| **Model**       | **Data** | **Frac Actives (%)** | **AI tool** | **AUROC ± STDev** |
|-----------------|----------|------------------|------------------|-------------------|
| ic50_hepg2_72h_5uM         | 1335   | 7.79   | Zairachem   | 0.888 ± 0.027 |
| ic50_hepg2_72h_10uM         | 1335   | 55.88   | Zairachem   | 0.794 ± 0.011 |