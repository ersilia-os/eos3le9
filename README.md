# HepG2 Toxicity (MMV Data)

Predicts cytotoxicity in HepG2 liver carcinoma cells, the standard counter- screen for separating genuine antiparasitic activity from general cell killing. Ersilia trained two LazyQSAR classifiers on 72-hour IC50 data for 1,335 compounds from Medicines for Malaria Venture, calling toxicity below 5 uM (104 toxic) or 10 uM (746 toxic), with AUROC 0.88 and 0.79 in five-fold out-of-fold validation. Outputs are ranks against 50,000 drug-like molecules. A single cell line does not anticipate organ-level or metabolism-dependent toxicity.

This model was incorporated on 2023-08-24.
Last packaged on 2026-11-23.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3le9`
- **Slug:** `hepg2-mmv`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Toxicity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Rank of predicted HepG2 cytotoxicity at IC50 cut-offs of 5 and 10 uM, against 50,000 drug-like molecules; 0.65 is more toxic than 99% of them.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ic50_hepg2_72h_5um_rank | float | high | Rank score of the compound's predicted HepG2 cytotoxicity at an IC50 cut-off of 5 uM (72 h), calibrated against a reference library of 50K drug-like molecules so that 0.65 is more toxic than 99% of them. Recommended threshold: 0.65. |
| ic50_hepg2_72h_10um_rank | float | high | Rank score of the compound's predicted HepG2 cytotoxicity at an IC50 cut-off of 10 uM (72 h), calibrated against a reference library of 50K drug-like molecules so that 0.65 is more toxic than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3le9](https://hub.docker.com/r/ersiliaos/eos3le9)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3le9.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3le9.zip)
- **Apptainer**: [https://models-sif.s3.eu-north-1.amazonaws.com/eos3le9_v1.sif](https://models-sif.s3.eu-north-1.amazonaws.com/eos3le9_v1.sif)

### Resource Consumption
- **Model Size (Mb):** `23`
- **Environment Size (Mb):** `6954`
- **Image Size (Mb):** `3284.6`

**Computational Performance (seconds):**
- 10 inputs: `37.45`
- 100 inputs: `33.17`
- 10000 inputs: `333.27`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://ersilia.io](https://ersilia.io)
- **Publication Type:** `Other`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3le9
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3le9
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
