import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"], 
  'rating': [3, 7, 0]
}
print(type(mydataset))

data_frame = pd.DataFrame(mydataset)
print(data_frame)

print(data_frame.loc[0])
print(data_frame['cars'])

for x in data_frame.index:
  if data_frame.loc[x, 'rating'] < 5:
    data_frame.loc[x] = 5, 'Honda'
print(data_frame)