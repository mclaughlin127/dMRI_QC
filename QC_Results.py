import pandas as pd

# importing csv
results = pd.read_csv(r'./raw_output.csv')
df = results.drop(columns=['GT Class'])

# Parsing out bad volumes
bad_vol_idx = pd.DataFrame(index=range(df.shape[0]), columns=['Predicted Logical'])

for x in range(len(df)):
    # Creating a logical index of bad volumes
    if df.loc[x, "Predicted Class"] == 'bad':
        bad_vol_idx.loc[x, 'Predicted Logical'] = 1
    elif df.loc[x, "Predicted Class"] == 'good':
        bad_vol_idx.loc[x, 'Predicted Logical'] = 0

# Joining it with the original table df
df2 = pd.concat([df, bad_vol_idx], axis=1)

# Reducing File Name col of df2 to just the IDs (1st 4 characters)
for i in range(len(df2)):
    fn = df2.loc[i, "File Name"]
    df2.loc[i, "File Name"] = fn[:4]
print(df2)

# Extracting each ID
id = df2['File Name'].unique()

# Count total bad volumes for each ID
bad_vol_count = pd.DataFrame(index=range(len(id)), columns=['ID', 'Pred tot_bad_vol'])
for y in range(len(id)):
    tot_bad_vol = 0
    for z in range(len(df2)):
        if df2.loc[z, 'File Name'] == id[y]:
            tot_bad_vol = tot_bad_vol + df2.loc[z, 'Predicted Logical']
    bad_vol_count.loc[y, 'ID'] = id[y]
    bad_vol_count.loc[y, 'Pred tot_bad_vol'] = tot_bad_vol


# Determining and adding scores and usability to table
for j in range(len(bad_vol_count)):
    bad_vols = bad_vol_count.loc[j, 'Pred tot_bad_vol']
    if bad_vols >= 15:
        vqc = 1
        usable = 'N'
    elif 1 <= bad_vols <= 14:
        vqc = 2
        usable = 'Y'
    elif bad_vols == 0:
        vqc = 3
        usable = 'Y'
    bad_vol_count.loc[j, 'Pred vqc'] = vqc
    bad_vol_count.loc[j, 'Pred usable?'] = usable

print(bad_vol_count)
bad_vol_count = bad_vol_count.sort_values(by='ID')
bad_vol_count.to_csv('./scored_results.csv', index=False)
