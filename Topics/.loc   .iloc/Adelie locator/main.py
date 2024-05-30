# put your code here. The data frame is already loaded and stored as penguins_df. 
df = penguins_df.loc[penguins_df.species == 'Adelie', 'island'::2]

print(df)