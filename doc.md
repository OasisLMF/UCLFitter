# Model Information

**Name**: Future Indonesian Tsunamis: Towards End-to-end Risk quantification (FITTER)

**Description**: FITTER was funded by Lloyd's Tercentenary Research Foundation and Lighthill Risk Network funded research project executed by University College London (UCL).

**License**: CC-BY-NC-SA-4.0

**Contact**: Serge Guillas, UCL s.guillas@ucl.ac.uk  

## Hazard module 

**ID**: fitter_haz

**Title**: FITTER hazard data - tsunami intensity damage index

**Description**: Tsunami hazard footprint files (qualitative intensity) developed through statistical emulation for Java and Sumatra, Indonesia in Oasis format

### Event set information 

| Event Set | Type        | Calculation Method | Countries  | Number of events |
|-----------|-------------|--------------------|------------|------------------|
| fitter_haz_Jav | probabilistic | simulated | ['IDN'] | 1278 |
| fitter_haz_Sum | probabilistic | simulated | ['IDN'] | 730 |

### Hazard information 

| Event Set | Process types | Intensity measure | Trigger type  | Trigger process types |
|-----------|---------------|-------------------|---------------|-----------------------|
| fitter_haz_Jav | ['tsunami'] | DI:- | earthquake | ['ground_motion'] |
| fitter_haz_Sum | ['tsunami'] | DI:- | earthquake | ['ground_motion'] |

## Vulnerability module 

**ID**: fitter_vln

**Title**: FITTER household and business vulnerability data

**Description**: Social vulnerability curves in Oasis format, relating qualitative levels of tsunami damage to percentage reduction in household and business asset value.

### Hazard information 

| Hazard type | Hazard process | Intensity |
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


This document has been generated using Risk Data Library Standard schema version 0.2. For more information about the RDLS please visit [RDLS](https://docs.riskdatalibrary.org/en/latest/)