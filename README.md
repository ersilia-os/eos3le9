# HepG2 Toxicity (MMV Data)

This model predicts the toxicity of small molecules in HepG2 cells. It has been developed by Ersilia thanks to data provided by Medicines for Malaria Venture (MMV). The dataset comprises IC50 data for 1335 molecules upon 72h incubation period. We have used two cut-offs to define activity (5 and 10 uM respectively). The models have been trained with LazyQSAR and achieve a performance of AUROC 0.85 and 0.75 upon 3-fold crossvalidation. 

This model was incorporated on 2023-08-24.Last packaged on 2025-07-23.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3le9`
- **Slug:** `hepg2-mmv`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Toxicity`, `Human`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of toxicity in HepG2 cells. Cut-offs: 5 and 10 uM

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ic50_hepg2_72h_5um | float | high | Classification score for HepG2 cytotoxicity based on an IC50 cut-off of 5uM |
| ic50_hepg2_72h_10um | float | high | Classification score for HepG2 cytotoxicity based on an IC50 cut-off of 10uM |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3le9](https://hub.docker.com/r/ersiliaos/eos3le9)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3le9.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3le9.zip)

### Resource Consumption
- **Model Size (Mb):** `11`
- **Environment Size (Mb):** `7610`
- **Image Size (Mb):** `6378.03`

**Computational Performance (seconds):**
- 10 inputs: `41.18`
- 100 inputs: `51.79`
- 10000 inputs: `553.72`

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
