import pandas as pd

# create Pandas Dataframe from a dictionary
df = pd.DataFrame({'row': [5, 6, 7],
                   'loop': [1, 1, 2],
                   'One_X': [1.1, 1.1, 1.1],
                   'One_Y': [1.2, 1.2, 1.2],
                  'Two_X': [5, 5, 5],
                   'Two_Y': [10, 10, 10]})

# As Labelled Index
df = df.set_index(['row', 'loop'])

# With Hierarchical Columns
df.columns = pd.MultiIndex.from_tuples([tuple(c.split('_'))
                                        for c in df.columns])

# Now stack & Reset
df = df.stack(0)

df = df.reset_index(2)

# And fix the labels (Notice the label 'level_1' got added automatically)
df.columns = ['Sample','All_X','All_Y']
