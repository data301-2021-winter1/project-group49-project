#Method chaining

import pandas as pd

def load_and_process(location):
    

# Method chaining begins

    df = (   
        pd.read_csv(location, sep = ",")
        .drop([' 77516',' 13',' 2174',' 0', ' Not-in-family', ' 40'],axis=1)
        .rename(columns={'39': 'Age', ' State-gov': 'Industry', ' Bachelors': 'Education'})
        .rename(columns={' Never-married': 'Marital Stat', ' Adm-clerical': 'Position'})
        .rename(columns={' White': 'Race', ' Male': 'Gender', ' United-States': 'Country', ' <=50K':'Income'})
        .fillna(np.nan)
        .drop_duplicates()
        .dropna()
        .sort_values("Age", ascending=True)
        .reset_index()
        .drop(columns=['index'])
        
        

    )

    return df


