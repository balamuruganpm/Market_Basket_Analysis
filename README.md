# Project 10: Market Basket Insights

**Project Title**: Market Basket Analysis

**Problem Statement**: Unveiling Customer Behaviour through Association Analysis: Utilize market basket analysis on the provided dataset to uncover hidden patterns and associations between products, aiming to understand customer purchasing behaviour and identify potential cross-selling opportunities for the retail business.

## Algorithms used in market basket analysis:

Market basket analysis utilizes association rule ***{IF} - > {THEN}*** to predict the probability of certain products being purchased together. They count the item frequency occurring together and seek to find associations that occur more than expected.

> Some algorithms that leverage these association rules are AIS, Apriori, and SETM.

Apriori is the commonly cited algorithm by the data scientist that identifies frequent items in the database. It is useful for unsupervised learning and requires no training and thus no predictions. This algorithm is used especially for large data sets where useful relationships among the items are to be determined.
You would be surprised to know that Apriori algorithm leverages a shortcut namely Apriori property. This shortcut states that all items in a frequent itemset must also be frequent. It helps in saving a lot of computational time.

The Apriori algorithm works in two steps that are illustrated below.

```
1.It identifies the itemsets systematically that occur frequently in the dataset and support greater than the pre-specified threshold value.
2.Next, it calculates the confidence of all possible rules. However, it only keeps those items states that have confidence greater than a pre-specified threshold.
```

### It is further classified into three components.

```
- Support
- Lift
- Confidence
```
## How does market basket analysis work?

Market basket analysis is based on association rule mining which is ```IF {}, THEN {} construct```

## Example

Import the necessary libraries

```
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#for viz
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

#to avoid warning
import warnings
warnings.filterwarnings('ignore')

#to display all feature if the number increase
pd.set_option('display.max_columns', None)
```

Data preprocessing

```
dataset = pd.read_excel('/kaggle/input/market-basket-analysis/Assignment-1_Data.xlsx')
```
