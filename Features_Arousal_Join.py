import pandas as pd
import numpy as np

# Loading the two CSV files
file1 = r"C:\Users\Salin\OneDrive\Documentos\ESSEX\DSPROJECT\PPG_HR_Analysis_Longer_Intervals_with_SW\merged_features_norm_grey_SW.csv"# Normalized Features
file2 = r"C:\Users\Salin\OneDrive\Documentos\ESSEX\DSPROJECT\individual_ground_truth.csv" # Ground Truth

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Renaming columns to match for merging
df1.rename(columns={'SourceStimuliName': 'Stimulus'}, inplace=True)
df2.rename(columns={'Stimulus_Name': 'Stimulus'}, inplace=True)

# Merging on 'Participant' and 'Stimulus'
merged_df = df1.merge(df2[['Participant', 'Stimulus', 'Arousal']], on=['Participant', 'Stimulus'], how='left')

# Warning if there are participants without arousal values
missing_arousal = merged_df[merged_df['Arousal'].isna()]['Participant'].unique()
if len(missing_arousal) > 0:
    print("Warning: 'Arousal' value not found for the following participants:")
    for p in missing_arousal:
        print(f"  - Participant {p}")
else:
    print("All participants have 'Arousal' values.")

merged_df = merged_df.dropna(subset=['Arousal'])

# Saving the merged file
output_path = r"C:\Users\Salin\OneDrive\Documentos\ESSEX\DSPROJECT\PPG_HR_Analysis_Longer_Intervals_with_SW\merged_features_norm_grey_arousal_SW.csv"
merged_df.to_csv(output_path, index=False)



print(f"\nMerged rows: {merged_df.shape[0]} / Original rows: {df1.shape[0]}")
dropped = df1.shape[0] - merged_df.shape[0]
print(f"Rows without arousal removed: {dropped}")


print(f"\nMerged file saved at: {output_path}")