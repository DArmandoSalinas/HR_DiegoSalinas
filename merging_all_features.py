import pandas as pd

# Loading the two datasets
df1 = pd.read_csv(r"C:\Users\Salin\OneDrive\Documentos\ESSEX\DSPROJECT\PPG_HR_Analysis_Longer_Intervals_with_SW\Time_Frequency_Features_SW.csv")
df2 = pd.read_csv(r"C:\Users\Salin\OneDrive\Documentos\ESSEX\DSPROJECT\PPG_HR_Analysis_Longer_Intervals_with_SW\PoincarePlots_SW\All_Participants_PoincareMetrics.csv")

# Standardizing column names
# df2.rename(columns={'Stimulus': 'SourceStimuliName'}, inplace=True)

# Row counts before merge
print(f"Rows in Time/Frequency features: {len(df1)}")
print(f"Rows in Poincaré features:      {len(df2)}")


# Merging the dataframes on 'Participant' and 'Stimulus'
merged_df = pd.merge(df1, df2, on=['Participant', 'SourceStimuliName', 'Window_Index'], how='inner')

print(f"Rows after merge:               {len(merged_df)}")

# Loss check
lost_rows_df1 = len(df1) - len(merged_df)
lost_rows_df2 = len(df2) - len(merged_df)

print(f"\nRows from df1 not matched:      {lost_rows_df1}")
print(f"Rows from df2 not matched:      {lost_rows_df2}")

# Saving the merged file
output = r"C:\Users\Salin\OneDrive\Documentos\ESSEX\DSPROJECT\PPG_HR_Analysis_Longer_Intervals_with_SW\merged_features_SW.csv"
merged_df.to_csv(output, index=False)

print("Merged file saved as 'merged_features.csv'")


