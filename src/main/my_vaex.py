import vaex

# Sample usage with 'bigfile.csv' (a larger dataset for demo)
df = vaex.open("../../data/bigfile.csv")
result = df[df.x > 0].mean(df.y)
print(result)
