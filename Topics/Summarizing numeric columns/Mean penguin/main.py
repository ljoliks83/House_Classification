# Your code here. The DataFrame is already loaded as penguins_example. 
bl_mean = penguins_example.bill_length_mm.mean()
bd_mean = penguins_example.bill_depth_mm.mean()
print(bl_mean / bd_mean)