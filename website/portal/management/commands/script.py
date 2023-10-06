import pandas as pd
from portal.models import College

cleaned_df = pd.read_csv('/home/poseidon/Desktop/code/ml/josaa_analysis/website/portal/data/2022_all_6.csv')
for index, row in cleaned_df.iterrows():
    instance = College(
        institute=row['Institute'],
        program_name=row['Academic Program Name'],
        quota=row['Quota'],
        seat_type=row['Seat Type'],
        gender=row['Gender'],
        opening_rank=row['Opening Rank'],
        closing_rank=row['Closing Rank'],
        year=row['Year'],
        round=row['Round'],
        # Set values for other fields
    )
    instance.save()
