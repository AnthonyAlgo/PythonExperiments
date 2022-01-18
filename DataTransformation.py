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
    data_frame.loc[x] = ['Honda',5]
print(data_frame)

print(data_frame.loc[1, 'cars'])

def test_map(x: int):
  if x > 1:
    return 1
transformed_df = data_frame['rating'].map(test_map)
print(transformed_df)