<img src="https://oasislmf.org/packages/oasis_theme_package/themes/oasis_theme/assets/src/oasis-lmf-colour.png" alt="Oasis LMF logo" width="250"/>

# Future Indonesian Tsunamis: Towards End-to-end Risk quantification (FITTER)

## Model Key Facts

FITTER was funded by Lloyd's Tercentenary Research Foundation and Lighthill Risk Network funded research project executed by University College London (UCL).

### Region and Peril

Indonesia Tsunami

### Publisher

**Name**: University College London / Alan Turing Institute

**Email**: s.guillas@ucl.ac.uk

**URL**: https://www.ucl.ac.uk/risk-disaster-reduction/research-projects/2024/jan/future-indonesian-tsunamis-towards-end-end-quantification-risk-fitter

### Contact

**Name**: Serge Guillas, UCL

**Email**: s.guillas@ucl.ac.uk

### Version and Licence

**Version**: 1

**License**: CC-BY-NC-SA-4.0

## Hazard module

**Title**: FITTER hazard data - tsunami intensity damage index

Tsunami hazard footprint files (qualitative intensity) developed through statistical emulation for Java and Sumatra, Indonesia in Oasis format

### Event set information

| Event Set | Type | Calculation Method | Countries | Number of events |
|---|---|---|---|---|
| Java_1 | probabilistic | simulated | ['IDN'] | 1278 |
| Sumatra_1 | probabilistic | simulated | ['IDN'] | 730 |
### Hazard information

| Event Set | Hazard Process | Intensity measure | Trigger Event | Trigger Process |
|---|---|---|---|---|
| QTS | ['tsunami'] | DI:- | earthquake | ['ground_motion'] |
| QTS | ['tsunami'] | DI:- | earthquake | ['ground_motion'] |
## Vulnerability module

**Title**: FITTER household and business vulnerability data

Social vulnerability curves in Oasis format, relating qualitative levels of tsunami damage to percentage reduction in household and business asset value.

### Hazard information

| Hazard type | Hazard process | Intensity |
|---|---|---|
| tsunami | tsunami | DI:- |
### Vulnerability functions

**Exposure category**: population

**Countries**: ['IDN']

**Impact type**: indirect

**Impact metric**: economic_loss_value - household asset and business asset values

**Impact unit**: percentage

**Base data type**: observed

**Approach**: empirical

### Further details

The curves to estimate impact on household business assets and business recovery are developed using longitudinal household survey data (two waves of the STAR longitudinal survey carried out in Banda Aceh, Sumatra, 5–14 and 17–29 months after the 2004 Indian Ocean tsunami. See https://www.sciencedirect.com/science/article/pii/S2212420922000875

This document has been generated using Risk Data Library Standard schema version 0.2.

For more information about the RDLS please visit [RDLS](https://docs.riskdatalibrary.org/en/latest/)

