# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar)
Upon 3-fold crossvalidation on train test splits with balanced classes, we obtain the following performance:


| **Model**       | **Data** | **Frac Actives (%)** | **AUROC ± STDev** |
|-----------------|----------|------------------|-------------------|
| ic50_hepg2_72h_5uM         | 1335   | 7.79   |  0.85 ± 0.02 |
| ic50_hepg2_72h_10uM         | 1335   | 55.88   |  0.75 ± 0.02 |