# Store Cannibalization and Cross-Store Overlap Analysis

## Overview

This report analyzes synthetic GPS-to-store matching records
to identify devices detected within multiple store catchment areas.

The results are potential cross-store overlap indicators.
They do not establish actual customer movement, store switching,
or confirmed retail cannibalization.

## Dataset Summary

- GPS-to-store matching records: 6,860
- Matched devices: 1,000
- Stores analyzed: 4
- Store pairs analyzed: 6
- Devices detected near multiple stores: 1,000

## Store-Level Device Summary

| StoreID   | StoreName        |   UniqueMatchedDevices |
|:----------|:-----------------|-----------------------:|
| ADY01     | Adyar_Store      |                    842 |
| ANN01     | Anna_Nagar_Store |                    850 |
| TNG01     | T_Nagar_Store    |                    843 |
| VEL01     | Velachery_Store  |                    850 |

## Store-Pair Overlap

| StoreA   | StoreB   |   DevicesInStoreA |   DevicesInStoreB |   SharedDevices |   JaccardSimilarity |   OverlapPercentage |
|:---------|:---------|------------------:|------------------:|----------------:|--------------------:|--------------------:|
| ADY01    | ANN01    |               842 |               850 |             708 |              0.7195 |               71.95 |
| ADY01    | TNG01    |               842 |               843 |             696 |              0.7037 |               70.37 |
| ADY01    | VEL01    |               842 |               850 |             704 |              0.7126 |               71.26 |
| ANN01    | TNG01    |               850 |               843 |             705 |              0.7136 |               71.36 |
| ANN01    | VEL01    |               850 |               850 |             718 |              0.7312 |               73.12 |
| TNG01    | VEL01    |               843 |               850 |             707 |              0.717  |               71.7  |

## Key Findings

- Highest pairwise overlap: ANN01 and
  VEL01, with
  718 shared devices and
  73.12% Jaccard similarity.

- Lowest pairwise overlap: ADY01 and
  TNG01, with
  696 shared devices and
  70.37% Jaccard similarity.

## Methodology

For each store pair, shared devices are calculated using set
intersection.

Jaccard similarity is calculated as:

J(A, B) = |A intersection B| / |A union B|

## Limitations

- The GPS dataset is synthetic.
- GPS pings are independently generated rather than continuous trajectories.
- Devices detected near multiple stores are not necessarily customers
  visiting or switching between those stores.
- High overlap does not prove geographic competition or cannibalization.
- Further analysis with real, consented mobility data and verified
  store locations would be required for business conclusions.
