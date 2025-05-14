## Table of Contents

- [Documentation](#documentation)
- [FITTER hazard data - tsunami intensity damage index](#fitter-hazard-data---tsunami-intensity-damage-index)
  - [Dataset Overview](#dataset-overview)
  - [Hazard metadata](#hazard-metadata)
    - [Spatial coverage](#spatial-coverage)
      - [loc_0](#loc_0)
        - [Gazetteer entries](#gazetteer-entries)
      - [loc_1](#loc_1)
        - [Gazetteer entries](#gazetteer-entries-1)
    - [Hazards](#hazards)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage)
    - [Spatial](#spatial)
    - [Gazetteer entries](#gazetteer-entries-2)
  - [Resources and Sources](#resources-and-sources)
    - [Resources](#resources)
      - [Intensity Bin Dictionary file for FITTER model](#intensity-bin-dictionary-file-for-fitter-model)
  - [Ownership and Contacts](#ownership-and-contacts)
    - [Publisher](#publisher)
    - [Creator](#creator)
    - [Contact point](#contact-point)
    - [Attributions](#attributions)
  - [Licensing and Links](#licensing-and-links)
    - [Links](#links)
    - [Referenced by](#referenced-by)
- [FITTER exposure data - for Sumatra and Java, and test acc and loc data](#fitter-exposure-data---for-sumatra-and-java-and-test-acc-and-loc-data)
  - [Dataset Overview](#dataset-overview-1)
  - [Exposure metadata](#exposure-metadata)
    - [Exposure metrics](#exposure-metrics)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage-1)
    - [Spatial](#spatial-1)
    - [Gazetteer entries](#gazetteer-entries-3)
  - [Resources and Sources](#resources-and-sources-1)
    - [Resources](#resources-1)
      - [Exposure Required Fields](#exposure-required-fields)
      - [Example account file](#example-account-file)
      - [Example location file](#example-location-file)
  - [Ownership and Contacts](#ownership-and-contacts-1)
    - [Publisher](#publisher-1)
    - [Creator](#creator-1)
    - [Contact point](#contact-point-1)
    - [Attributions](#attributions-1)
  - [Licensing and Links](#licensing-and-links-1)
    - [Links](#links-1)
- [FITTER household and business vulnerability data](#fitter-household-and-business-vulnerability-data)
  - [Dataset Overview](#dataset-overview-2)
  - [Vulnerability metadata](#vulnerability-metadata)
    - [Hazard info](#hazard-info)
    - [Exposure info](#exposure-info)
    - [Vulnerability Impact info](#vulnerability-impact-info)
    - [Vulnerability Spatial info](#vulnerability-spatial-info)
    - [Vulnerability Functions info](#vulnerability-functions-info)
      - [Vulnerability function](#vulnerability-function)
    - [Vulnerability Extra info](#vulnerability-extra-info)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage-2)
    - [Spatial](#spatial-2)
  - [Resources and Sources](#resources-and-sources-2)
    - [Resources](#resources-2)
      - [Vulnerability function dictionary](#vulnerability-function-dictionary)
    - [Sources](#sources)
  - [Ownership and Contacts](#ownership-and-contacts-2)
    - [Publisher](#publisher-2)
    - [Creator](#creator-2)
    - [Contact point](#contact-point-2)
    - [Attributions](#attributions-2)
  - [Licensing and Links](#licensing-and-links-2)
    - [Links](#links-2)
    - [Referenced by](#referenced-by-1)
- [FITTER loss data](#fitter-loss-data)
  - [Dataset Overview](#dataset-overview-3)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage-3)
    - [Spatial](#spatial-3)
    - [Gazetteer entries](#gazetteer-entries-4)
  - [Resources and Sources](#resources-and-sources-3)
    - [Resources](#resources-3)
      - [Ground up AAL](#ground-up-aal)
      - [Ground up ELT](#ground-up-elt)
      - [Ground up Aggregate LEC](#ground-up-aggregate-lec)
      - [Ground up Occurrence LEC](#ground-up-occurrence-lec)
      - [Ground up Summary Info](#ground-up-summary-info)
      - [Analysis settings for modelled losses](#analysis-settings-for-modelled-losses)
  - [Ownership and Contacts](#ownership-and-contacts-3)
    - [Publisher](#publisher-3)
    - [Creator](#creator-3)
    - [Contact point](#contact-point-3)
    - [Attributions](#attributions-3)
  - [Licensing and Links](#licensing-and-links-3)
    - [Links](#links-3)
    - [Referenced by](#referenced-by-2)

# Documentation
# FITTER hazard data - tsunami intensity damage index
## Dataset Overview
**Dataset identifier**: fitter_haz

**Title**: FITTER hazard data - tsunami intensity damage index

**Description**: Tsunami hazard footprint files (qualitative intensity) developed through statistical emulation for Java and Sumatra, Indonesia in Oasis format

**Risk data type**: hazard

**Dataset version**: 1

**Dataset purpose**: Create a national scale tsunami model in Oasis format

**Project title**: Future Indonesian Tsunamis: Towards End-to-end Risk quantification (FITTER)

**Additional details**: FITTER was funded by Lloyd's Tercentenary Research Foundation and Lighthill Risk Network funded research project executed by University College London (UCL).

## Hazard metadata
| Event set identifier | Hazards | Analysis type | Frequency distribution | Seasonality distribution | Calculation Method | Event count | Occurrence range | Spatial coverage | Temporal coverage | Events |
|---|---|---|---|---|---|---|---|---|---|---|
| Java_1 | QTS | probabilistic | user_defined | uniform | simulated | 1278 | 1 to 15324 years | loc_0 | Duration: P15324Y |  |
| Sumatra_1 | QTS | probabilistic | user_defined | uniform | simulated | 730 | 1 to 15043 years | loc_1 | Duration: P15043Y |  |

### Spatial coverage
#### loc_0
**Countries**: IDN

**Bounding box**: [105.62173, 114.43404, -8.54748, -5.88703]

##### Gazetteer entries
| Gazetteer entry identifier | Scheme | Description | Uniform resource locator |
|---|---|---|---|
| fitter_haz_Java_sp | ISO 3166-2 | ID |  |

#### loc_1
**Countries**: IDN

**Bounding box**: [95.128774, 105.370721, -5.592648, 5.891494]

##### Gazetteer entries
| Gazetteer entry identifier | Scheme | Description | Uniform resource locator |
|---|---|---|---|
| fitter_haz_Sumatra_sp | ISO 3166-2 | ID |  |

### Hazards
| Hazard identifier | Hazard type | Hazard processes | Intensity measure | Trigger |
|---|---|---|---|---|
| QTS | tsunami | tsunami | d_tsi:m | Hazard type: earthquake,<br>Hazard processes: ['ground_motion'] |

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: IDN

### Gazetteer entries
| Gazetteer entry identifier | Scheme | Description | Uniform resource locator |
|---|---|---|---|
| fitter_haz_Sum | GEONAMES | Sumatra, Indonesia | https://www.geonames.org/1626198/sumatra.html |
| fitter_haz_Java | GEONAMES | Java, Indonesia | https://www.geonames.org/1642673/java.html |

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| haz_intensity_bin_dict | Intensity Bin Dictionary file for FITTER model | Hazard intensity measure ranges used in model | text/csv | csv |  |  |  | resources/haz/intensity_bin_dict.csv |  |  |

#### Intensity Bin Dictionary file for FITTER model
File (intensity_bin_dict.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/haz/intensity_bin_dict.csv)

First 10 rows displayed only

| bin_index | bin_from | bin_to | interpolation | interval_type |
|---|---|---|---|---|
| 1 | 0.05 | 0.5 | 0.1 | 1202 |
| 2 | 0.5 | 1.5 | 1 | 1202 |
| 3 | 1.5 | 40 | 5 | 1202 |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| University College London / Alan Turing Institute | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/risk-disaster-reduction/research-projects/2024/jan/future-indonesian-tsunamis-towards-end-end-quantification-risk-fitter |

### Creator
| Name | Email address | URL |
|---|---|---|
| Dimitra Salmanidou | d.salmanidou.12@ucl.ac.uk | https://www.researchgate.net/profile/Dimitra-Salmanidou |

### Contact point
| Name | Email address | URL |
|---|---|---|
| Serge Guillas, UCL | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/statistics/people/sergeguillas |

### Attributions
| Attribution identifier | Entity | Role |
|---|---|---|
| fitter_haz_distr | Oasis LMF,<br>https://www.oasislmf.org | distributor |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json

### Referenced by
| Related resource identifier | Name | Author names | Publication date | URL | Digital object identifier |
|---|---|---|---|---|---|
| fitter_haz_CG23 | Multi-level emulation of tsunami simulations over Cilacap, South Java, Indonesia | "Ehara A.,<br> Salmanidou D.M.,<br> Heidarzadeh M.,<br> Guillas S." | 2022-12-21 | https://link.springer.com/article/10.1007/s10596-022-10183-1 | 10.1007/s10596-022-10183-1 |



# FITTER exposure data - for Sumatra and Java, and test acc and loc data
## Dataset Overview
**Dataset identifier**: fitter_exp

**Title**: FITTER exposure data - for Sumatra and Java, and test acc and loc data

**Description**: Household and business asset values for Java and Sumatra, for the UCL FITTER tsunami modelling project. Additional test data included. 

**Risk data type**: exposure

**Dataset version**: 1

**Dataset purpose**: Demonstrate the use of the FITTER model, with test portfolio containing blanket building TIV

**Project title**: Future Indonesian Tsunamis: Towards End-to-end Risk quantification (FITTER)

**Additional details**: FITTER was funded by Lloyd's Tercentenary Research Foundation and Lighthill Risk Network funded research project executed by University College London (UCL).

## Exposure metadata
**Exposure category**: buildings

**Exposure taxonomy scheme**: OED

### Exposure metrics
| Identifier | Metric dimension | Metric quantity kind |
|---|---|---|
| 1 | structure | currency |
| 3 | content | currency |

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: IDN

### Gazetteer entries
| Gazetteer entry identifier | Scheme | Description | Uniform resource locator |
|---|---|---|---|
| fitter_exp_Sum | GEONAMES | Sumatra, Indonesia | https://www.geonames.org/1626198/sumatra.html |
| fitter_exp_Java | GEONAMES | Java, Indonesia | https://www.geonames.org/1642673/java.html |

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| ExposureRequiredFields | Exposure Required Fields | Describes the exposure format and fields required for modelling. | text/csv | csv |  |  |  | resources/exp/ExposureRequiredFields.csv |  |  |
| account | Example account file | A sample exposure account file which can be run through the model. | text/csv | csv |  |  |  | resources/exp/account.csv |  |  |
| location | Example location file | A sample exposure location file which can be run through the model. | text/csv | csv |  |  |  | resources/exp/location.csv |  |  |

#### Exposure Required Fields
File (ExposureRequiredFields.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/exp/ExposureRequiredFields.csv)

First 10 rows displayed only

| Field | Scheme | File | Description | Valid values |
|---|---|---|---|---|
| LocPerilsCovered | OED | location | The perils to which the location is at risk. | "QTS", or group peril codes "QQ1" and "AA1" |
| CountryCode | OED | location | The OED country code for the location | "IN" |
| Latitude | OED | location | The latitude of the location (decimal) | Floating point number |
| Longitude | OED | location | The longitude of the location (decimal) | Floating point number |

#### Example account file
File (account.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/exp/account.csv)

First 10 rows displayed only

| PortNumber | AccNumber | AccCurrency | PolNumber | PolPerilsCovered |
|---|---|---|---|---|
| 1 | 1 | IDR | 1 | QTS |

#### Example location file
File (location.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/exp/location.csv)

First 10 rows displayed only

| LocNumber | AccNumber | PortNumber | BuildingTIV | ContentsTIV | BITIV | Latitude | Longitude | CountryCode | LocPerilsCovered | LocCurrency | LocName |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 100000 | 50000 | 0 | -8.0042 | 114.42801 | ID | QTS | IDR | AP0000001 |
| 2 | 1 | 1 | 100000 | 50000 | 0 | -8.0043 | 114.42783 | ID | QTS | IDR | AP0000002 |
| 3 | 1 | 1 | 100000 | 50000 | 0 | -8.00478 | 114.42797 | ID | QTS | IDR | AP0000003 |
| 4 | 1 | 1 | 100000 | 50000 | 0 | -8.00509 | 114.42803 | ID | QTS | IDR | AP0000004 |
| 5 | 1 | 1 | 100000 | 50000 | 0 | -8.03478 | 114.43392 | ID | QTS | IDR | AP0000005 |
| 6 | 1 | 1 | 100000 | 50000 | 0 | -8.03512 | 114.43404 | ID | QTS | IDR | AP0000006 |
| 7 | 1 | 1 | 100000 | 50000 | 0 | -8.01002 | 114.42675 | ID | QTS | IDR | AP0000007 |
| 8 | 1 | 1 | 100000 | 50000 | 0 | -8.01031 | 114.42667 | ID | QTS | IDR | AP0000008 |
| 9 | 1 | 1 | 100000 | 50000 | 0 | -8.01033 | 114.426 | ID | QTS | IDR | AP0000009 |
| 10 | 1 | 1 | 100000 | 50000 | 0 | -8.01044 | 114.42656 | ID | QTS | IDR | AP0000010 |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| University College London / Alan Turing Institute | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/risk-disaster-reduction/research-projects/2024/jan/future-indonesian-tsunamis-towards-end-end-quantification-risk-fitter |

### Creator
| Name | Email address | URL |
|---|---|---|
| Serge Guillas | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/statistics/people/sergeguillas |

### Contact point
| Name | Email address | URL |
|---|---|---|
| Serge Guillas, UCL | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/statistics/people/sergeguillas |

### Attributions
| Attribution identifier | Entity | Role |
|---|---|---|
| fitter_exp_distr | Oasis LMF,<br>https://www.oasislmf.org | distributor |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json



# FITTER household and business vulnerability data
## Dataset Overview
**Dataset identifier**: fitter_vln

**Title**: FITTER household and business vulnerability data

**Description**: Social vulnerability curves in Oasis format, relating qualitative levels of tsunami damage to percentage reduction in household and business asset value.

**Risk data type**: vulnerability

**Dataset version**: 1

**Dataset purpose**: Test and demonstrate the application of household data to develop social vulnerability curves in a catastrophe modelling framework

**Project title**: Future Indonesian Tsunamis: Towards End-to-end Risk quantification (FITTER)

**Additional details**: FITTER was funded by Lloyd's Tercentenary Research Foundation and Lighthill Risk Network funded research project executed by University College London (UCL).

## Vulnerability metadata
### Hazard info
| Key | Value |
|---|---|
| Primary hazard type | tsunami |
| Primary hazard process | tsunami |
| Hazard analysis type | empirical |
| Hazard intensity measurement | d_tsi:m |

### Exposure info
**Exposure category**: buildings

**Exposure taxonomy scheme**: OED

| Cost identifier | Cost dimension | Cost unit |
|---|---|---|
| 1 | structure | IDR |
| 3 | content | IDR |

### Vulnerability Impact info
**Impact type**: direct

**Impact metric**: economic_loss_value - household asset and business asset values

**Impact unit**: percentage

**Impact base data type**: observed

### Vulnerability Spatial info
**Spatial scale**: sub-national

**Countries**: IDN

### Vulnerability Functions info
#### Vulnerability function
| Key | Value |
|---|---|
| Vulnerability function approach | empirical |
| Vulnerability impact relationship type | discrete |

### Vulnerability Extra info
**Analysis details**: The curves to estimate impact on household business assets and business recovery are developed using longitudinal household survey data (two waves of the STAR longitudinal survey carried out in Banda Aceh, Sumatra, 5–14 and 17–29 months after the 2004 Indian Ocean tsunami. See https://www.sciencedirect.com/science/article/pii/S2212420922000875

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: IDN

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| vulnerability_dict | Vulnerability function dictionary | A list of vulnerability functions used in the model with associated attributes | text/csv | csv |  |  |  | resources/vln/vulnerability_dict.csv |  |  |

#### Vulnerability function dictionary
File (vulnerability_dict.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/vln/vulnerability_dict.csv)

First 10 rows displayed only

| countrycode | vulnerability_id |
|---|---|
| ID | 1 |

### Sources
| Source identifier | Name | URL | type | Component |
|---|---|---|---|---|
| fitter_vuln_STAR | Study of the Tsunami Aftermath and Recovery (STAR) | http://stardata.org/ | dataset | vulnerability |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| University College London / Alan Turing Institute | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/risk-disaster-reduction/research-projects/2024/jan/future-indonesian-tsunamis-towards-end-end-quantification-risk-fitter |

### Creator
| Name | Email address | URL |
|---|---|---|
| Rozana Himaz | r.himaz@ucl.ac.uk | https://profiles.ucl.ac.uk/83535-rozana-himaz |

### Contact point
| Name | Email address | URL |
|---|---|---|
| Rozana Himaz | r.himaz@ucl.ac.uk | https://profiles.ucl.ac.uk/83535-rozana-himaz |

### Attributions
| Attribution identifier | Entity | Role |
|---|---|---|
| fitter_vln_distr | Oasis LMF,<br>https://www.oasislmf.org | distributor |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json

### Referenced by
| Related resource identifier | Name | Author names | Publication date | URL | Digital object identifier |
|---|---|---|---|---|---|
| fitter_vuln_IJDRR22 | Business recovery in Aceh and North Sumatra following the Indian Ocean Tsunami | Rozana Himaz | 2022-04-15 | https://www.sciencedirect.com/science/article/pii/S2212420922000875?via%3Dihub | 10.1016/j.ijdrr.2022.102868 |



# FITTER loss data
## Dataset Overview
**Dataset identifier**: fitter_los

**Title**: FITTER loss data

**Description**: A set of ground up loss results for the sample property exposure is provided as an example of model output.

**Risk data type**: loss

**Dataset version**: 1

**Project title**: Future Indonesian Tsunamis: Towards End-to-end Risk quantification (FITTER)

**Additional details**: FITTER was funded by Lloyd's Tercentenary Research Foundation and Lighthill Risk Network funded research project executed by University College London (UCL).

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: IDN

### Gazetteer entries
| Gazetteer entry identifier | Scheme | Description | Uniform resource locator |
|---|---|---|---|
| fitter_los_Sum | GEONAMES | Sumatra, Indonesia | https://www.geonames.org/1626198/sumatra.html |
| fitter_los_Java | GEONAMES | Java, Indonesia | https://www.geonames.org/1642673/java.html |

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| gul_S1_aalcalc | Ground up AAL | Ground up Average Annual Loss report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_aalcalc.csv |  |  |
| gul_S1_eltcalc | Ground up ELT | Ground up Event Loss Table report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_eltcalc.csv |  |  |
| gul_S1_leccalc_full_uncertainty_aep | Ground up Aggregate LEC | Aggregate Exceedance Probability report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_leccalc_full_uncertainty_aep.csv |  |  |
| gul_S1_leccalc_full_uncertainty_oep | Ground up Occurrence LEC | Occurrence Loss Exceedance Curve report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_leccalc_full_uncertainty_oep.csv |  |  |
| gul_S1_summary-info | Ground up Summary Info | Describes the summary level for the Ground Up loss reports. | text/csv | csv |  |  |  | resources/los/gul_S1_summary-info.csv |  |  |
| analysis_settings | Analysis settings for modelled losses | The Oasis analysis settings file for modelled losses of sample exposure location file. | application/json | json |  |  |  | resources/los/analysis_settings.json |  |  |

#### Ground up AAL
File (gul_S1_aalcalc.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/los/gul_S1_aalcalc.csv)

First 10 rows displayed only

| summary_id | type | mean | standard_deviation |
|---|---|---|---|
| 1 | 1 | 159.342451 | 2316.721032 |
| 1 | 2 | 160.777295 | 3516.486117 |

#### Ground up ELT
File (gul_S1_eltcalc.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/los/gul_S1_eltcalc.csv)

First 10 rows displayed only

| summary_id | type | event_id | mean | standard_deviation | exposure_value |
|---|---|---|---|---|---|
| 1 | 1 | 2 | 25045.841797 | 0.000000 | 300000.000000 |
| 1 | 2 | 2 | 21192.226562 | 25173.708984 | 300000.000000 |
| 1 | 1 | 4 | 78263.968750 | 0.000000 | 1200000.000000 |
| 1 | 2 | 4 | 70176.328125 | 37587.273438 | 1200000.000000 |
| 1 | 1 | 13 | 14086.141602 | 0.000000 | 300000.000000 |
| 1 | 2 | 13 | 8961.675781 | 5946.729492 | 300000.000000 |
| 1 | 1 | 15 | 14086.141602 | 0.000000 | 300000.000000 |
| 1 | 2 | 15 | 18083.400391 | 33043.644531 | 300000.000000 |
| 1 | 1 | 23 | 7043.070312 | 0.000000 | 150000.000000 |
| 1 | 2 | 23 | 4026.737793 | 2375.948730 | 150000.000000 |

#### Ground up Aggregate LEC
File (gul_S1_leccalc_full_uncertainty_aep.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/los/gul_S1_leccalc_full_uncertainty_aep.csv)

First 10 rows displayed only

| summary_id | type | return_period | loss |
|---|---|---|---|
| 1 | 1 | 1000.000000 | 44611.835938 |
| 1 | 1 | 990.000000 | 44611.835938 |
| 1 | 1 | 980.000000 | 44611.835938 |
| 1 | 1 | 970.000000 | 44611.835938 |
| 1 | 1 | 960.000000 | 44611.835938 |
| 1 | 1 | 950.000000 | 44611.835938 |
| 1 | 1 | 940.000000 | 44611.835938 |
| 1 | 1 | 930.000000 | 44611.835938 |
| 1 | 1 | 920.000000 | 44611.835938 |
| 1 | 1 | 910.000000 | 44611.835938 |

#### Ground up Occurrence LEC
File (gul_S1_leccalc_full_uncertainty_oep.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/los/gul_S1_leccalc_full_uncertainty_oep.csv)

First 10 rows displayed only

| summary_id | type | return_period | loss |
|---|---|---|---|
| 1 | 1 | 1000.000000 | 44611.835938 |
| 1 | 1 | 990.000000 | 44611.835938 |
| 1 | 1 | 980.000000 | 44611.835938 |
| 1 | 1 | 970.000000 | 44611.835938 |
| 1 | 1 | 960.000000 | 44611.835938 |
| 1 | 1 | 950.000000 | 44611.835938 |
| 1 | 1 | 940.000000 | 44611.835938 |
| 1 | 1 | 930.000000 | 44611.835938 |
| 1 | 1 | 920.000000 | 44611.835938 |
| 1 | 1 | 910.000000 | 44611.835938 |

#### Ground up Summary Info
File (gul_S1_summary-info.csv) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/los/gul_S1_summary-info.csv)

First 10 rows displayed only

| summary_id | _not_set_ | tiv |
|---|---|---|
| 1 | All-Risks | 1500000.0 |

#### Analysis settings for modelled losses
File (analysis_settings.json) found [here](/home/anish/Documents/github/UCLFitter/docs/resources/los/analysis_settings.json)

Cannot display preview for json files

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| University College London / Alan Turing Institute | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/risk-disaster-reduction/research-projects/2024/jan/future-indonesian-tsunamis-towards-end-end-quantification-risk-fitter |

### Creator
| Name | Email address | URL |
|---|---|---|
| Dimitra Salmanidou | d.salmanidou.12@ucl.ac.uk | https://www.researchgate.net/profile/Dimitra-Salmanidou |

### Contact point
| Name | Email address | URL |
|---|---|---|
| Serge Guillas, UCL | s.guillas@ucl.ac.uk | https://www.ucl.ac.uk/statistics/people/sergeguillas |

### Attributions
| Attribution identifier | Entity | Role |
|---|---|---|
| fitter_los_distr | Oasis LMF,<br>https://www.oasislmf.org | distributor |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json

### Referenced by
| Related resource identifier | Name | Author names | Publication date | URL | Digital object identifier |
|---|---|---|---|---|---|
| fitter_los_IJDRR21 | Impact of future tsunamis from the Java trench on household welfare: Merging geophysics and economics through catastrophe modelling | "Dimitra M. Salmanidou,<br> Ayao Ehara,<br> Rozana Himaz,<br> Mohammad Heidarzadeh,<br> Serge Guillas" | 2021-04-26 | https://www.sciencedirect.com/science/article/pii/S2212420921002570 | 10.1016/j.ijdrr.2021.102291 |



