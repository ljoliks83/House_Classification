# Your code here. The DataFrame is already loaded as grades
stud_series = pd.Series(grades.mean(axis='columns', numeric_only=True))

print(stud_series)